# encoding: utf-8

import codecs


class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return "<Morph Class>\n  surface: {}, base: {}, pos: {}, pos1: {}".format(self.surface, self.base, self.pos, self.pos1)


if __name__ == '__main__':
    sentences = []
    sentence = []
    with codecs.open('neko.txt.cabocha', 'r', 'utf-8') as neko:
        for line in neko:
            line = line.strip('\n')
            if line == 'EOS':
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            elif line.startswith('*'):
                pass
            else:
                line = line.split('\t')
                surface = line[0]
                line = line[1].split(',')
                base, pos, pos1 = line[-3], line[0], line[1]
                sentence.append(Morph(surface, base, pos, pos1))
    print(' '.join(m.surface for m in sentences[2]))
    print(sentences[1][0])
