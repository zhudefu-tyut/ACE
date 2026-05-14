# 数据后处理与总荷载计算

读取 CSV 文件：S_ALL_withCoords_ZHU_EDGE.csv

// 1. 数据筛选
筛选符合以下条件的行：在矿柱内部且靠近矿柱顶部边界

保存筛选结果到新文件：S_ALL_withCoords_ZHU_EDGE_filtered_S22_neg.csv

// 2. 数据排序
重新读取筛选后的文件
按 X 坐标从小到大排序

// 3. 提取数据
x = X 坐标数组
y = S22 应力数组

去除包含 NaN 的数据

// 4. 读取参数
从 bianliang.txt 文件读取 spacing_zhu 的值

// 5. 计算总荷载
如果有效数据点少于 2 个：
    total_load = 0.0
否则：
    计算相邻 X 坐标的中点
    在首尾分别添加 -spacing_zhu/2 和 +spacing_zhu/2
    对所有位置点进行排序
    计算每段区间的长度 lengths
    计算每段荷载 = S22 × 长度
    total_load = 所有区段荷载之和

打印 total_load 值

// 6. 输出结果
将 total_load 保留两位小数
写入文件：total_load.txt
