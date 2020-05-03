'''
Base64隐写解密脚本
'''
import base64

BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def decrypt():
    bin_str = ''
    with open('stego.txt') as file:
        for line in file:
            line = line.replace('\n','')
            equ_cnt = line.count('=')
            if(equ_cnt):
                last_chr = BASE64.index(line[len(line) - equ_cnt - 1])
                bin_str += bin(last_chr).replace('0b','').zfill(8)[8 - 2 * equ_cnt:]
    flag = ''
    for i in range(0,len(bin_str),8):
        flag += chr(int(bin_str[i:i + 8],2))
    return flag


print(decrypt())