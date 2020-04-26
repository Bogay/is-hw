import re
import json
from collections import defaultdict


def freq(s: str):
    '''
    analysis the frequency of each character
    '''
    d = defaultdict(int)
    for c in s:
        if c.islower():
            d[c] += 1
    return sorted(d.items(), key=lambda v: (v[1], v[0]), reverse=True)


if __name__ == '__main__':
    # constants
    CIPHERTEXT = 'frequency_attack.txt'
    TABLE = 'table.json'
    # read data
    ct = [*open(CIPHERTEXT).read()]
    d = json.load(open(TABLE))
    # substitution
    for i, c in enumerate(ct):
        ct[i] = d.get(c, c)
    ct = ''.join(ct)
    # highlight lower letter
    ct = re.sub(r'[a-z]', lambda m: f'\033[91m{m.group(0)}\033[0m', ct)
    print(ct)