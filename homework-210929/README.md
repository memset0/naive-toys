# 2021.9.29 · 车牌随机抽取

实现程序，从给定车牌列表中（存储到 csv 文件中）抽取 m 个车牌，m 由用户输入。

### random 库常用函数

| 函数 | 方法 |
| :-: | :-: |
| `random.randint(a, b)` | 从 [a, b] 中选择随机一个整数 |
| `random.choice(arr[])` | 从列表 arr 中随机选择一个元素<br>*arr 可以为任意 iterable objects，下同理 |
| `random.randrange(a, b, c)` | 从 range(a, b, c) 中随机选择一个整数<br>等价于 `random.choice(range(a, b, c))`<br>*并不会真的生成 range |
| `random.shuffle(arr[])` | 讲给定列表 arr 打乱顺序<br>直接在 arr 上做修改，该函数并没有返回值 |
| `random.sample(arr[], k)` | 给定列表 arr 中选择不同的 k 个元素并返回 <br>等价于 `random.shuffle(arr); return arr[:k]`<br>元素不同是指下标不同 |

### 标准做法 (`sol_1.py`)

```python
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
```

### 稍微聪明一点的做法 (`sol_2.py`)

```python
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
```

测试

```python
# -*- coding: UTF-8 -*-

from random import randrange

with open('bh.csv', 'r+') as csv_file:
    luck = csv_file.read().splitlines()

n = len(luck)
m = int(input('请输入要抽取的车牌数: '))

while m:                 # why?
    k = randrange(0, n)
    if luck[k] != 42:    # why?
        print(luck[k])
        luck[k] = 42
        m -= 1
```

### 家长还有两分钟就来收电脑的做法 (`sol_3.py`)

```python
print('\n'.join(__import__('random').sample(open('bh.csv', 'r+').read().splitlines(), int(input('m = ')))))
```

<footer class="print-footer">@memset0</footer>
<link rel="stylesheet" href="../markdown-printed.css">