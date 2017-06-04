# encoding: utf-8

import chap4_30


if __name__ == '__main__':
    prev1 = ""
    prev2 = False
    for sentence in chap4_30.read_neko():
        for word in sentence:
            if word['pos'] == "名詞":
                if prev2 and prev1:
                    print(prev1 + "の" + word["surface"])
                prev1 = word["surface"]
                prev2 = False
            elif word['pos'] == "助詞" and word['surface'] == "の":
                prev2 = True
            else:
                prev1 = ""
                prev2 = False
