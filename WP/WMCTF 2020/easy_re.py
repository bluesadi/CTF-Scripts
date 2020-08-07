import os

srcfile = open("WP/WMCTF 2020/src","r")

src = srcfile.read().replace('\n','').split(' ')

code = ''

for c in src:
    if len(c) == 2:
        code += chr(int(c,16))

print(code)