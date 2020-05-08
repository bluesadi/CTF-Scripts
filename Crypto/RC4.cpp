/*
RC4加解密cpp实现
参考资料：https://blog.csdn.net/cpongo3/article/details/89708316
*/
#include <bits/stdc++.h>
using namespace std;
#define byte unsigned char

byte S[256],T[256];

void RC4Init(const byte *key,int keylen){
    for(int i = 0;i < 256;i ++) S[i] = i;
    for(int i = 0;i < 256;i ++) T[i] = key[i % keylen];
    int j = 0;
    for (int i = 0 ;i < 256 ;i ++){
        j = (j + S[i] + T[i]) % 256;
        swap(S[i] , S[j]);
    }
}

void PRGA(byte *plaintext,int len){
    int x = 0,y = 0;
    for(int i = 0;i < len;i ++){
        x = (x + 1) % 256;
        y = (y + S[x]) % 256;
        swap(S[x],S[y]);
        int r = (S[x] + S[y]) % 256;
        plaintext[i] ^= S[r];
    }
}

byte* RC4Encrypt(byte *plaintext,int len,const byte *key,int keylen){
    byte* ciphertext = (byte*)malloc(keylen * sizeof(byte));
    RC4Init(key,keylen);
    PRGA(plaintext,len);
}

int main(){
    byte plaintext[100] = "\x9D\x87\x71\xA4\x83\x0B\xAA\x53\xC4\x38\x36\x85";
    int len = 12;
    byte key[100] = "a1dWT1pJXF1USVxRV1ZbUElQSVBJ";
    int keylen = 28;
    RC4Encrypt(plaintext,12,key,28);
    for(int i = 0;i < 12;i ++) putchar(plaintext[i]);
}