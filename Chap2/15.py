# encoding: utf-8

import codecs
import sys

"""
tail -N hightemp.txt
"""

if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
    except IndexError:
        print("Usage: python 15.py N")
        sys.exit()
    except ValueError:
        print("please input valid number!")
        sys.exit()
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        lines = []
        for line in fin:
            lines.append(line)
            if len(lines) > N:
                del lines[0]
        for line in lines:
            print(line.strip())

    # print('\n'.join([s.strip() for s in codecs.open('hightemp.txt', 'r', 'utf-8')][-int(sys.argv[1]):]))
