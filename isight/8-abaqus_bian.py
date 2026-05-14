# Abaqus 导入 INP 文件并创建作业

初始化 Abaqus 环境
创建新的模型数据库 Model-1
设置并最大化视口

// 1. 从 INP 文件导入模型
从文件导入 Part：
    inputFileName = 'model.inp'
    导入后部件名称为 'PART-1'

// 2. 执行外部插件脚本
运行外部 Python 脚本：
    execfile('cohesive_element_creat.py')

// 3. 设置显示与集合处理
设置当前显示对象为 'PART-1' 部件
开启截面属性和工程特征显示

获取部件 'PART-1' 中的所有单元

如果存在集合 'Set-cohesive'：
    获取 cohesive 单元集合
    创建剩余单元集合 'Set-specimen'（排除所有 cohesive 单元）
否则：
    报错：未找到 Set-cohesive

// 4. 装配
进入装配模块
创建默认笛卡尔坐标系
将部件 'PART-1' 实例化为 'PART-1-1'（依赖实例）

// 5. 创建分析作业
创建作业 ：

// 6. 输出 INP 文件
将作业 'gai' 写入输入文件
