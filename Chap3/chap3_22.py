# encoding: utf-8

import re
import chap3_20


def extract_category_content():
    return [re.findall(r'\[\[Category:(.+)\]\]', l)[0] for l in list(filter(lambda s: '[[Category:' in s, chap3_20.extract_nation_text('イギリス').split('\n')))]

if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text('イギリス')
    for line in eng_line.split('\n'):
        if re.search(r'\[\[Category:(.+)\]\]', line):
            print(re.search(r'\[\[Category:(.+)\]\]', line).group(1))
    #for cont in extract_category_content():
    #    print(cont)
