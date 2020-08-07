import os

fo = open("D:\\CTF\\CTF-Scripts\\temp\\test.txt", "r")


rawlist = fo.read().replace('\n',' ').split(' ')

cnt = 0
index = 1
arglist = []
solve = 'from z3 import *\n\n'
x = [0x313EF, 0x32F1B, 0x31C4E, 0x3246F, 0x30158, 0x33BF0
,0x2E3C8, 0x2A9B9, 0x30344, 0x31749, 0x2D060, 0x2D97F
,0x345ED, 0x35BA8, 0x27523, 0x3729D, 0x31A55, 0x335FF
,0x29380, 0x32DA3, 0x33F5D, 0x35B6C, 0x2EAA9, 0x3241A
,0x2B11A, 0x3062D, 0x31041, 0x33820, 0x2BA33, 0x322E9
,0x2FFCD, 0x38606]

for i in range(1,33):
    solve += f'x{i} = Real(\'x{i}\')\n'

solve += 's = Solver()\n'

for c in rawlist:
    if len(c) == 2 and c != '00':
        arglist.append(int(c,16))
        cnt += 1
        if cnt == 32:
            f = f's.add('
            for i in range(32):
                f += f'{arglist[i]} * x{i + 1}'
                if i != 31:
                    f += ' + '
            f += f' == {x[index - 1]})\n'
            solve += f
            arglist.clear()
            cnt = 0
            index += 1

solve += 's.add('

for i in range(1,33):
    solve += f'x{i} > 32'
    if(i != 32):
        solve += ','

solve += ')\n'

solve += 's.add('

for i in range(1,33):
    solve += f'x{i} < 127'
    if(i != 32):
        solve += ','

solve += ')\n'

solve += 's.check()\ns.model()'

fw = open("D:\\CTF\\CTF-Scripts\\WP\\2020-天翼杯\\re1.py",'w+')
fw.write(solve)
fw.close()
