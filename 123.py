import gmsh

# 初始化 Gmsh
gmsh.initialize()
gmsh.option.setNumber("General.Terminal", 1)

# 添加模型并导入 STEP 文件
model_name = "example"
gmsh.model.add(model_name)
gmsh.merge("2.stp")  # 替换为你的 STEP 文件路径
gmsh.model.occ.synchronize()
gmsh.model.occ.healShapes()
gmsh.model.occ.synchronize()

mesh_else = 1
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), mesh_else)
gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(2)


start_id = 1
line_max_id = gmsh.model.occ.get_max_tag(1)
inside_ids = set()
for i in range(start_id,line_max_id+1):
    p = gmsh.model.get_adjacencies(1,i)
    if len(p[0]) == 2:
        inside_ids.add(i)
for i in inside_ids:
    gmsh.model.addPhysicalGroup(1,[0+i], i,"line"+str(i))
gmsh.model.occ.synchronize()

gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 1)
gmsh.option.setNumber("Mesh.SaveAll", 0)
gmsh.write("information.inp")
gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 0)
gmsh.option.setNumber("Mesh.SaveAll", 1)
gmsh.write("model.inp")

gmsh.fltk.run()

start_marker = "*ELEMENT, type=T3D2, ELSET=Line1"
end_marker = "*ELEMENT, type=CPS3, ELSET=Surface1\n"
input_file_path = 'model.inp'
output_file_path = 'output.inp'
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