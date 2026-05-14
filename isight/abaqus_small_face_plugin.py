# Abaqus 模型几何修复脚本伪代码（小边 + 小面修复）

定义参数：
    MODEL_NAME   = 'Model-1'
    PART_NAME    = 'model-cut'
    AREA_THRESH  = 0.001     // 面积阈值（小面）
    EDGE_THRESH  = 0.01      // 长度阈值（小边）
    FACE_SET_NAME = 'SmallAreaFacesSet'
    EDGE_SET_NAME = 'SmallEdgesSet'

获取部件：
    part = Model-1 中的部件 'model-cut'

// ==================== 小边修复 ====================

// 小边修复 - 阈值 0.01
查找所有长度 < 0.01 的边
创建集合 'SmallEdgesSet'
执行 RepairSmallEdges 修复

// 小边修复 - 阈值 0.02
查找所有长度 < 0.02 的边
创建集合 'SmallEdgesSet'
执行 RepairSmallEdges 修复

// 小边修复 - 阈值 0.03（执行两次）
查找所有长度 < 0.03 的边
创建集合 'SmallEdgesSet'
执行 RepairSmallEdges 修复

// ==================== 小面修复 ====================

// 小面修复 - 阈值 0.001
查找所有面积 < 0.001 的面
创建集合 'SmallAreaFacesSet'
执行 RepairSmallFaces 修复

// 小面修复 - 阈值 0.002
查找所有面积 < 0.002 的面
创建集合 'SmallAreaFacesSet'
执行 RepairSmallFaces 修复

// 小面修复 - 阈值 0.003
查找所有面积 < 0.003 的面
创建集合 'SmallAreaFacesSet'
执行 RepairSmallFaces 修复

// ==================== 最终导出 ====================

将修复后的部件 'model-cut' 导出为：model-repair.stp
