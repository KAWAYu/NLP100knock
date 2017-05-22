# encoding: utf-8

import codecs
import sys
import pprint

"""
split
"""

if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
    except IndexError:
        print("Usage: python 16.py N")
        sys.exit()
    except ValueError:
        print('Invalid argument!')
        sys.exit(0)
    sentences = [[] for _ in range(N)]
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        file_lines = list(map(lambda x: x.strip(), fin))
        line_num = len(file_lines)
        line_per = line_num // N
        r = line_num % N
        for i in range(N):
            for _ in range(line_per):
                sentences[i].append(file_lines.pop())
            if r:
                sentences[i].append(file_lines.pop())
                r -= 1
    pprint.pprint(sentences)

