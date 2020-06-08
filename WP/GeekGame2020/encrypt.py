def c2i(c):
    return ord(c)-ord('a')

def i2c(i):
    return chr(i+ord('a'))

def affine(x):
    return (5 *x +8)%26

flag = input()
assert(flag.startswith('flag'))
result = "".join([i2c(affine(c2i(i))) for i in flag ] )
encrypt = "hlimiuaxhiurxhefwxehyiatumx"
if (encrypt == result):
    print("correct!")
else:
    print("wrong!")
