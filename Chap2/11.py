# encoding: utf-8

import codecs

"""
cat hightemp.txt | sed ""???
cat hightemp.txt | tr "\t" " "

"""


if __name__ == '__main__':
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        for line in fin:
            new_line = line.strip().replace('\t', ' ')
            print(new_line)

    # print('\n'.join([s.strip().replace('\t', ' ') for s in codecs.open('hightemp.txt', 'r', 'utf-8')]))
