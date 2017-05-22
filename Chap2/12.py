# encoding: utf-8

import codecs

"""
cut -f1,2 hightemp.txt
"""

if __name__ == '__main__':
    with codecs.open('hightemp.txt', 'r', 'utf-8') as hightemp, codecs.open('col1.txt', 'w', 'utf-8') as col1, codecs.open('col2.txt', 'w', 'utf-8') as col2:
        for line in hightemp:
            cols = line.strip().split()
            print(cols[0], file=col1)
            print(cols[1], file=col2)
