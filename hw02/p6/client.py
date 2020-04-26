import requests as rq
import random
import logging
import asyncio
from binascii import hexlify, unhexlify
from aiohttp import ClientSession

cs = [
    *map(
        lambda s: unhexlify(s.strip()),
        open('ciphertext'),
    ),
]
oracle = 'http://140.122.185.173:8080/oracle'


async def crack(iv: bytes, c: bytes):
    '''
    crack a ciphertext `c` (iv + 1 block)
    '''
    # forged IV
    _iv = bytearray([random.randint(0, 255) for _ in range(16)])
    # middle value
    mid = bytearray(16)
    # for each round, we want to get a padding with length `i+1`
    async with ClientSession() as sess:
        for i in range(16):
            for j in range(i):
                _iv[j] = mid[j] ^ (i + 1)
            for j in range(256):
                _iv[i] = j
                _c = hexlify(_iv[::-1] + c).decode('ascii')
                logging.debug(f'try {_c}')
                r = await sess.get(f'{oracle}/{_c}')
                rt = await r.text()
                logging.debug(rt)
                # got correct value
                if rt == 'valid':
                    mid[i] = j ^ (i + 1)
                    break
            # failed
            else:
                logging.error(
                    'can not find padding value for '
                    f'ciphertext {hexlify(c).decode("ascii")}', )
                logging.error(
                    f'intermediate value: {hexlify(mid).decode("ascii")}')
                exit(1)
    # get message
    mid = mid[::-1]
    msg = bytearray([a ^ b for a, b in zip(mid, iv)])
    # msg = msg.decode('utf-8')
    logging.debug(f'intermediate value: {hexlify(mid).decode("ascii")}')
    logging.info(f'{hexlify(c).decode("ascii")} -> {msg}')
    return msg


async def crack_all(cs):
    res = await asyncio.gather(*[crack(a, b) for a, b in zip(cs, cs[1:])])
    ret = bytearray()
    for r in res:
        ret += r
    return ret


def strip_padding(bs: bytearray):
    return bs[:-bs[-1]]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    p = loop.run_until_complete(crack_all(cs))
    print(strip_padding(p).decode('utf-8'))
    loop.close()