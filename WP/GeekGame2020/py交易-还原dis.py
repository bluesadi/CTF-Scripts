import dis

def func():
    inputs = input('please your flag:')
    inputs = inputs[7:-1]
    flag = 'th31_scuctf_eXclus1v3'
    theflag = ''
    i = 0
    j = 0
    print(flag)
    if len(flag) != len(inputs):
        print("Error!")
        return
    for i in range(0,len(flag) - 14):
        theflag += chr(ord(flag[i]) + ord(inputs[i + 8]))
    for i in range(10,len(flag) - 6):
        theflag += chr(ord(flag[i]) + ord(inputs[i - 8]))
        j = i + 1
    for i in range(j,len(flag)):
        theflag += chr(ord(flag[i - 3]) + ord(inputs[i]))
    flags = list(theflag)
    for i in range(0,len(flags) // 2):
        flags[i] = chr(ord(flags[i]) + 20)
    flagt = flags[len(flags) // 2:len(flags)]
    theflag = ''.join(flagt)
    for k in range(0,len(flags) // 2):
        theflag = theflag + ''.join(flags[k])
    print(theflag)
    if(theflag == '×\x8bÙÍ\x8cÓÜî¤ú±¬¤¤úÖíÒ'):
        print("You win!")
    else:
        print("Error!!!")

dis.dis(func)