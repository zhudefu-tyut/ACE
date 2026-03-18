from abaqus import *
from abaqusConstants import *
import sys

MODEL_NAME   = 'Model-1'
PART_NAME    = 'model-cut'
AREA_THRESH  = 0.001
EDGE_THRESH  = 0.01
FACE_SET_NAME = 'SmallAreaFacesSet'
EDGE_SET_NAME = 'SmallEdgesSet'

try:
    part = mdb.models[MODEL_NAME].parts[PART_NAME]
except KeyError:
    print(f"Error: Model '{MODEL_NAME}' or Part '{PART_NAME}' not found")
    #sys.exit(1)

#edge0.01

points_on_edges = []
for e in part.edges:
    try:
        if e.getSize() < EDGE_THRESH:
            points_on_edges.append(e.pointOn)
    except:
        print(f"Warning: Unable to compute size for edge {e.index}")

edges_to_add = [part.edges.findAt(p) for p in points_on_edges]

if EDGE_SET_NAME in part.sets.keys():
    del part.sets[EDGE_SET_NAME]

if edges_to_add:
    smallEdgesSet = part.Set(edges=edges_to_add, name=EDGE_SET_NAME)
    print(f'Success: {len(edges_to_add)} edges added to "{EDGE_SET_NAME}"')
else:
    print('No edges below length threshold – edge set not created.')
    #sys.exit(1)

if 'smallEdgesSet' in locals() and smallEdgesSet:
    try:
        edgeList = smallEdgesSet.edges
        part.RepairSmallEdges(
            edgeList=edgeList,
            toleranceChecks=False
        )
        print(f"Repaired {len(edgeList)} small edges successfully")
    except Exception as e:
        print(f"Edge repair failed: {str(e)}")
        #sys.exit(1)

#edge0.02

points_on_edges = []
for e in part.edges:
    try:
        if e.getSize() < EDGE_THRESH*2:
            points_on_edges.append(e.pointOn)
    except:
        print(f"Warning: Unable to compute size for edge {e.index}")

edges_to_add = [part.edges.findAt(p) for p in points_on_edges]

if EDGE_SET_NAME in part.sets.keys():
    del part.sets[EDGE_SET_NAME]

if edges_to_add:
    smallEdgesSet = part.Set(edges=edges_to_add, name=EDGE_SET_NAME)
    print(f'Success: {len(edges_to_add)} edges added to "{EDGE_SET_NAME}"')
else:
    print('No edges below length threshold – edge set not created.')
    #sys.exit(1)

if 'smallEdgesSet' in locals() and smallEdgesSet:
    try:
        edgeList = smallEdgesSet.edges
        part.RepairSmallEdges(
            edgeList=edgeList,
            toleranceChecks=False
        )
        print(f"Repaired {len(edgeList)} small edges successfully")
    except Exception as e:
        print(f"Edge repair failed: {str(e)}")
        #sys.exit(1)

#edge0.03

points_on_edges = []
for e in part.edges:
    try:
        if e.getSize() < EDGE_THRESH*3:
            points_on_edges.append(e.pointOn)
    except:
        print(f"Warning: Unable to compute size for edge {e.index}")

edges_to_add = [part.edges.findAt(p) for p in points_on_edges]

if EDGE_SET_NAME in part.sets.keys():
    del part.sets[EDGE_SET_NAME]

if edges_to_add:
    smallEdgesSet = part.Set(edges=edges_to_add, name=EDGE_SET_NAME)
    print(f'Success: {len(edges_to_add)} edges added to "{EDGE_SET_NAME}"')
else:
    print('No edges below length threshold – edge set not created.')
    #sys.exit(1)

if 'smallEdgesSet' in locals() and smallEdgesSet:
    try:
        edgeList = smallEdgesSet.edges
        part.RepairSmallEdges(
            edgeList=edgeList,
            toleranceChecks=False
        )
        print(f"Repaired {len(edgeList)} small edges successfully")
    except Exception as e:
        print(f"Edge repair failed: {str(e)}")
        #sys.exit(1)

#face0.001

centroids = []
for f in part.faces:
    if f.getSize() < AREA_THRESH:
        centroids.append(f.getCentroid())

