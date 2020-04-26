from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
from ctypes import *
from datetime import datetime, timedelta
import pytz

iv = unhexlify('09080706050403020100A2B2C2D2E2F2')
plaintext = unhexlify('255044462d312e350a25d0d4c5d80a34')
ciphertext = unhexlify('d06bf9d0dab8e8ef880660d2af65aa82')
# setup c random function
rand = cdll.LoadLibrary('./librand.so')
rand.gen_key.restype = POINTER(c_char)
rand.gen_key.argtype = [c_uint]
# time duration
end = datetime(2018, 4, 17, 23, 8, 49, tzinfo=pytz.timezone('US/Eastern'))
start = int((end - timedelta(hours=2)).timestamp())
end = int(end.timestamp())
print(start, end)
# brute force
for t in range(start, end + 1):
    key = rand.gen_key(c_uint(t))[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    _ciphertext = cipher.encrypt(plaintext)
    if _ciphertext == ciphertext:
        print(f'timestamp: {t}\nkey: {hexlify(key).decode("ascii")}')