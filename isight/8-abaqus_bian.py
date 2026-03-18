# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-20.55.25 RELr426 190762
# Run by gbl on Thu Nov 27 11:01:56 2025
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
mdb.models['Model-1'].PartFromInputFile(
    inputFileName='D:/Work_Directory_new/model.inp')
#: Warning: Undefined node and element ids have been removed from some node and element sets
#: The part "PART-1" has been imported from the input file.
#:
#: Parts have been imported in "Model-1" from an input file.
#: Please scroll up to check for error and warning messages.
#:
execfile('D:/Work_Directory_new/cohesive_element_creat.py', __main__.__dict__)

p = mdb.models['Model-1'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['PART-1']
e = p.elements
if 'Set-cohesive' not in p.sets.keys():
    raise ValueError('PART-1 cant find Set-cohesive!')
cohesive_set = p.sets['Set-cohesive']
cohesive_label = set(elem.label for elem in cohesive_set.elements)
remain_elem = [elem for elem in e if elem.label not in cohesive_label]
elemSeq = p.elements.sequenceFromLabels([elem.label for elem in remain_elem])
p.Set(elements=elemSeq, name='Set-specimen')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['PART-1']
a.Instance(name='PART-1-1', part=p, dependent=ON)
mdb.Job(name='gai', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, numDomains=1, activateLoadBalancing=False,
    numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, numCpus=1,
    numGPUs=0)
mdb.jobs['gai'].writeInput(consistencyChecking=OFF)