# encoding: utf-8

import re
import chap3_20


if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text("イギリス")
    in_basic_info = False
    my_dict = {}
    for line in eng_line.split('\n'):
        print(line)
        if not in_basic_info and "{{基礎情報" in line:
            in_basic_info = True
        elif in_basic_info:
            if line == "}}":
                break
            else:
                if re.findall(r'\|(.+?) = (.+)$', line.strip()):
                    k, v = re.findall(r'\|(.+?) = (.+)$', line.strip())[0]
                    my_dict[k] = v
    print(my_dict)
    for k, v in my_dict.items():
        print(k + ':' + v)
