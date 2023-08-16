import resource

# 设置核心文件的大小限制（以字节为单位）
resource.setrlimit(resource.RLIMIT_CORE, (1, resource.RLIM_INFINITY))

# 生成一个除以零错误，导致崩溃并生成核心文件
x = 1 / 0

