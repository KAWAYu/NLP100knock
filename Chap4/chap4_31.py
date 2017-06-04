# encoding: utf-8

import chap4_30


if __name__ == '__main__':
    for sentence in chap4_30.read_neko():
        for word in sentence:
            if word["pos"] == "動詞":
                print("表層形:", word["surface"])
        print("-----")
