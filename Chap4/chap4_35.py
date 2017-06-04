# encoding: utf-8

import chap4_30


if __name__ == '__main__':
    nouns = []
    for sentence in chap4_30.read_neko():
        for word in sentence:
            if word["pos"] == "名詞":
                nouns.append(word["surface"])
            else:
                if len(nouns) >= 2:
                    print(''.join(w for w in nouns))
                nouns = []
