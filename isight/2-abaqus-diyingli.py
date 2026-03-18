# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-20.55.25 RELr426 190762
# Run by gbl on Tue Nov 18 20:50:31 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=322.670806884766,
    height=138.133331298828)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
step = mdb.openStep('D:/Work_Directory_new/model-diceng.stp', scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(name='model', geometryFile=step,
    combine=True, retainBoundary=True, mergeSolidRegions=True,
    dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['model']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#Material
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='baiyunyan_di')
mdb.models['Model-1'].materials['baiyunyan_di'].Density(table=((2860.0, ), ))
mdb.models['Model-1'].materials['baiyunyan_di'].Elastic(table=((50080000000.0,
    0.35), ))
mdb.models['Model-1'].Material(name='baiyunyan_ding')
mdb.models['Model-1'].materials['baiyunyan_ding'].Density(table=((2761.0, ), ))
mdb.models['Model-1'].materials['baiyunyan_ding'].Elastic(table=((
    42970000000.0, 0.29), ))
mdb.models['Model-1'].Material(name='lvtuyan')
mdb.models['Model-1'].materials['lvtuyan'].Density(table=((2782.0, ), ))
mdb.models['Model-1'].materials['lvtuyan'].Elastic(table=((24180000000.0,
    0.25), ))
mdb.models['Model-1'].Material(name='niantuyan')
mdb.models['Model-1'].materials['niantuyan'].Density(table=((2640.0, ), ))
mdb.models['Model-1'].materials['niantuyan'].Elastic(table=((12450000000.0,
    0.25), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='baiyunyan_di',
    material='baiyunyan_di', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='baiyunyan_ding',
    material='baiyunyan_ding', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='lvtuyan',
    material='lvtuyan', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='niantuyan',
    material='niantuyan', thickness=None)

p = mdb.models['Model-1'].parts['model']
baiyunyan_di = p.faces.findAt(((80,1,0), ))
p.Set(faces=(baiyunyan_di,), name='baiyunyan_di')

baiyunyan_ding = p.faces.findAt(((80,29,0), ))
p.Set(faces=(baiyunyan_ding,), name='baiyunyan_ding')

niantuyan = p.faces.findAt(((80,24,0), ))
p.Set(faces=(niantuyan,), name='niantuyan')

with open('D:/Work_Directory_new/bianliang.txt', encoding='utf-8') as f:
    spacing_zhu = float(f.read().replace(' ', '').split('=')[1])
long_caikongqu = 5
lvtuyan1 = p.faces.findAt(((1,18,0), ))
lvtuyan2 = p.faces.findAt(((80-2.6*spacing_zhu-2*long_caikongqu,18,0), ))
lvtuyan3 = p.faces.findAt(((80-1.6*spacing_zhu-2*long_caikongqu,18,0), ))
lvtuyan4 = p.faces.findAt(((80-1.6*spacing_zhu-long_caikongqu,18,0), ))
lvtuyan5 = p.faces.findAt(((80-0.6*spacing_zhu-long_caikongqu,18,0), ))
lvtuyan6 = p.faces.findAt(((80-0.6*spacing_zhu,18,0), ))
lvtuyan7 = p.faces.findAt(((80,18,0), ))
lvtuyan8 = p.faces.findAt(((80+0.6*spacing_zhu,18,0),))
lvtuyan9 = p.faces.findAt(((80+0.6*spacing_zhu+long_caikongqu,18,0),))
lvtuyan10 = p.faces.findAt(((80+1.6*spacing_zhu+long_caikongqu,18,0),))
lvtuyan11 = p.faces.findAt(((80+1.6*spacing_zhu+2*long_caikongqu,18,0),))
lvtuyan12 = p.faces.findAt(((80+2.6*spacing_zhu+2*long_caikongqu,18,0),))
lvtuyan13 = p.faces.findAt(((159,18,0), ))
p.Set(faces=(lvtuyan1,lvtuyan2,lvtuyan3,lvtuyan4,lvtuyan5,lvtuyan6,lvtuyan7,lvtuyan8,lvtuyan9,lvtuyan10,lvtuyan11,lvtuyan12,lvtuyan13,), name='lvtuyan')
p.Set(faces=(lvtuyan2,lvtuyan4,lvtuyan6,lvtuyan8,lvtuyan10,lvtuyan12,), name='kaiwa')

ce_edge1 = p.edges.findAt(((0, 1, 0), ))
ce_edge2 = p.edges.findAt(((0, 18, 0), ))
ce_edge3 = p.edges.findAt(((0, 24, 0), ))
ce_edge4 = p.edges.findAt(((0, 29, 0), ))
ce_edge5 = p.edges.findAt(((160, 1, 0), ))
ce_edge6 = p.edges.findAt(((160, 18, 0), ))
ce_edge7 = p.edges.findAt(((160, 24, 0), ))
ce_edge8 = p.edges.findAt(((160, 29, 0), ))
p.Set(edges=(ce_edge1,ce_edge2,ce_edge3,ce_edge4,ce_edge5,ce_edge6,ce_edge7,ce_edge8,), name='cebian')

di_edge1 = p.edges.findAt(((1, 0, 0), ))
p.Set(edges=(di_edge1,), name='dibian')

ding_edge1 = p.edges.findAt(((1, 40, 0), ))
p.Surface(side1Edges=(ding_edge1,), name='dingbian')

zhu_edge1 = p.edges.findAt(((80, 23, 0), ))
p.Set(edges=(zhu_edge1,), name='zhu_edge')

p = mdb.models['Model-1'].parts['model']
region = p.sets['baiyunyan_di']
p = mdb.models['Model-1'].parts['model']
p.SectionAssignment(region=region, sectionName='baiyunyan_di', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

p = mdb.models['Model-1'].parts['model']
region = p.sets['baiyunyan_ding']
p = mdb.models['Model-1'].parts['model']
p.SectionAssignment(region=region, sectionName='baiyunyan_ding', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

p = mdb.models['Model-1'].parts['model']
region = p.sets['lvtuyan']
p = mdb.models['Model-1'].parts['model']
p.SectionAssignment(region=region, sectionName='lvtuyan', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

p = mdb.models['Model-1'].parts['model']
region = p.sets['niantuyan']
p = mdb.models['Model-1'].parts['model']
p.SectionAssignment(region=region, sectionName='niantuyan', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
#zhuangpei
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['model']
a.Instance(name='model-1', part=p, dependent=ON)
#fenxibu
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].GeostaticStep(name='diyingli', previous='Initial',
    timeIncrementationMethod=AUTOMATIC, initialInc=0.02, minInc=1e-05,
    maxInc=1.0, utol=1e-05)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='diyingli')
mdb.models['Model-1'].StaticStep(name='kaiwa', previous='diyingli',
    initialInc=0.1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='kaiwa')
#xianghuzuoyohng
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
    constraints=ON, connectors=ON, engineeringFeatures=ON,
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region =a.instances['model-1'].sets['kaiwa']
mdb.models['Model-1'].ModelChange(name='kaiwa', createStepName='kaiwa',
    region=region, activeInStep=False, includeStrain=False)
#: The interaction "Int-1" has been created.
#load
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
    predefinedFields=ON, interactions=OFF, constraints=OFF,
    engineeringFeatures=OFF)
mdb.models['Model-1'].Gravity(name='zhongli', createStepName='diyingli',
    comp2=-9.8, distributionType=UNIFORM, field='')
mdb.models['Model-1'].SmoothStepAmplitude(name='smooth', timeSpan=STEP, data=((
    0.0, 0.0), (1.0, 1.0)))
a2 = mdb.models['Model-1'].rootAssembly
region = a2.instances['model-1'].surfaces['dingbian']
mdb.models['Model-1'].Pressure(name='shangfuzaihe', createStepName='diyingli',
    region=region, distributionType=UNIFORM, field='', magnitude=4570000.0,
    amplitude='smooth')
a3 = mdb.models['Model-1'].rootAssembly
region = a3.instances['model-1'].sets['cebian']
mdb.models['Model-1'].DisplacementBC(name='ce', createStepName='Initial',
    region=region, u1=SET, u2=UNSET, ur3=UNSET, amplitude=UNSET,
    distributionType=UNIFORM, fieldName='', localCsys=None)
a3 = mdb.models['Model-1'].rootAssembly
region = a3.instances['model-1'].sets['dibian']
mdb.models['Model-1'].DisplacementBC(name='di', createStepName='Initial',
    region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET,
    distributionType=UNIFORM, fieldName='', localCsys=None)
#mesh
p = mdb.models['Model-1'].parts['model']
p.seedPart(size=0.4, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['model']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD,
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT,
    distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['model']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#ff ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
    predefinedFields=OFF, connectors=OFF)

mdb.Job(name='diyingli', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1,
    multiprocessingMode=DEFAULT, numCpus=10, numDomains=10, numGPUs=4)

mdb.jobs['diyingli'].submit(consistencyChecking=OFF)
