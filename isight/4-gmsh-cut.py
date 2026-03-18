import gmsh

gmsh.initialize()
gmsh.model.add("model")
gmsh.merge('model-qie.stp')
gmsh.model.occ.synchronize()
surface_id_before = gmsh.model.occ.getEntities(2)
gmsh.model.occ.synchronize()

with open('D:/Work_Directory_new/bianliang.txt', encoding='utf-8') as f:
    long = float(f.read().replace(' ', '').split('=')[1])
gmsh.model.occ.addRectangle(-1/2*long,-5,0,long,10,9999)
gmsh.model.occ.synchronize()
gmsh.model.occ.intersect(surface_id_before,[(2,9999)])
gmsh.model.occ.synchronize()

gmsh.write("model-cut.stp")
#gmsh.fltk.run()
gmsh.finalize()
