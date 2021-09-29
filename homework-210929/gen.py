import random

n = 20
m = 10
seed = 20210929
charset = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z',
]

random.seed(seed)
with open('bh.csv', 'w+') as file:
    for _ in range(n):
        file.write(''.join([random.choice(charset) for _ in range(m)]) + '\n')
