#include <cstdio>
#define BYTE unsigned char

int start_addr = 0xB30;
int end_addr = 0xB30 + 76;

int main(){
    BYTE buffer[100];
    int addr = start_addr,len = end_addr - start_addr + 1;
    printf("Patched addr is 0x%x\n",addr);
    FILE* pfile = fopen("SMCDemo.exe","r+");
    fseek(pfile,addr,SEEK_SET);
    fread(buffer,sizeof(char),len,pfile);
    for(int i = 0;i < len;i ++){
        buffer[i] ^= 0x1C;
    }
    fseek(pfile,addr,SEEK_SET);
    fwrite(buffer,sizeof(char),len,pfile);
    fclose(pfile);
}