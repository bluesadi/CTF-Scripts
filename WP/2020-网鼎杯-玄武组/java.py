import base64
from Crypto.Cipher import AES

def decrypt(text):
     key = 'aos_chock_koy!@#'.encode('utf-8')
     mode = AES.MODE_ECB
     cryptor = AES.new(key, mode)
     plain_text = cryptor.decrypt(text)
     return bytes.decode(plain_text).rstrip('\0')

f2525c = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 43, 103, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 43, 103, 170, 68, 19, 38, 73, 134, 43, 103, 153, 156, 66, 80, 244, 145, 80, 103, 239, 152, 122, 98, 50, 214]

flag = base64.b64decode(b"VsBDJCvuhD65/+sL+Hlf587nWuIa2MPcqZaq7GMVWI0Vx8l9R42PXWbhCRftoFB3")

flag = bytearray(flag)

for i in range(len(flag)):
    flag[i] ^= f2525c[i]
    flag[i] ^= 22

print(decrypt(flag))
