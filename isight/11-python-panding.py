from odbAccess import openOdb
from abaqusConstants import *
import math
import sys

odb = openOdb(path=r'Job-1.odb', readOnly=True)

try:
    with open('total_load.txt', 'r') as f:
        load_str = f.read().strip()
    load = float(load_str)
except ValueError:
    #print("Error: total_load.txt does not contain a valid float.")
    sys.exit(1)
except FileNotFoundError:
    #print("Error: total_load.txt not found.")
    sys.exit(1)

step_names = list(odb.steps.keys())
if not step_names:
    #print("Error: No steps found in ODB.")
    sys.exit(1)
step = odb.steps[step_names[-1]]

frames = step.frames
positive_forces = []
frame_indices = []

for frame_idx, frame in enumerate(frames):
    if 'RF' not in frame.fieldOutputs:
        continue
    rf_field = frame.fieldOutputs['RF']
    node_set = odb.rootAssembly.nodeSets['CANKAODIAN']
    subset = rf_field.getSubset(region=node_set)

    if not subset.values:
        continue

    value = subset.values[0]
    rf_components = value.data
    main_rf = min(rf_components)
    if main_rf >= 0:
         continue
        #print(f"Warning: RF data in frame {frame_idx} is not negative as expected.")
    positive_force = -main_rf

    positive_forces.append(positive_force)
    frame_indices.append(frame_idx)

if len(positive_forces) < 2:
    #print("Error: Not enough frames with RF data.")
    sys.exit(1)

diffs = [positive_forces[i + 1] - positive_forces[i] for i in range(len(positive_forces) - 1)]

max_drop = 0
peak_index = -1
i = 0
n = len(diffs)

while i < n:
    if diffs[i] < 0:
        current_drop = 0
        start = i
        while i < n and diffs[i] < 0:
            current_drop -= diffs[i]
            i += 1
        # 检查是否是最大下降
        if current_drop > max_drop:
            max_drop = current_drop
            peak_index = start
    else:
        i += 1

if peak_index == -1:
    #print("Error: No decreasing segments found.")
    sys.exit(1)

peak_frame_idx = frame_indices[peak_index]
peak_force = positive_forces[peak_index]

#print(f"The point before the big decrease is at frame: {peak_frame_idx}")
#print(f"The force value at that point: {peak_force}")

with open('bianliang.txt', encoding='utf-8') as f:
    canshu = float(f.read().replace(' ', '').split('=')[1])
A = peak_force
B = load * 1.2
if A < B:
    result = 20-canshu
    #print("矿柱强度不够")
elif A > B:
    result = canshu
    ##print("矿柱强度达标")
else:
    result = canshu

##print(f"Result: {result}")

with open('result.txt', 'w') as f:
    f.write(f"{result:.2f}")

odb.close()