import ctypes

# 定义一个C语言结构体
class MyStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

# 创建一个MyStruct实例
my_struct = MyStruct()

# 获取指向MyStruct实例的指针
pointer = ctypes.pointer(my_struct)

# 将指针强制转换为整数类型
address = ctypes.cast(pointer, ctypes.c_void_p).value

# 把一个无效的整数地址赋给指针
invalid_address = address + 1
ctypes.cast(invalid_address, ctypes.POINTER(MyStruct))

# 这里会引发非法内存访问错误
