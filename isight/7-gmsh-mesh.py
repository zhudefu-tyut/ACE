# Gmsh 模型修复、边界定义与网格生成

初始化 Gmsh 环境
创建名为 "model" 的新几何模型

// 1. 导入修复后的模型
合并文件：model-repair-AP214.stp
同步几何模型

// 2. 移除小面（模型修复）
设置面积阈值
查找所有面积小于阈值的面
获取这些面相关的边和点
移除小面 → 相关边 → 相关点
同步几何模型

// 3. 再次清理残留小面并裁剪模型
查找并记录剩余小面
同步几何模型
记录当前所有面（surface_id_before）
添加一个大矩形（-10,-10 到 20x20）用于裁剪
执行 Intersect（交）运算进行模型裁剪
同步几何模型

// 4. 网格尺寸设置
设置默认网格尺寸为 0.1
对所有点设置网格尺寸

// 5. 处理短边（Transfinite）
遍历所有线段
    若线段长度很小：
        设置为 TransfiniteCurve（2个节点）
        调整端点网格尺寸（略小于线段长度）

// 6. 定义 Physical Groups（边界条件用）
创建顶部边界 Physical Group  → 名称 "dingbian"
创建底部边界 Physical Group  → 名称 "dibian"

从 bianliang.txt 读取 spacing_zhu
创建左侧边界 Physical Group（x≈ -spacing_zhu/2） → 名称 "zuobian"
创建右侧边界 Physical Group（x≈ +spacing_zhu/2） → 名称 "youbian"

// 7. 网格生成与文件输出
设置网格控制选项（从边界、从点、从曲率）
生成二维网格
导出 information1.inp

// 8. 生成带所有线单元的网格文件
移除之前的边界 Physical Groups
为所有内部线段创建独立 Physical Group（line + 编号）
同步模型
再次生成网格
导出 information.inp
导出 output.inp（包含所有组）

// 9. 后处理 INP 文件
读取 output.inp
删除其中 T3D2 梁单元部分
保留 CPS3 等平面单元
保存为 model.inp

结束 Gmsh 环境
