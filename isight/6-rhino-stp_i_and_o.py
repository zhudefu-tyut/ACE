# RhinoInside STP格式转换（AP214）

导入必要模块：
    os, sys, pathlib
    rhinoinside
    Rhino 相关模块（Rhino, FileStpWriteOptions）

// 1. 配置 Rhino 8 运行环境
设置 Rhino 8 系统路径
将 Rhino 路径加入 sys.path
更新系统环境变量 PATH
加载 rhinoinside

// 2. 定义输入输出文件路径
STP_IN  = model-repair.stp
STP_OUT = model-repair-AP214.stp

// 3. 定义转换函数
定义函数 stp_214(源文件, 目标文件)：
    创建无界面（Headless）Rhino 文档
    尝试：
        导入源 STP 文件
        若导入失败则报错

        创建 STP 输出选项
        设置输出格式为 Scheme = 214（AP214）

        将文档写入目标 STP 文件（AP214格式）
        若写入失败则报错
        打印完成信息
    最终：
        释放 Rhino 文档资源

// 4. 执行主程序
如果作为主程序运行：
    调用 stp_214 函数进行格式转换
