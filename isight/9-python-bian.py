# Abaqus INP 文件后处理 - 创建顶底 Surface

读取 information1.inp 文件

// 1. 提取 dingbian 和 dibian 节点集合
使用正则表达式查找 *NSET, NSET=dingbian 对应的节点编号列表 → initial_tags_ding
使用正则表达式查找 *NSET, NSET=dibian 对应的节点编号列表 → initial_tags_di

// 2. 解析 gai.inp 文件，获取顶底边界节点坐标
初始化节点集合 tags_ding 和 tags_di
初始化坐标列表 coord_ding 和 coord_di

遍历 gai.inp 文件：
    进入 *NODE 段时：
        读取节点编号、X、Y 坐标
        匹配属于 dingbian 或 dibian 的节点，记录坐标
        建立完整节点编号集合（考虑坐标匹配）

    进入 *ELEMENT, TYPE=CPS3 段时：
        读取每个三角形单元的三个节点编号
        若单元有两个或以上节点属于 dingbian → 记录到 list1、list2、list3
        若单元有两个或以上节点属于 dibian → 记录到 list4、list5、list6

// 3. 修改 gai.inp 文件，插入 Surface 定义
读取 gai.inp 的所有行
查找 *END PART 的位置

准备要插入的内容：
    定义顶面 Surface (Surf-ding)：
        _Surf-q_S1（S1面）、_Surf-q_S2（S2面）、_Surf-q_S3（S3面）
    定义底面 Surface (Surf-di)：
        _Surf-q_S4（S1面）、_Surf-q_S5（S2面）、_Surf-q_S6（S3面）

将插入块内容写在 *END PART 之前

// 4. 保存修改后的文件
将处理后的内容写回 gai.inp
