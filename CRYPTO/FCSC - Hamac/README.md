# HAMAC
```
Type : Cryptography
Plateform : FCSC
Difficulty : [x] [x] [] [] []
Tools : Python / HashCat
```
#### STEP 1
 - Decode first HMAC hash generated in output.txt (h)
 - A hint talk about rockyou wordlist, try to bruteforce with hashcat tool</br>
 - Create file hash.txt (with hash + key) : `hash:FCSC2022` and run hashcat</br>
`-->  hashcat -a 0 -m 1450 hash.txt /usr/share/wordlists/rockyou.txt`
 - Found password : `omgh4xx0r`
#### STEP 2
 - Unexify the second hash generated in output.txt (iv)
```
iv = binascii.unhexlify("ea425b2ea4bb67445abe967e3bd1b583")
```
 - Serialize main encoded hash in good format (c)
```
encoded = binascii.unhexlify("
    69771c85e2362a35eb0157497e9e2d17858bf11492e003c4aa8ce1b76d8d3a31ccc3412ec6e619e79
    96190d8693299fc3873e1e6a96bcc1fe67abdf5175c753c09128fd1eb2f2f15bd07b12c5bfc2933")
```
#### STEP 3
 - Generate sha256 hash for `omgh4xx0r` password
 - Create new AES encoded format with hash and iv
 - Uncrypt the AES encoded hash and decode in utf-8
```
hash = SHA256.new('omgh4xx0r').digest()
flag = AES.new(hash, AES.MODE_CBC, iv = iv)
flag = flag.decrypt(encoded).decode('utf-8')
```
#### FLAG
`==> FCSC{5bb0780f8af31f69b4eccf18870f493628f135045add3036f35a4e3a423976d6}`