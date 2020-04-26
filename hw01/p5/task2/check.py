'''
for the purpose of checking python and c random number equality 
'''

import subprocess

with open('output') as f:
    for l in f:
        s, k = l.split()
        p = subprocess.run(
            './rand',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            input=s.encode('ascii'),
        )
        o = p.stdout.decode('ascii').strip()
        if o != k:
            print(s, o, k)