# -*- coding: UTF-8 -*-

import random

with open('bh.csv', 'r+') as csv_file:
    lines = csv_file.readlines()  # readlines() 截出的每个列表后都会跟换行符

n = len(lines)
luck = [''] * n
for i in range(n):
    luck[i] = lines[i][:-1]  # 删去最后一个字符

m = int(input('请输入要抽取的车牌数: '))

count = 0
choosed = [False] * n

while count < m:
    k = random.randint(0, n - 1)
    if choosed[k]:  # 说明被抽中的车牌已经被抽过
        continue
    count += 1
    choosed[k] = True
    print(luck[k])
