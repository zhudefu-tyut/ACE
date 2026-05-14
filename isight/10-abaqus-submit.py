# Abaqus 显式动力学建模与分析（含刚性压头、Cohesive单元）

初始化 Abaqus 环境
创建新的模型数据库 Model-1
设置并最大化视口

// 1. 导入模型
从 gai.inp 文件导入模型，模型名称设为 "gai"
// 部件 PART-1 被导入

// 2. 创建刚性压头（Part-2）
进入装配模块
从 bianliang.txt 读取“矿柱宽度”，计算 X_zhu = spacing_zhu/2
创建草图：在 y=-2.8 到 -3.0 处绘制宽度为 spacing_zhu 的矩形
创建离散刚体部件 Part-2（二维平面）
基于草图生成 BaseWire
在压头中点创建 Reference Point
创建 Part-2 的线性阵列（共2个压头）

// 3. 定义材料与截面
创建材料 kuaiti（岩体）：

创建材料 cohesive（内聚力单元）：

// 4. 装配与相互作用
删除原有实例，重新实例化 PART-1 和 Part-2
创建刚体约束（RigidBody）将压头绑定到参考点
创建 Tie 约束：
    Surf-di（底面）与模型 Surf-di 绑定
    Surf-ding（顶面）与模型 Surf-ding 绑定
创建通用接触 Int-1（Explicit）

// 5. 定义分析步
创建 Explicit Dynamics 步（Step-1），时间 3.0 ，自动质量缩放
设置场输出（S, PE, U, V, A, CSTRESS, SDEG 等），输出间隔 120

// 6. 边界条件与载荷
初始步：
    固定上方压头参考点（全部自由度）
    固定下方压头参考点（全部自由度）

Step-1 中：
    对下方压头参考点施加竖向位移m（使用 SmoothStep 幅值）

// 7. 网格划分
为 SET-COHESIVE 设置 COH2D4 单元
为 SET-SPECIMEN 设置 CPE3 单元
为刚性压头 Part-2 设置种子大小 0.01 并生成网格

// 8. 创建并提交作业
创建作业 Job-1（10 CPU）
提交作业进行计算
