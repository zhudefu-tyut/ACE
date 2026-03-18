import gmsh

gmsh.initialize()
gmsh.model.add("diceng")

gmsh.model.occ.addRectangle(0,0,0,160,40,0)
gmsh.model.occ.addPoint(0,17.4,0)
gmsh.model.occ.addPoint(160,17.4,0)
gmsh.model.occ.addPoint(0,23,0)
gmsh.model.occ.addPoint(160,23,0)
gmsh.model.occ.addPoint(0,28,0)
gmsh.model.occ.addPoint(160,28,0)

with open('bianliang.txt', encoding='utf-8') as f:
    spacing_zhu = float(f.read().replace(' ', '').split('=')[1])
long_caikongqu = 5
gmsh.model.occ.addPoint(80-2.5*spacing_zhu-3*long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80-2.5*spacing_zhu-3*long_caikongqu,23,0)

gmsh.model.occ.addPoint(80-2.5*spacing_zhu-2*long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80-2.5*spacing_zhu-2*long_caikongqu,23,0)

gmsh.model.occ.addPoint(80-1.5*spacing_zhu-2*long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80-1.5*spacing_zhu-2*long_caikongqu,23,0)

gmsh.model.occ.addPoint(80-1.5*spacing_zhu-long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80-1.5*spacing_zhu-long_caikongqu,23,0)

gmsh.model.occ.addPoint(80-0.5*spacing_zhu-long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80-0.5*spacing_zhu-long_caikongqu,23,0)

gmsh.model.occ.addPoint(80-0.5*spacing_zhu,17.4,0)
gmsh.model.occ.addPoint(80-0.5*spacing_zhu,23,0)

gmsh.model.occ.addPoint(80+0.5*spacing_zhu,17.4,0)
gmsh.model.occ.addPoint(80+0.5*spacing_zhu,23,0)

gmsh.model.occ.addPoint(80+0.5*spacing_zhu+long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80+0.5*spacing_zhu+long_caikongqu,23,0)

gmsh.model.occ.addPoint(80+1.5*spacing_zhu+long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80+1.5*spacing_zhu+long_caikongqu,23,0)

gmsh.model.occ.addPoint(80+1.5*spacing_zhu+2*long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80+1.5*spacing_zhu+2*long_caikongqu,23,0)

gmsh.model.occ.addPoint(80+2.5*spacing_zhu+2*long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80+2.5*spacing_zhu+2*long_caikongqu,23,0)

gmsh.model.occ.addPoint(80+2.5*spacing_zhu+3*long_caikongqu,17.4,0)
gmsh.model.occ.addPoint(80+2.5*spacing_zhu+3*long_caikongqu,23,0)

gmsh.model.occ.addLine(5,6)
gmsh.model.occ.addLine(7,8)
gmsh.model.occ.addLine(9,10)

gmsh.model.occ.addLine(11,12)
gmsh.model.occ.addLine(13,14)
gmsh.model.occ.addLine(15,16)
gmsh.model.occ.addLine(17,18)
gmsh.model.occ.addLine(19,20)
gmsh.model.occ.addLine(21,22)
gmsh.model.occ.addLine(23,24)
gmsh.model.occ.addLine(25,26)
gmsh.model.occ.addLine(27,28)
gmsh.model.occ.addLine(29,30)
gmsh.model.occ.addLine(31,32)
gmsh.model.occ.addLine(33,34)

diceng = list()
for i in range(5,20):
    a = [(1,i)]
    diceng.extend(a)

gmsh.model.occ.fragment([(2,0)],diceng,-1,-1,1)

gmsh.model.occ.synchronize()

gmsh.write("model-diceng.stp")
gmsh.fltk.run()
