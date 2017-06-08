# encoding: utf-8

import codecs
from chap5_40 import Morph


class Chunk(object):
    def __init__(self, d):
        self.morphs = None
        self.dst = d
        self.srcs = []


def read_neko_chunk():
    morphs = []
    ds_pairs = []
    sentences = []
    sentence = []
    with codecs.open("neko.txt.cabocha", 'r', 'utf-8') as neko:
        for line in neko:
            line = line.strip('\n')
            if line == 'EOS':
                # 一行の終わりの時
                if morphs:  # 形態素列があるなら
                    sentence[-1].morphs = morphs
                    morphs = []
                if ds_pairs:
                    for ds_pair in ds_pairs:
                        if ds_pair[1] == -1:
                            continue
                        sentence[ds_pair[1]].srcs.append(ds_pair[0])
                    ds_pairs = []
                if sentence:  # 行があるなら（空行でないなら）
                    sentences.append(sentence)
                    sentence = []
            elif line.startswith('* '):
                # 文節情報を表す行の時
                line = line.split()
                if morphs:  # 前の形態素列があるなら
                    sentence[-1].morphs = morphs
                    morphs = []
                sentence.append(Chunk(int(line[2][:-1])))
                ds_pairs.append((int(line[1]), int(line[2][:-1])))
            else:
                # 上記以外 = 形態素を表す行
                line = line.split('\t')
                s = line[0]
                line = line[1].split(',')
                b, p, p1 = line[6], line[0], line[1]
                morphs.append(Morph(s, b, p, p1))
    return sentences


if __name__ == '__main__':
    sentences = read_neko_chunk()
    for chunk in sentences[7]:
        print("文字列:", ''.join([m.surface for m in chunk.morphs]))
        print("係り先:", chunk.dst)
