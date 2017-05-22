# encoding: utf-8

import codecs
import sys

"""
head -N hightemp.txt
"""

if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
    except IndexError:
        print("Usage: python 14.py N")
        sys.exit()
    except ValueError:
        print("please input valid number!")
        sys.exit()
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        for i, line in enumerate(fin):
            print(line.strip())
            if i+1 == N:
                break

    # print('\n'.join([s.strip() for s in codecs.open('hightemp.txt', 'r', 'utf-8')][:int(sys.argv[1])]))
