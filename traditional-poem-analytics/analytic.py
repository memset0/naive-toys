#!/usr/bin/python
# -*- coding: UTF-8 -*-

# author: whisperain
# blog: https://memset0.cn/

# MARK: 才知道 [...] * k 的语法是浅拷贝，真是害人不浅！
# MARK: 才知道 a = b = ... 的语法也是浅拷贝，真他妈害人不浅！

from time import time
# import diojit as jit

K = 4
STOPWORDS = ['，', '。', '《', '》', '-', '□', 'z']


def readFile(path):
    with open(path, 'r+', encoding='utf-8') as file:
        text = file.read()
        file.close()
    return text

def writeFile(path, text):
    with open(path, 'w+', encoding='utf-8') as file:
        file.write(text)
        file.close()

def pretty(a, num=False):
    def prettyWord(t):
        return t[0]
    def prettyWordWithNum(t):
        return t[0] + '[' + str(t[1]) + ']'
    return ' '.join(map(prettyWordWithNum if num else prettyWord, a))


def parse(text):
    res = []
    for line in text.split('\n'):
        if line.startswith('　　') and not line.startswith('　　◎'):
            res.append(line[2:])
    print('[parse]', 'seg_size:', len(res))
    return res


# @jit.eagerjit
def analytic(segs, lim):
    cnt = []
    res = []
    for k in range(K):
        cnt.append({})
        res.append([])
    time_s = time()
    for seg in segs:
        for k in range(K):
            for i in range(0, len(seg) - k - 1):
                s = seg[i: i + k + 1]
                f = True
                for stopword in STOPWORDS:
                    if stopword in s:
                        f = False
                        break
                if f:
                    if s in cnt[k]:
                        cnt[k][s] += 1
                    else:
                        cnt[k][s] = 1
    time_e = time()
    print('[analytic]', 'time_cost_1:', time_e - time_s)
    time_s = time()
    for i in range(len(cnt)):
        for stopword in STOPWORDS:
            if stopword in cnt[i]:
                del cnt[i][stopword]
        res[i] = sorted(cnt[i].items(), key=lambda e: -e[1])[:lim]
    time_e = time()
    print('[analytic]', 'time_cost_2:', time_e - time_s)
    return list(res)



text = readFile('全唐诗-曹寅.txt')

segs = parse(text)
writeFile('tmp/sentence.txt', '\n'.join(segs))

out = list(analytic(segs, 500))
print(pretty(out[0][:500]))
print(pretty(out[1][:500]))
print(pretty(out[2][:100]))
print(pretty(out[3][:100]))

