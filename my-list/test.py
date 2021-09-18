# AUTHOR: whisperain (https://github.com/memset0)

from my_list import List

if __name__ == '__main__':
    a = List([i ** 2 for i in range(20)])
    print(a)
    print(a[1], a[-1])
    a[2] = 42
    a[-4] = -725
    print(a)
    a.append(0)
    print(a)
    print(a.pop())
    print(a.pop(10))
    a.extend([-1] * 2)
    print(a.index(-1))
    print(a.index(81))
    print(a)
    a.insert(5, 666)
    a.remove(15)
    print(a)
    a.reverse()
    print(a)
    a.reverse()
    print(a)
