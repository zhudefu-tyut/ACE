import gmsh
import sys

gmsh.initialize()
gmsh.model.add("model")

gmsh.merge('model-repair-AP214.stp')
area_threshold = 0.0001
surfaces = gmsh.model.getEntities(2)
#repair small face
to_remove_surface = []
to_remove_edge_set = set()
to_remove_point_set = set()

for dim, tag in surfaces:
    area = gmsh.model.occ.getMass(dim, tag)
    if area < area_threshold:
        to_remove_surface.append((dim, tag))

for i in to_remove_surface:
    a = gmsh.model.getAdjacencies(i[0], i[1])[1]
    for j in a:
        to_remove_edge_set.add((1,j))
        b = gmsh.model.getAdjacencies(1, j)[1]
        for k in b:
            to_remove_point_set.add((0,k))

to_remove_edge = list(to_remove_edge_set)
to_remove_point = list(to_remove_point_set)
gmsh.model.occ.remove(to_remove_surface, recursive=False)
gmsh.model.occ.remove(to_remove_edge, recursive=False)
gmsh.model.occ.remove(to_remove_point, recursive=False)
gmsh.model.occ.synchronize()

to_remove_surface_after = []
surfaces = gmsh.model.getEntities(2)
for dim, tag in surfaces:
    area = gmsh.model.occ.getMass(dim, tag)
    if area < area_threshold:
        to_remove_surface_after.append((dim, tag))

gmsh.model.occ.synchronize()
surface_id_before = gmsh.model.occ.getEntities(2)
gmsh.model.occ.synchronize()

#gmsh.model.occ.dilate(surface_id_before, 0.0, 0.0, 0.0, 0.001, 0.001, 0.001)

gmsh.model.occ.synchronize()

gmsh.model.occ.addRectangle(-10,-10,0,20,20,9999)

gmsh.model.occ.synchronize()

gmsh.model.occ.intersect(surface_id_before,[(2,9999)])
gmsh.model.occ.synchronize()
mesh_else = 0.1
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

#dingbina PhysicalGroup
Y_TARGET = 2.8
TOL = 0.01

dim_tags = gmsh.model.getEntities(1)

dingbian_tags = []
for dim, tag in dim_tags:
    xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.getBoundingBox(dim, tag)
    if abs(ymin - Y_TARGET) < TOL and abs(ymax - Y_TARGET) < TOL:
        dingbian_tags.append(tag)

pg_tag = gmsh.model.addPhysicalGroup(1, dingbian_tags, 10000,name="dingbian")

Y_TARGET = -2.8
TOL = 0.01

dim_tags = gmsh.model.getEntities(1)

dingbian_tags = []
for dim, tag in dim_tags:
    xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.getBoundingBox(dim, tag)
    if abs(ymin - Y_TARGET) < TOL and abs(ymax - Y_TARGET) < TOL:
        dingbian_tags.append(tag)

pg_tag = gmsh.model.addPhysicalGroup(1, dingbian_tags, 10001,name="dibian")

with open('D:/Work_Directory_new/bianliang.txt', encoding='utf-8') as f:
    spacing_zhu = float(f.read().replace(' ', '').split('=')[1])
X = spacing_zhu/2
X_TARGET = -X
TOL = 0.03

dim_tags = gmsh.model.getEntities(1)

dingbian_tags = []
for dim, tag in dim_tags:
    xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.getBoundingBox(dim, tag)
    if abs(xmin - X_TARGET) < TOL and abs(xmax - X_TARGET) < TOL:
        dingbian_tags.append(tag)

pg_tag = gmsh.model.addPhysicalGroup(1, dingbian_tags, 10002,name="zuobian")

X_TARGET = X
TOL = 0.03

dim_tags = gmsh.model.getEntities(1)

dingbian_tags = []
for dim, tag in dim_tags:
    xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.getBoundingBox(dim, tag)
    if abs(xmin - X_TARGET) < TOL and abs(xmax - X_TARGET) < TOL:
        dingbian_tags.append(tag)

pg_tag = gmsh.model.addPhysicalGroup(1, dingbian_tags, 10003,name="youbian")

gmsh.model.geo.synchronize()

gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 1)

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(2)
gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 1)
gmsh.option.setNumber("Mesh.SaveAll", 0)
gmsh.write("information1.inp")
#yuan gongneng
gmsh.model.removePhysicalGroups([(1, 10000), (1, 10001), (1, 10002), (1, 10003)])
edges = gmsh.model.getEntities(1)

inside_ids = set()
for dim, tag in edges:
    adj = gmsh.model.get_adjacencies(1, tag)
    if len(adj[0]) == 2:
        inside_ids.add(tag)

for i in inside_ids:
    gmsh.model.addPhysicalGroup(1, [i], i, name="line" + str(i))

gmsh.model.occ.synchronize()

gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 1)

gmsh.model.occ.synchronize()

#gmsh.model.mesh.generate(2)
gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 1)
gmsh.option.setNumber("Mesh.SaveAll", 0)
gmsh.write("information.inp")
gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 0)
gmsh.option.setNumber("Mesh.SaveAll", 1)
gmsh.write("output.inp")

#gmsh.fltk.run()

start_marker = "*ELEMENT, type=T3D2, ELSET=Line1"
end_marker = "*ELEMENT, type=CPS3,"
input_file_path = 'output.inp'
output_file_path = 'model.inp'
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
deleting = False
result = []
for line in lines:
    if start_marker in line:
        deleting = True
        continue
    if not deleting:
        result.append(line)
    if end_marker in line:
        deleting = False
        result.append(line)
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(result)

#  finalize Gmsh
gmsh.finalize()
