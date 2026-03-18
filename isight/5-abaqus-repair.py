# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-20.55.25 RELr426 190762
# Run by gbl on Thu Sep 25 16:46:42 2025
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
step = mdb.openStep('"D:\Work_Directory_new\model-cut.stp"', scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(name='model-cut', geometryFile=step,
    combine=True, mergeSolidRegions=True, dimensionality=TWO_D_PLANAR,
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['model-cut']
session.viewports['Viewport: 1'].setValues(displayedObject=p)

execfile('D:/Work_Directory_new/abaqus_small_face_plugin.py', __main__.__dict__)

