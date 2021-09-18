# AUTHOR: whisperain (https://github.com/memset0)
# DEPENDENCE: Windows 7+, Python3 (ver<3.8)

from ctypes import *
from os import path

dirname = path.split(path.realpath(__file__))[0]
array = cdll.LoadLibrary(path.join(dirname, r'c_module\arraymodule.dll'))

array.array_new.restype = POINTER(c_int)
array.array_new.argtypes = [c_size_t]

array.array_delete.argtypes = [POINTER(c_int)]

array.array_get_value.restype = c_int
array.array_get_value.argtypes = [POINTER(c_int), c_size_t]

array.array_set_value.argtypes = [POINTER(c_int), c_size_t, c_int]


class Array:
    def __getitem__(self, index):
        return array.array_get_value(self.arr_p, index)

    def __setitem__(self, index, value):
        return array.array_set_value(self.arr_p, index, value)

    def __delete__(self):
        array.array_delete(self.arr_p)
        self.arr_p = None

    def __init__(self, length):
        assert(length > 0)
        self.arr_p = array.array_new(length)


if __name__ == '__main__':
    a = Array(10)
    for i in range(10):
        a[i] = i ** 2
    for i in range(10):
        print(a[i])
