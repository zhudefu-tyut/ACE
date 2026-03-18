import pandas as pd
import numpy as np

input_file = 'S_ALL_withCoords_ZHU_EDGE.csv'
output_file = 'S_ALL_withCoords_ZHU_EDGE_filtered_S22_neg.csv'
df = pd.read_csv(input_file)

df = df[(df.iloc[:, 4] <= 23) & (df.iloc[:, 1].isin([2, 4]))].copy()
df.to_csv(output_file, index=False, encoding='utf-8-sig')

df = pd.read_csv(output_file)

df = df.sort_values('X').reset_index(drop=True)

x = df['X'].values
y = df['S22'].values

mask = ~np.isnan(x) & ~np.isnan(y)
x = x[mask]
y = y[mask]

n = len(y)

with open('bianliang.txt', encoding='utf-8') as f:
    spacing_zhu = float(f.read().replace(' ', '').split('=')[1])

if n < 2:
    total_load = 0.0
    print("0")
else:
    mid_x = (x[:-1] + x[1:]) / 2

    pos = np.append(np.append(-spacing_zhu / 2, mid_x), spacing_zhu / 2)
    pos = np.sort(pos)

    lengths = np.diff(pos)

    load_forces = y * lengths

    total_load = np.sum(load_forces)

print("sum", total_load)

formatted_total_load = "{:.2f}".format(total_load)

with open('total_load.txt', 'w', encoding='utf-8') as f:
    f.write(formatted_total_load)