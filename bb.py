import ctypes


# 定义一个C语言结构体
class MyStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int * 5)]


# 创建一个MyStruct实例
my_struct = MyStruct()

# 获取指向MyStruct实例的指针
pointer = ctypes.pointer(my_struct)

# 将指针强制转换为整数类型
address = ctypes.cast(pointer, ctypes.c_void_p).value

# 把一个无效的整数地址赋给指针
invalid_address = address + 100
ctypes.cast(invalid_address, ctypes.POINTER(MyStruct))


for v in range(100000):
    address = ctypes.cast(pointer, ctypes.c_void_p).value

    invalid_pointer = address + (v + 1)
    invalid_pointer = ctypes.cast(invalid_address, ctypes.POINTER(MyStruct))

    # 在无效指针上尝试写入数据
    for i in range(10):
        invalid_pointer.contents.x[i] = 123
    print(invalid_pointer.contents.x)
# 这里会引发非法内存访问错误
print("ddddddd")
