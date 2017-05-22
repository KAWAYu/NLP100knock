# encoding: utf-8

import codecs
from collections import Counter

"""
cut -f1 hightemp.txt | sort | uniq -c | sort -k1nr
"""

if __name__ == '__main__':
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        my_dict = {}
        for line in fin:
            e = line.strip().split()[0]
            if e in my_dict:
                my_dict[e] += 1
            else:
                my_dict[e] = 1
        for k, _ in sorted(my_dict.items(), key=lambda x: -x[-1]):
            print(k)
    # print('\n'.join([k[0] for k in Counter([s.strip().split()[0] for s in codecs.open('hightemp.txt', 'r', 'utf-8')]).most_common()]))
    # print('\n'.join(sorted()))
