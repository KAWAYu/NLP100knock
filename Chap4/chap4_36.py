# encoding: utf-8

import chap4_30
from collections import Counter

if __name__ == '__main__':
    cnt = Counter()
    for sentence in chap4_30.read_neko():
        cnt += Counter([w['surface'] for w in sentence])
    for k, v in cnt.most_common():
        print(k + ': ' + str(v) + '回')
