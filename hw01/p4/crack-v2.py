import string
from collections import Counter


def list_xor(al: list, bl: list) -> tuple:
    return [a ^ b for a, b in zip(al, bl)]


if __name__ == '__main__':
    CIPHERTEXT = 'ciphertext'
    cs = [[int(v, 16) for v in l.split()]
          for l in open(CIPHERTEXT).readlines()]
    xcs = []
    for i, c in enumerate(cs[:-1]):
        for j, d in enumerate(cs[i + 1:]):
            xcs.append(((i, i + j + 1), ''.join(map(chr, list_xor(c, d)))))
    rs = [(t, ''.join(map(lambda c: c.lower() if c.isalpha() else '_', xc)))
          for t, xc in xcs]
    pk = []  # possible keys
    for i, c in enumerate(cs[-1]):
        ms = []
        for (a, b), s in rs:
            if len(s) <= i:
                continue
            if not s[i].isalpha():
                continue
            _s = ord(s[i])
            ms.extend((cs[a][i] ^ _s, cs[b][i] ^ _s))
        # print(ms)
        cms = Counter(ms)
        cms = sorted(cms.items(), key=lambda x: (-x[1], x[0]))
        pk.append(cms[0][0] if len(cms) else None)
    print(pk)
    msg = [a ^ b if b else 64 for a, b in zip(cs[-1], pk)]
    msg = ''.join(map(chr, msg)).replace('@', '\\w')
    print(msg)