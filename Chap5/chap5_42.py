# encoding: utf-8

import chap5_41


if __name__ == '__main__':
    sentences = chap5_41.read_neko_chunk()
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            print(''.join([m.surface if m.surface != "、" or m.surface != "。" else "" for m in chunk.morphs]) + '\t' +
                  ''.join([m.surface if m.surface != "、" or m.surface != "。" else "" for m in sentence[chunk.dst].morphs]))
