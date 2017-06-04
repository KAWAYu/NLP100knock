# encoding: utf-8

import chap4_30
import matplotlib.pyplot as plt
from collections import Counter


if __name__ == '__main__':
    cnt = Counter()
    for sentence in chap4_30.read_neko():
        cnt += Counter([w['surface'] for w in sentence])
    y = [v for _, v in cnt.most_common()]
    plt.plot([i+1 for i in range(len(y))], y, 'b-')
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
