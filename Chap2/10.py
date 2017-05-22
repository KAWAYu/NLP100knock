# encoding: utf-8

import codecs

"""
wc hightemp.txt
"""

if __name__ == '__main__':
    with codecs.open('hightemp.txt', 'r', 'utf-8') as hightemp:
        count = 0
        for line in hightemp:
            if line.strip():
                count += 1
        print(count)

    # print(len(list(codecs.open('hightemp.txt', 'r', 'utf-8'))))
