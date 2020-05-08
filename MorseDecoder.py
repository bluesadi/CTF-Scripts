#摩斯电码解码脚本
table = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
'--.':'G', '....':'H', '..':'I','.---':'J','-.-':'K','.-..':'L',
'--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S',
'-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
'-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5',
'-....':'6','--...':'7','---..':'8','----.':'9','.-.-.-':'.',
'---...':':','--..--':',','-.-.-.':';','..--..':'?','-...-':'=',
'.----.':'\'','-..-.':'/','-.-.--':'!','-....-':'-','..--.-':'_',
'.-..-.':'\"','-.--.':'(','-.--.-':')','...-..-':'$','.--.-.':'@'}

text = 'BABA BBB BA BBA ABA AB B AAB ABAA AB B AA BBB BA AAA BBAABB AABA ABAA AB BBA BBBAAA ABBBB BA AAAB ABBBB AAAAA ABBBB BAAA ABAA AAABB BB AAABB AAAAA AAAAA AAAAB BBA AAABB'

def decode(text):
    text = text.replace('/',' ')
    arr = text.split(' ')
    result = ''
    for s in arr:
        result += table[s]
    return result

print(decode(text.replace('B','-').replace('A','.')))