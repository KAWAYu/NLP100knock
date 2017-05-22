# encoding: utf-8

import codecs

"""
sort -k3r hightemp.txt
"""

if __name__ == '__main__':
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        sorted_lines = []
        for line in fin:
            temp = line.strip().split()[2]
            for i in range(len(sorted_lines) + 1):
                if i == len(sorted_lines):
                    sorted_lines.append(line.strip())
                elif temp > sorted_lines[i]:
                    sorted_lines.insert(i, line.strip())
        print('\n'.join([line for line in sorted_lines]))

    print('\n'.join(sorted([s.strip() for s in codecs.open('hightemp.txt', 'r', 'utf-8')], key=lambda y: -float(y.split()[2]))))
