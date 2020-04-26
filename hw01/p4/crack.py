import string
from functools import reduce
from collections import defaultdict
from itertools import chain


def xor_table() -> dict:
    d = defaultdict(list)
    s = ' .\'' + string.ascii_lowercase
    for i, a in enumerate(s):
        for b in s[i:]:
            v = ord(a) ^ ord(b)
            d[v].extend((a, b))
    return d


def list_xor(al: list, bl: list):
    return [a ^ b for a, b in zip(al, bl)]


if __name__ == '__main__':
    CIPHERTEXT = 'ciphertext'
    cs = [[int(v, 16) for v in l.split()]
          for l in open(CIPHERTEXT).readlines()]
    tar = cs[-1]
    del cs[-1]
    table = xor_table()
    # print(*table.items(), sep='\n')
    rs = [[table[v] for v in list_xor(c, tar)] for c in cs]
    for i in range(len(tar)):
        rks = [{*r[i]} for r in rs if len(r) > i]
        rks = reduce(lambda x, y: x & y, rks)
        print([*rks][0] if len(rks) == 1 else rks)
