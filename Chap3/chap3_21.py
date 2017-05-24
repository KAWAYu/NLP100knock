# encoding: utf-8

import chap3_20


def extract_category_line():
    return list(filter(lambda s: 'Category' in s, chap3_20.extract_nation_text('イギリス').split('\n')))

if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text('イギリス')
    for line in eng_line.split('\n'):
        if 'Category' in line:
            print(line)
    #for line in extract_category_line():
    #    print(line)
