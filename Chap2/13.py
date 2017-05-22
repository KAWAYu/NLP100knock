# encoding: utf-8

import codecs
import itertools

"""
paste col1.txt col2.txt
"""

if __name__ == '__main__':
    with codecs.open('col1.txt', 'r', 'utf-8') as col1, codecs.open('col2.txt', 'r', 'utf-8') as col2, codecs.open('col12.txt', 'w', 'utf-8') as col12:
        for l1, l2 in itertools.zip_longest(col1, col2):
            if not l1:
                print('\t' + l2.strip(), file=col12)
            elif not l2:
                print(l1.strip() + '\t', file=col12)
            else:
                print(l1.strip() + '\t' + l2.strip(), file=col12)

    # print('\n'.join([l1.strip()+'\t'+l2.strip() for l1, l2 in itertools.zip_longest(codecs.open('col1.txt', 'r', 'utf-8'), codecs.open('col2.txt', 'r', 'utf-8'))]))
