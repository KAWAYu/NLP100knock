# encoding: utf-8

import chap4_30
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib as mpl


if __name__ == '__main__':
    mpl.rcParams['font.family'] = 'AppleGothic'
    cnt = Counter()
    for sentence in chap4_30.read_neko():
        cnt += Counter([w['surface'] for w in sentence])
    keys, values = [], []
    for k, v in cnt.most_common(10):
        keys.append(k)
        values.append(v)
    plt.bar(range(len(keys)), values, width=0.5,
            tick_label=keys, align='center')
    plt.show()
