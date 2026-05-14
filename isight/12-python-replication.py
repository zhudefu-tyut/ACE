# 文件批量备份与归档管理伪代码

定义常量：
    SRC_DIR =           // 源文件夹
    DST_ROOT =          // 目标根目录
    CONFIG_FILE =       // 参数配置文件
    PARAM_NAME =        // 要提取的参数名称
    COUNTER_FILE =      // 批次计数器文件

// 1. 从文件中提取参数值
定义函数 extract_param_from_py(file_path, param_name)：
    使用正则表达式搜索 设计变量（支持整数、浮点数、字符串）
    返回提取到的参数值

// 2. 获取下一个批次编号
定义函数 get_next_batch_id()：
    如果 COUNTER_FILE 存在：
        读取当前计数
    否则：
        初始计数为 0
    计数 + 1 并写回 COUNTER_FILE
    返回当前批次编号

// 3. 执行复制操作
定义函数 copy_files()：
    读取 SRC_DIR 中的 bianliang.txt
    提取设计变量的值 → param

    获取下一个批次编号 batch_id
    创建目标文件夹：DST_ROOT/batch{batch_id}_{param}

    复制 SRC_DIR 下所有文件到目标文件夹

    打印完成信息（目标路径）

    // 清理临时结果文件
    删除 SRC_DIR 中所有以 diyingli 或 Job-1 开头的文件

// 4. 主程序入口
如果作为主程序运行：
    执行 copy_files() 函数
