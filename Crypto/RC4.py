'''
RC4加解密 Python实现
'''
from Crypto.Cipher import ARC4

def RC4(key,text):
    cipher = ARC4.new(key)
    return cipher.encrypt(text)

print(RC4(b'yydsyyds',b'yyds'))