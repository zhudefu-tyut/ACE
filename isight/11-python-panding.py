# Abaqus ODB 后处理 - 峰值力提取与强度判断伪代码

打开 ODB 文件：Job-1.odb（只读模式）

// 1. 读取参考荷载
从 total_load.txt 读取 total_load 值（若读取失败则退出）

// 2. 提取参考点反力
获取最后一个分析步
遍历该步的所有帧（frames）：
    提取场输出 RF（Reaction Force）
    获取节点集合 CANKAODIAN 的反力数据
    取反力中的最小分量（主方向力）
    转换为正值 positive_force = -RF
    记录每个有效帧的正向力值和帧序号

// 3. 寻找峰值力（最大下降前的力值）
计算相邻帧之间的力差值 diffs
遍历 diffs，找出下降段（连续负差值）中下降量最大的段落
记录该下降段起始位置对应的峰值力 peak_force 和峰值帧序号

// 4. 强度判断与结果计算
从 bianliang.txt 读取参数 canshu

A = peak_force          // 实际峰值承载力
B = total_load * 1.2    // 设计要求阈值

如果 A < B：
    result = 20 - canshu     // 强度不够
否则：
    result = canshu          // 强度达标

// 5. 输出结果
将 result 保留两位小数
写入文件 result.txt

关闭 ODB 文件
