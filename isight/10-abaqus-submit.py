# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-20.55.25 RELr426 190762
# Run by gbl on Fri Dec 12 21:32:08 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=322.982269287109,
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
#daoru
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='gai',
    inputFileName='D:/Work_Directory_new/gai.inp')
#: The model "gai" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "gai" has been imported from an input file.
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['gai'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#dingdiban
p = mdb.models['gai'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['gai'].ConstrainedSketch(name='__profile__', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
with open('D:/Work_Directory_new/bianliang.txt', encoding='utf-8') as f:
    spacing_zhu = float(f.read().replace(' ', '').split('=')[1])
X_zhu = spacing_zhu/2
s.rectangle(point1=(-X_zhu, -2.8), point2=(X_zhu, -3.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.00353,
    farPlane=10.8527, width=15.3035, height=6.70286, cameraPosition=(1.71086,
    -1.2657, 9.42809), cameraTarget=(1.71086, -1.2657, 0))
p = mdb.models['gai'].Part(name='Part-2', dimensionality=TWO_D_PLANAR,
    type=DISCRETE_RIGID_SURFACE)
p = mdb.models['gai'].parts['Part-2']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['gai'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['gai'].sketches['__profile__']
p = mdb.models['gai'].parts['Part-2']
v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=p.InterestingPoint(edge=e[2], rule=MIDDLE))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['gai'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#cailiao
#kuaiti
mdb.models['gai'].Material(name='kuaiti')
mdb.models['gai'].materials['kuaiti'].Density(table=((2782.0, ), ))
mdb.models['gai'].materials['kuaiti'].Elastic(table=((30000000000.0, 0.25), ))
mdb.models['gai'].HomogeneousSolidSection(name='kuaiti', material='kuaiti',
    thickness=None)
p = mdb.models['gai'].parts['PART-1']
region = p.sets['SET-SPECIMEN']
p = mdb.models['gai'].parts['PART-1']
p.SectionAssignment(region=region, sectionName='kuaiti', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
#cohesive
mdb.models['gai'].Material(name='cohesive')
mdb.models['gai'].materials['cohesive'].Density(table=((2000.0, ), ))
mdb.models['gai'].materials['cohesive'].Elastic(type=TRACTION, table=((
    1200000000.0, 400000000.0, 400000000.0), ))
mdb.models['gai'].materials['cohesive'].QuadsDamageInitiation(table=((
    4000000.0, 8000000.0, 8000000.0), ))
mdb.models['gai'].materials['cohesive'].quadsDamageInitiation.DamageEvolution(
    type=DISPLACEMENT, table=((1e-05, ), ))
mdb.models['gai'].materials['cohesive'].quadsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=1e-05)
mdb.models['gai'].CohesiveSection(name='cohesive', material='cohesive',
    response=TRACTION_SEPARATION, initialThicknessType=SPECIFY,
    initialThickness=0.001, outOfPlaneThickness=None)
p = mdb.models['gai'].parts['PART-1']
region = p.sets['SET-COHESIVE']
p = mdb.models['gai'].parts['PART-1']
p.SectionAssignment(region=region, sectionName='cohesive', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
#assembly
a = mdb.models['gai'].rootAssembly
a.regenerate()
a = mdb.models['gai'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['gai'].rootAssembly
del a.features['PART-1-1']
a1 = mdb.models['gai'].rootAssembly
p = mdb.models['gai'].parts['PART-1']
a1.Instance(name='PART-1-1', part=p, dependent=ON)
p = mdb.models['gai'].parts['Part-2']
a1.Instance(name='Part-2-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.3369,
    farPlane=18.0433, width=16.365, height=7.16779, viewOffsetX=0.934226,
    viewOffsetY=-0.301234)
a1 = mdb.models['gai'].rootAssembly
a1.LinearInstancePattern(instanceList=('Part-2-1', ), direction1=(1.0, 0.0,
    0.0), direction2=(0.0, 1.0, 0.0), number1=1, number2=2, spacing1=6.0,
    spacing2=5.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.2552,
    farPlane=18.125, width=15.4986, height=6.78833, viewOffsetX=1.0848,
    viewOffsetY=0.60529)
a = mdb.models['gai'].rootAssembly
s1 = a.instances['Part-2-1-lin-1-2'].edges
side2Edges1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side2Edges=side2Edges1, name='Surf-1')
#: The surface 'Surf-1' has been created (1 edge).
mdb.models['gai'].rootAssembly.surfaces.changeKey(fromName='Surf-1',
    toName='ding-di')
a = mdb.models['gai'].rootAssembly
s1 = a.instances['Part-2-1'].edges
side2Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Surface(side2Edges=side2Edges1, name='di-ding')
#: The surface 'di-ding' has been created (1 edge).
# step
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['gai'].ExplicitDynamicsStep(name='Step-1', previous='Initial',
    timePeriod=3.0, massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 30.0,
    0.0, None, 0, 0, 0.0, 0.0, 0, None), ), improvedDtMethod=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['gai'].fieldOutputRequests['F-Output-1'].setValues(variables=('S',
    'SVAVG', 'PE', 'PEVAVG', 'PEEQ', 'PEEQVAVG', 'LE', 'U', 'V', 'A', 'RF',
    'CSTRESS', 'SDEG', 'EVF', 'STATUS'), numIntervals=120)
# interaction
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
    constraints=ON, connectors=ON, engineeringFeatures=ON,
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1568,
    farPlane=18.2234, width=16.3816, height=7.17505, viewOffsetX=1.2399,
    viewOffsetY=0.388795)
a = mdb.models['gai'].rootAssembly
e1 = a.instances['Part-2-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
region2=a.Set(edges=edges1, name='b_Set-1')
a = mdb.models['gai'].rootAssembly
r1 = a.instances['Part-2-1'].referencePoints
refPoints1=(r1[2], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['gai'].RigidBody(name='Constraint-1', refPointRegion=region1,
    bodyRegion=region2)
a = mdb.models['gai'].rootAssembly
r1 = a.instances['Part-2-1-lin-1-2'].referencePoints
refPoints1=(r1[2], )
a.Set(referencePoints=refPoints1, name='cankaodian')
#: The set 'cankaodian' has been created (1 reference point).
a = mdb.models['gai'].rootAssembly
e1 = a.instances['Part-2-1-lin-1-2'].edges
edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
region2=a.Set(edges=edges1, name='b_Set-4')
a = mdb.models['gai'].rootAssembly
r1 = a.instances['Part-2-1-lin-1-2'].referencePoints
refPoints1=(r1[2], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['gai'].RigidBody(name='Constraint-2', refPointRegion=region1,
    bodyRegion=region2)
a = mdb.models['gai'].rootAssembly
region1=a.instances['PART-1-1'].surfaces['SURF-DI']
a = mdb.models['gai'].rootAssembly
region2=a.surfaces['di-ding']
mdb.models['gai'].Tie(name='Constraint-3', main=region1, secondary=region2,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
a = mdb.models['gai'].rootAssembly
region1=a.instances['PART-1-1'].surfaces['SURF-DING']
a = mdb.models['gai'].rootAssembly
region2=a.surfaces['ding-di']
mdb.models['gai'].Tie(name='Constraint-4', main=region2, secondary=region1,
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
mdb.models['gai'].ContactExp(name='Int-1', createStepName='Step-1')
mdb.models['gai'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Step-1', useAllstar=ON)
mdb.models['gai'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Step-1', assignments=((GLOBAL, SELF, ''), ))
#: The interaction "Int-1" has been created.
# load
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
    predefinedFields=ON, interactions=OFF, constraints=OFF,
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['gai'].rootAssembly
r1 = a.instances['Part-2-1'].referencePoints
refPoints1=(r1[2], )
region = a.Set(referencePoints=refPoints1, name='Set-6')
mdb.models['gai'].DisplacementBC(name='BC-1', createStepName='Initial',
    region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET,
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['gai'].rootAssembly
region = a.sets['cankaodian']
mdb.models['gai'].DisplacementBC(name='BC-2', createStepName='Initial',
    region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET,
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['gai'].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((0.0,
    0.0), (3.0, 1.0)))
mdb.models['gai'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-1',
    u2=-0.003, amplitude='Amp-1')
#mesh
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF,
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['gai'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)

elemType1 = mesh.ElemType(elemCode=COH2D4, elemLibrary=EXPLICIT,
    elemDeletion=ON)
p = mdb.models['gai'].parts['PART-1']
region = p.sets['SET-COHESIVE']
p.setElementType(regions=region, elemTypes=(elemType1, ))

elemType1 = mesh.ElemType(elemCode=CPE3, elemLibrary=EXPLICIT,
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['gai'].parts['PART-1']
region = p.sets['SET-SPECIMEN']
p.setElementType(regions=region, elemTypes=(elemType1, ))
p = mdb.models['gai'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['gai'].parts['Part-2']
p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['gai'].parts['Part-2']
p.generateMesh()
#job
a1 = mdb.models['gai'].rootAssembly
a1.regenerate()
a = mdb.models['gai'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-1', model='gai', description='', type=ANALYSIS, atTime=None,
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, numDomains=10, activateLoadBalancing=False,
    numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, numCpus=10)

mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
