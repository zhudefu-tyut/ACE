# Gmsh 模型切割

初始化 Gmsh 环境
创建名为 "model" 的新几何模型

// 1. 导入已有几何
合并外部文件：model-qie.stp
同步几何模型
记录当前所有面（Surface）的 ID（surface_id_before）

// 2. 读取参数
从 bianliang.txt 文件读取 long 的值（柱间距/长度）

// 3. 创建切割用基座矩形
添加矩形：
    中心位于 x=0，y=-5
    宽度 = long
    高度 = 10
    标签 = 9999

同步几何模型

// 4. 执行布尔交运算
使用已存在的面（surface_id_before）与新建矩形（标签9999）进行 Intersect（交）操作
同步几何模型

// 5. 输出结果
导出模型为 "model-cut.stp"
（可选：启动 Gmsh 图形界面显示）
结束 Gmsh 环境
