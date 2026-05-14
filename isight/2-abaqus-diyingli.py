# Abaqus 模型建立与分析

初始化 Abaqus 环境
创建新的模型数据库 Model-1
打开视口并最大化

// 1. 导入几何模型
打开 STEP 文件：model-diceng.stp
基于几何文件创建二维可变形部件 Part = 'model'

// 2. 定义材料属性
创建材料 材料1：

创建材料 材料2：

创建材料 材料3：

创建材料 材料4：

...

创建对应的均质实体截面（HomogeneousSolidSection）

// 3. 创建几何集合（Sets）
p = 部件 'model'

通过坐标拾取创建对应材料的模型集合：

从 bianliang.txt 读取 “矿柱宽度”
设置采空区宽度

通过坐标拾取创建开挖区域地层集合
根据预先设置的开挖区域创建 kaiwa 集合

创建边界集合：
    cebian   ← 左右侧边界所有竖边
    dibian   ← 底边
    dingbian ← 顶边（Surface）

// 4. 赋予截面属性
将对应集合赋予各自的材料截面

// 5. 装配
创建装配体
将部件 'model' 实例化为 model-1

// 6. 定义分析步
创建 Geostatic 步（diyingli）- 地应力平衡步
创建 Static 步（kaiwa）- 开挖步

// 7. 定义相互作用
在 kaiwa 步中对 kaiwa 集合施加 ModelChange（移除/钝化单元）

// 8. 定义荷载与边界条件
施加重力（-9.8 m/s²）于地应力步

施加顶部均布压力于 dingbian，使用 smooth 幅值曲线

施加边界条件：
    侧边 (cebian)：水平方向固定 (u1=0)
    底边 (dibian)：完全固定 (u1=0, u2=0)

// 9. 网格划分
设置全局种子大小 ≈ 0.4
生成网格
设置单元类型：以 CPE4（四边形）为主，CPE3（三角形）为辅

// 10. 创建并提交作业
创建分析作业 diyingli（使用 10 CPU + 4 GPU）
提交作业进行计算
