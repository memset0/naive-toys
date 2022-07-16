from math import log


def fln(x):
    cln2 = 0
    ans = 0
    while True:
        while x % 2 == 0:
            cln2 += 1
            x /= 2
        if x == 1:
            break
        x -= 1
        ans += 2. / (2 * x + 1)
    ans += 0.693 * cln2
    return ans


lim = [3, 10, 100, 1000]
maxd = 0
sum = 0 
for i in range(3, lim[-1] + 1):
    a = fln(i)
    b = log(i)
    sum += abs(a - b)
    maxd = max(maxd, abs(a - b))
    # print(i, a, b)
    if i in lim:
        print(i, maxd, sum / (i - 2))
