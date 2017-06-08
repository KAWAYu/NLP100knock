# encoding: utf-8

import chap5_41


if __name__ == '__main__':
    sentences = chap5_41.read_neko_chunk()
    for sentence in sentences:
        for chunk in sentence:
            for prev_m in chunk.morphs:
                if prev_m.pos == "名詞":
                    is_prev = True
                    break
            if is_prev and chunk.dst != -1:
                for pos_m in sentence[chunk.dst].morphs:
                    if pos_m.pos == "動詞":
                        print(''.join([prev_m.surface if prev_m.surface != "、" and prev_m.surface != "。" else ""
                                       for prev_m in chunk.morphs]) + '\t' +
                              ''.join([pos_m.surface if pos_m.surface != "、" and pos_m.surface != "。" else ""
                                       for pos_m in sentence[chunk.dst].morphs]))
                        break
                is_prev = False