faces_to_add = [part.faces.findAt(c) for c in centroids]
print(faces_to_add)
if FACE_SET_NAME in part.sets.keys():
    del part.sets[FACE_SET_NAME]

if faces_to_add:
    smallFacesSet = part.Set(faces=faces_to_add, name=FACE_SET_NAME)
    print(f'Success: {len(faces_to_add)} faces added to "{FACE_SET_NAME}"')
else:
    print('No faces below area threshold – face set not created.')
    #sys.exit(1)

if 'smallFacesSet' in locals() and smallFacesSet:
    try:
        faceList = smallFacesSet.faces
        part.RepairSmallFaces(
            faceList=faceList,
            toleranceChecks=False
        )
        print(f"Repaired {len(faceList)} small faces successfully")
    except Exception as e:
        print(f"Face repair failed: {str(e)}")
        #sys.exit(1)

#face0.002

centroids = []
for f in part.faces:
    if f.getSize() < AREA_THRESH*2:
        centroids.append(f.getCentroid())

faces_to_add = [part.faces.findAt(c) for c in centroids]
print(faces_to_add)
if FACE_SET_NAME in part.sets.keys():
    del part.sets[FACE_SET_NAME]

if faces_to_add:
    smallFacesSet = part.Set(faces=faces_to_add, name=FACE_SET_NAME)
    print(f'Success: {len(faces_to_add)} faces added to "{FACE_SET_NAME}"')
else:
    print('No faces below area threshold – face set not created.')
    #sys.exit(1)

if 'smallFacesSet' in locals() and smallFacesSet:
    try:
        faceList = smallFacesSet.faces
        part.RepairSmallFaces(
            faceList=faceList,
            toleranceChecks=False
        )
        print(f"Repaired {len(faceList)} small faces successfully")
    except Exception as e:
        print(f"Face repair failed: {str(e)}")
        #sys.exit(1)

#face0.003

centroids = []
for f in part.faces:
    if f.getSize() < AREA_THRESH*3:
        centroids.append(f.getCentroid())

faces_to_add = [part.faces.findAt(c) for c in centroids]
print(faces_to_add)
if FACE_SET_NAME in part.sets.keys():
    del part.sets[FACE_SET_NAME]

if faces_to_add:
    smallFacesSet = part.Set(faces=faces_to_add, name=FACE_SET_NAME)
    print(f'Success: {len(faces_to_add)} faces added to "{FACE_SET_NAME}"')
else:
    print('No faces below area threshold – face set not created.')
    #sys.exit(1)

if 'smallFacesSet' in locals() and smallFacesSet:
    try:
        faceList = smallFacesSet.faces
        part.RepairSmallFaces(
            faceList=faceList,
            toleranceChecks=False
        )
        print(f"Repaired {len(faceList)} small faces successfully")
    except Exception as e:
        print(f"Face repair failed: {str(e)}")
        #sys.exit(1)

#edge0.03

points_on_edges = []
for e in part.edges:
    try:
        if e.getSize() < EDGE_THRESH*3:
            points_on_edges.append(e.pointOn)
    except:
        print(f"Warning: Unable to compute size for edge {e.index}")

edges_to_add = [part.edges.findAt(p) for p in points_on_edges]

if EDGE_SET_NAME in part.sets.keys():
    del part.sets[EDGE_SET_NAME]

if edges_to_add:
    smallEdgesSet = part.Set(edges=edges_to_add, name=EDGE_SET_NAME)
    print(f'Success: {len(edges_to_add)} edges added to "{EDGE_SET_NAME}"')
else:
    print('No edges below length threshold – edge set not created.')
    #sys.exit(1)

if 'smallEdgesSet' in locals() and smallEdgesSet:
    try:
        edgeList = smallEdgesSet.edges
        part.RepairSmallEdges(
            edgeList=edgeList,
            toleranceChecks=False
        )
        print(f"Repaired {len(edgeList)} small edges successfully")
    except Exception as e:
        print(f"Edge repair failed: {str(e)}")
        #sys.exit(1)

mdb.models['Model-1'].parts['model-cut'].writeStepFile(
    'D:\\Work_Directory_new\\model-repair.stp')