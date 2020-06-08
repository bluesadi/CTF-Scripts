#include <cstdio>
#include <cstring>
#include <windows.h>
#define BYTE unsigned char

char flag[100] = "hboiu}cmQ?}Qi>>js";

void encrypt(char* str, int len) {
	for (int i = 0; i < len; i++) {
		str[i] ^= 0x0E;
	}
}

LONG WINAPI MyUnhandledExceptionFilter(PEXCEPTION_POINTERS pExceptionPtrs)
{
	printf("Wrong\n");
	system("pause");
	exit(0);
}
int init()
{
	PBYTE addr = (BYTE*)encrypt;
	DWORD old;
	if (VirtualProtect(addr, 20, PAGE_EXECUTE_READWRITE, &old) == NULL)
	{
		MessageBoxA(NULL, "A Fatal Error Occured!", "ERROR", MB_OK);
		exit(0);
	}
	SetUnhandledExceptionFilter(MyUnhandledExceptionFilter);
	return 1;
}
int doit = init();

//flag{smc_1s_g00d}
int main() {
	char input[100];
	printf("Please input your flag:");
	scanf("%s", input);
	int len = strlen(input);
	if (len != 17) {
		printf("Error!\n");
		exit(0);
	}
	for (int i = 0; i < 76; i++) {
		((BYTE*)encrypt)[i] ^= 0x1C;
	}
	encrypt(input,len);
	if (!strcmp(input, flag)) {
		printf("Right!\n");
		system("pause");
		exit(0);
	}
	printf("Wrong!\n");
	return 0;
}
