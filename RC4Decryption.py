#RC4解密脚本
from Crypto.Cipher import ARC4

data = b"\x9D\x87\x71\xA4\x83\x0B\xAA\x53\xC4\x38\x36\x85"
key = b"a1dWT1pJXF1USVxRV1ZbUElQSVBJ"
m = ARC4.new(key).decrypt(data)
print(m.decode())