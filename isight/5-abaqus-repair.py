# Abaqus 导入切割模型并执行插件

初始化 Abaqus 环境
创建新的模型数据库 Model-1
设置并最大化视口

// 1. 导入几何模型
打开 STEP 文件：model-cut.stp
基于几何文件创建二维可变形部件：
    部件名称 = 'model-cut'
    合并实体区域

设置当前显示对象为 'model-cut' 部件

// 2. 执行外部插件
运行外部 Python 脚本：
    execfile('abaqus_small_face_plugin.py')
