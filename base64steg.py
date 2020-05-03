import base64
 
def encrypt():
    with open('stego.txt') as file:
        for line in file:
            line = line.replace('\n','0')
            print(line)

encrypt()