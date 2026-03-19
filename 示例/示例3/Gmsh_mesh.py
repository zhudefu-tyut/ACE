import gmsh

gmsh.initialize()
gmsh.model.add("model")

gmsh.merge('model-repair-AP214.stp')

gmsh.model.occ.synchronize()
surface_id_before = gmsh.model.occ.getEntities(2)
gmsh.model.occ.synchronize()

gmsh.model.occ.dilate(surface_id_before, 0.0, 0.0, 0.0, 0.001, 0.001, 0.001)

gmsh.model.occ.synchronize()

gmsh.model.occ.addRectangle(-1,-1,0,2,2,9999)

gmsh.model.occ.synchronize()

gmsh.model.occ.intersect(surface_id_before,[(2,9999)])
gmsh.model.occ.synchronize()
mesh_else = 0.003
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), mesh_else)
gmsh.model.occ.synchronize()

edges = gmsh.model.getEntities(1)

inside_ids = set()
for dim, tag in edges:
    adj = gmsh.model.get_adjacencies(1, tag)
    if len(adj[0]) == 2:
        inside_ids.add(tag)

for i in inside_ids:
    gmsh.model.addPhysicalGroup(1, [i], i, name="line" + str(i))

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

gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 1)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 1)

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(2)
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