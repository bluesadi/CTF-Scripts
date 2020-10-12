/*
RC4加解密 C/CPP实现
2020/10/12 by bluesadi
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
#define Byte unsigned char
using std::swap;

Byte S[256],T[256];
char key[256] = "yydsyyds";
int keylen = strlen(key);

void RC4Init(){
    for(int i = 0;i < 256;i++) S[i] = i,T[i] = key[i % keylen];
    int j = 0;
    for(int i = 0;i < 256;i++){
        j = (j + S[i] + T[i]) % 256;
        swap(S[i],S[j]);
    }
}

void RC4(Byte *dest,const char *src){
    RC4Init();
    int i = 0,j = 0;
    for(int k = 0;src[k];k++){
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        swap(S[i],S[j]);
        int t = (S[i] + S[j]) % 256;
        dest[k] = src[k] ^ S[t];
    }
}

int main(){
    Byte *dest = new Byte[100];
    memset(dest,0,100);
    RC4(dest,"yyds");
    printf("b'");
    for(int i = 0;dest[i];i++){
        printf("\\x%x",dest[i]);
    }
    printf("'");
}