# encoding: utf-8

import re
import chap3_20


if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text('イギリス')
    for line in eng_line.split('\n'):
        if re.search(r'^(=+)(.+)(\1)$', line):
            print("Section:" + re.findall(r'(=+)(.+)(\1)', line)[0][1])
            print("Level:" + str(len(re.findall(r'(=+)(.+)(\1)', line)[0][0])-1))
