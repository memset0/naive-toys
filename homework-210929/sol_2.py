# -*- coding: UTF-8 -*-

from random import randrange  # 还可以这样导入库函数

with open('bh.csv', 'r+') as csv_file:
    luck = csv_file.read().splitlines()
    # .readlines() 截出的每个列表后都会跟换行符
    # 改用 .read().splitlines() 则不会

n = len(luck)
m = int(input('请输入要抽取的车牌数: '))

while m:  # 每次选择 m 都会减少 1，选择 m 次后 m == 0 退出 while 循环
    k = randrange(0, n)
    if luck[k] != 42:
        # 因为 luck 列表本来存储的元素都是 str 类型
        # 我们打标记（赋值为 42）则不是 str 类型（此处为 int）
        print(luck[k])  # 这条语句必须放对 luck[k] 进行赋值的语句上面
        luck[k] = 42
        m -= 1
