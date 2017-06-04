# encoding: utf-8

import codecs


def read_neko():
    sentences = []
    sentence = []
    with codecs.open("neko.txt.mecab", 'r', 'utf-8') as neko:
        for line in neko:
            line = line.strip('\n')
            if line == 'EOS':
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            else:
                tokens = line.split('\t')
                tokens[1] = tokens[1].split(',')
                sentence.append({
                    "surface": tokens[0],
                    "base": tokens[1][6],
                    "pos": tokens[1][0],
                    "pos1": tokens[1][1]
                })
    return sentences

if __name__ == "__main__":
    print(read_neko())
