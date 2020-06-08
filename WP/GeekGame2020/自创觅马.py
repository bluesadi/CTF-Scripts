encrypt = "hlimiuaxhiurxhefwxehyiatumx"

flag = ''

for c in encrypt:
    v = ord(c) - ord('a')
    for k in range(0,100):
        if v + k * 26 - 8 >= 0 and (v + k * 26 - 8) % 5 == 0:
            flag += chr((v + k * 26 - 8) // 5 + ord('a'))
            break

print(flag)