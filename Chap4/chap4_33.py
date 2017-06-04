# encoding: utf-8

import chap4_30


if __name__ == '__main__':
    for sentence in chap4_30.read_neko():
        for word in sentence:
            if word['pos1'] == "サ変接続" and word['pos'] == "名詞":
                print(word["surface"])
        print("-----")
