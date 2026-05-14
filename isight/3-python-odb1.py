# Abaqus ODB 后处理

打开 ODB 文件：diyingli.odb（只读模式）

获取最后一个分析步（step）和其最后一帧（frame）
获取倒数第二个分析步（step2）和其最后一帧（frame2）

获取部件实例 'MODEL-1'
获取集合 柱边单元集合

// 1. 计算原岩应力（地应力平衡阶段）
stressField2 = 从 frame2 提取应力场 S
提取 ZHU_EDGE 集合在单元质心位置的应力子集
遍历所有单元，提取 S22 分量
计算平均 S22 值
yuanyanyingli = - (平均 S22)
将 yuanyanyingli 写入文件 yuanyanyingli.txt

// 2. 提取开挖后积分点应力及坐标
stressField = 从最终 frame 提取应力场 S
提取 ZHU_EDGE 集合在积分点位置的应力子集

// 定义 CPE4 单元积分点坐标计算函数
定义函数 ipCoord_cpe4（elem, frame, instance, uCache, intPt）：
    获取单元节点连接性
    读取各节点原始坐标 + 位移，得到变形后坐标
    使用高斯积分点形状函数（ξ, η）计算当前积分点全局坐标 (ipX, ipY)
    返回积分点坐标

// 缓存位移场
uField = 从最终 frame 提取位移场 U
建立节点标签 → 位移 的缓存字典 uCache

// 3. 输出结果到 CSV 文件
创建文件 S_ALL_withCoords_ZHU_EDGE.csv
写入表头：Element,IntPt,S22,X,Y

遍历 ZHU_EDGE 中所有积分点的应力值：
    获取对应单元和积分点编号
    调用 ipCoord_cpe4 计算积分点坐标
    写入一行数据：
        单元编号, 积分点编号, -S22, ipX, ipY

关闭 ODB 文件
