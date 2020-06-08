enflag = '×\x8bÙÍ\x8cÓÜî¤ú±¬¤¤úÖíÒ'
flag = 'th31_scuctf_eXclus1v3'
ans = 'd1' + '_' * 19
step1 = enflag[9:] + enflag[0:9]
print(ans)
print(step1) 
theflag = ''
for i in range(0,9):
    theflag += chr(ord(step1[i]) - 20)
theflag += step1[9:]
print(theflag)

inputs = list(ans)

for i in range(0,7):
    inputs[i + 8] = chr(ord(theflag[i]) - ord(flag[i]))

for i in range(10,15):
    inputs[i - 8] = chr(ord(theflag[i - 3]) - ord(flag[i]))

for i in range(15,21):
    inputs[i] = chr(ord(theflag[i - 3]) - ord(flag[i - 3]))
inputs[7] = '3'

print('scuctf{' + ''.join(inputs) + '}')
