#include <cstdio>

int main(){
    char fake[100] = "scu_ctf_f4k3_f14g";
    char fstr[100] = "pbm`KkL`dKQ2KeJLd";
    for(int i = 0;i < 25;i ++) putchar(fstr[i] * 2 - fake[i]);
}