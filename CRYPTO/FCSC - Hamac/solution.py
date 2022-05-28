# python3 -m pip install pycryptodome
import json
import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

print("Enter your password")
password = input(">>> ").encode()
h = HMAC.new(password, digestmod = SHA256)
h.update(b"FCSC2022")

iv = binascii.unhexlify("ea425b2ea4bb67445abe967e3bd1b583")
encoded = binascii.unhexlify("69771c85e2362a35eb0157497e9e2d17858bf11492e003c4aa8ce1b76d8d3a31ccc3412ec6e619e7996190d8693299fc3873e1e6a96bcc1fe67abdf5175c753c09128fd1eb2f2f15bd07b12c5bfc2933")
hash  = SHA256.new(password).digest()
flag = AES.new(hash, AES.MODE_CBC, iv = iv)
flag = flag.decrypt(encoded).decode('utf-8')
print("GG! Here is your flag:", flag)
