# encoding: utf-8

import re
import chap3_20


def make_dict(lines):
    in_basic_info = False
    my_dict = {}
    for line in lines:
        if not in_basic_info and "{{基礎情報" in line:
            in_basic_info = True
        elif in_basic_info:
            if line == "}}":
                break
            else:
                if re.findall(r'\|(.+?) = (.+)$', line.strip()):
                    k, v = re.findall(r'\|(.+?) = (.+)$', line.strip())[0]
                    if re.match(r'{{lang\|', v):
                        v = re.sub(r'{{lang\|(.+?)\|(.+)\}\}', r'\2', v)
                    if re.search(r'\[\[ファイル:', line):
                        v = re.sub(r'\[\[ファイル:(.+?)\|(.+?)\|(.+?)\]\]', r'\1', v)
                    if re.search(r'\'\'\'\'\'(.+)\'\'\'\'\'', v):
                        trans_strs = re.findall(r'\'\'\'\'\'(.+)\'\'\'\'\'', v)
                        for trans_str in trans_strs:
                            v = v.replace('\'\'\'\'\'' + trans_str + '\'\'\'\'\'', trans_str)
                    if re.search(r'\'\'\'(.+)\'\'\'', v):
                        trans_strs = re.findall(r'\'\'\'(.+)\'\'\'', v)
                        for trans_str in trans_strs:
                            v = v.replace('\'\'\'' + trans_str + '\'\'\'', trans_str)
                    if re.search(r'\'\'(.+)\'\'', v):
                        trans_strs = re.findall(r'\'\'(.+)\'\'', v)
                        for trans_str in trans_strs:
                            v = v.replace('\'\'' + trans_str + '\'\'', trans_str)
                    if re.search(r'\[\[(.+?)(\|.*?)?\]\]', v):
                        trans_strs = re.findall(r'\[\[(.+?)(\|.*?)?\]\]', v)
                        print(trans_strs)
                        for trans_str in trans_strs:
                            v = v.replace('[[' + trans_str[0] + trans_str[1] + ']]', trans_str[1][1:]) if trans_str[1]\
                                    else v.replace('[[' + trans_str[0] + trans_str[1] + ']]', trans_str[0])
                    if re.search(r'\[(.+)\]', v):
                        trans_strs = re.findall(r'\[(.+?)\]', v)
                        for trans_str in trans_strs:
                            v = v.replace('[' + trans_str + ']', trans_str)
                    my_dict[k] = v
    return my_dict


if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text("イギリス")
    tmp_dict = make_dict(eng_line.split('\n'))
    for k, v in tmp_dict.items():
        print(k, ':', v)
