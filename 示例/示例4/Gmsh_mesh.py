import gmsh
import numpy as np

gmsh.initialize()
gmsh.model.add("model")
gmsh.merge('1001.stp')
gmsh.model.occ.synchronize()

surface_id_before = gmsh.model.occ.getEntities(dim=2)
gmsh.model.occ.addRectangle(-50, -50, 0, 100, 100, 99999)
gmsh.model.occ.intersect([(2,99999)], surface_id_before)
gmsh.model.occ.synchronize()

surfaces = gmsh.model.getEntities(dim=2)

for dim, tag in surfaces:
    # 每个面用自己的 tag 作为 Physical Group 的 tag（方便对应）
    gmsh.model.addPhysicalGroup(
        dim=2,
        tags=[tag],
        tag=tag,                  # 也可以用其他编号方式，例如自增计数器
        name=f"surf_{tag}"
    )

print(f"共创建 {len(surfaces)} 个 surface Physical Group")


edges = gmsh.model.getEntities(dim=1)
inside_edges = []
for dim, etag in edges:
    # 获取该边相邻的高维实体（通常是面）
    upward_adj, _ = gmsh.model.get_adjacencies(1, etag)
    if len(upward_adj) == 2:           # 正好被两个面共享 → 内部边
        inside_edges.append((etag, upward_adj[0], upward_adj[1]))


for etag, _, _ in inside_edges:
    gmsh.model.addPhysicalGroup(
        dim=1,
        tags=[etag],
        tag=etag,
        name=f"edge_{etag}"
    )

gmsh.model.occ.synchronize()

mesh_else = 2
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), mesh_else)
gmsh.model.occ.synchronize()

entities = gmsh.model.getEntities()

points_dict = {}

for entity in entities:
    dim, tag = entity
    if dim == 0:
        points_dict[tag] =  mesh_else

lines = gmsh.model.getEntities(dim=1)
for line in lines:
    line_tag = line[1]
    points = gmsh.model.getBoundary([line], oriented=False)

    point_tags = [p[1] for p in points]

    if len(point_tags) == 2:
        point_tag_1 = point_tags[0]
        point_tag_2 = point_tags[1]
        point1_coords = gmsh.model.getBoundingBox(0, point_tag_1)
        point2_coords = gmsh.model.getBoundingBox(0, point_tag_2)

        length = ((point1_coords[0] - point2_coords[0]) ** 2 +
                  (point1_coords[1] - point2_coords[1]) ** 2 +
                  (point1_coords[2] - point2_coords[2]) ** 2) ** 0.5
        if length < mesh_else:
            gmsh.model.mesh.setTransfiniteCurve(line_tag, 2)
            value_1 = points_dict.get(point_tag_1)
            value_2 = points_dict.get(point_tag_2)
            if value_1 > length:
                points_dict[point_tag_1] = length/1.1
            if value_2 > length:
                points_dict[point_tag_2] = length/1.1
            #small_lines_tags.append(line_tag)

for point_tag, value in points_dict.items():
    gmsh.model.mesh.setSize([(0, point_tag)], value)

gmsh.model.occ.synchronize()

gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 1)

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(2)
gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 1)
gmsh.option.setNumber("Mesh.SaveAll", 0)
gmsh.write("test.inp")
gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 0)
gmsh.option.setNumber("Mesh.SaveAll", 1)
#gmsh.write("test.inp")

areas = {}
total_area = 0.0
for dim, tag in gmsh.model.getEntities(dim=2):
    area = gmsh.model.occ.get_mass(dim, tag)
    areas[tag] = area
    total_area += area

with open("test.inp", "a", encoding="utf-8") as f:
    for tag, area in sorted(areas.items()):
        f.write(f"**{tag}:{area:.4f}\n")

#gmsh.fltk.run()
gmsh.finalize()