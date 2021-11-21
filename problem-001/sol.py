m = 6
a = [0] * (m * m)  # 存储矩阵状态，2代表钻石，1代表固定障碍物，0代表空格
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(m):
        a[i * m + j] = row[j]

q = [0] * m  # 存储有效空格位置
f, t, k = 0, 0, m - 1

# 先模拟钻石下落过程
for i in range(m * m):
    if a[k] == 0:
        q[t] = k
        t = t + 1
    elif a[k] == 1:
        f, t = 0, 0
    elif f != t:
        a[q[f]] = 2
        f = f + 1
        a[k] = 0
        q[t] = k
        t = t + 1
    if k % m == 0:
        f, t = 0, 0
        k += 2 * m - 1
    else:
        k -= 1

# 顺时针旋转90° 后输出
p = (m - 1) * m
s = ''
for i in range(m * m):
    s += str(a[p]) + ' '
    print(p)
    if i % m == m - 1:
        s += '\n'
        p = (m - 1) * m + i // m + 1
    else:
        p -= m
print(s)