# encoding: utf-8

import codecs

"""
cut -f1 hightemp.txt | sort | uniq
"""

if __name__ == '__main__':
    col1_list = []
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        for line in fin:
            col1_list.append(line.strip().split()[0])
    col1_set = set(col1_list)
    print(col1_set)

    # print(set([s.strip().split()[0] for s in codecs.open('hightemp.txt', 'r', 'utf-8')]))
