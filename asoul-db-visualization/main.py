#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import jieba
from os import path
from math import log
from wordcloud import WordCloud

ignore_words = ['我', '你', '的', '了', '我们', '你们',
                '是', '就', '嗯', '啊', '吗', '吧', '哈哈', '哈哈哈']

dirname = path.split(path.realpath(__file__))[0]
source_files = [
    path.join(dirname, 'db/BV1f64y1i7Mv-1.srt'),
    path.join(dirname, 'db/BV1f64y1i7Mv-2.srt'),
]
dist_file = path.join(dirname, 'dist.png')

source = {}
for file in source_files:
    with open(file, 'r+', encoding='utf-8') as f:
        plain = f.read()
        f.close()
    sentences = plain.split('\n')[2::4]
    for sentence in sentences:
        words = jieba.cut(sentence, cut_all=False)
        for word in words:
            if word not in source:
                source[word] = 0
            source[word] += 1
for ignore_word in ignore_words:
    source[ignore_word] = log(source[ignore_word])

wc = WordCloud(height=800, width=2000, background_color="white",
               margin=2, font_path=path.join(dirname, 'Lolita.ttf'))
im = wc.generate_from_frequencies(source)
im.to_file(dist_file)
