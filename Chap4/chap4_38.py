# encoding: utf-8

import chap4_30
from collections import Counter
import matplotlib.pyplot as plt


if __name__ == '__main__':
    cnt = Counter()
    for sentence in chap4_30.read_neko():
        cnt += Counter([w['surface'] for w in sentence])
    (_, max_cnt) = cnt.most_common(1)[0]
    y = [0 for _ in range(max_cnt)]
    for _, v in cnt.most_common():
        y[v-1] += 1
    plt.bar(range(max_cnt), y, width=1.0, align='edge')
    plt.show()
