from odbAccess import openOdb
from abaqusConstants import *

import math

odb = openOdb(path=r'D:/Work_Directory_new/diyingli.odb', readOnly=True)

step = odb.steps.values()[-1]
frame = step.frames[-1]

step2 = odb.steps.values()[-2]
frame2 = step2.frames[-1]

instance = odb.rootAssembly.instances['MODEL-1']
instElSet = instance.elementSets['ZHU_EDGE']

stressField2 = frame2.fieldOutputs['S']
stressSubset2 = stressField2.getSubset(region=instElSet,
                                       position=CENTROID)
s22_list = []
for v in stressSubset2.values:
    s22 = v.data[1]
    s22_list.append(s22)

yuanyanyingli = (-1) * sum(s22_list) / len(s22_list)
with open('yuanyanyingli.txt', 'w', encoding='utf-8') as f:
    f.write(str(yuanyanyingli))
stressField = frame.fieldOutputs['S']
stressSubset = stressField.getSubset(region=instElSet,
                                     position=INTEGRATION_POINT)

def ipCoord_cpe4(elem, frame, instance, uCache, intPt):
    conn = elem.connectivity
    X = [0.0] * 4
    Y = [0.0] * 4
    for i, lab in enumerate(conn):
        n = instance.getNodeFromLabel(lab)
        ux, uy = uCache[lab]
        X[i] = n.coordinates[0] + ux
        Y[i] = n.coordinates[1] + uy

    gauss_pts = [
        (-1 / math.sqrt(3), -1 / math.sqrt(3)),
        (1 / math.sqrt(3), -1 / math.sqrt(3)),
        (1 / math.sqrt(3), 1 / math.sqrt(3)),
        (-1 / math.sqrt(3), 1 / math.sqrt(3))
    ]
    if intPt < 1 or intPt > 4:
        raise ValueError("1~4")
    xi, eta = gauss_pts[intPt - 1]

    N1 = (1 - xi) * (1 - eta) / 4.0
    N2 = (1 + xi) * (1 - eta) / 4.0
    N3 = (1 + xi) * (1 + eta) / 4.0
    N4 = (1 - xi) * (1 + eta) / 4.0

    ipX = N1 * X[0] + N2 * X[1] + N3 * X[2] + N4 * X[3]
    ipY = N1 * Y[0] + N2 * Y[1] + N3 * Y[2] + N4 * Y[3]

    return (ipX, ipY, 0.0)


uField = frame.fieldOutputs['U']
uCache = {v.nodeLabel: v.data for v in uField.values}

csvName = 'S_ALL_withCoords_ZHU_EDGE.csv'
with open(csvName, 'w') as f:
    f.write('Element,IntPt,S22,X,Y\n')
    for v in stressSubset.values:
        elem = instance.elements[v.elementLabel - 1]
        ipX, ipY, ipZ = ipCoord_cpe4(elem, frame, instance, uCache, v.integrationPoint)
        f.write('{0},{1},{3},{6},{7}\n'.format(
            v.elementLabel,
            v.integrationPoint,
            *v.data * (-1),
            ipX - 80, ipY))

odb.close()