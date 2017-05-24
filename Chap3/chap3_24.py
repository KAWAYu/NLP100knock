# encoding: utf-8

import re
import chap3_20


if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text('イギリス')
    for line in eng_line.split('\n'):
        if re.search(r'\[\[ファイル:', line):
            print(re.search(r'\[\[ファイル:(.+?)\|(.+?)\|(.+?)\]\]', line).group(1))
        elif re.search(r'\[\[file:', line):
            print(re.search(r'\[\[file:(.+?)|(.+?)|(.+?)\]\]', line).group(1))
