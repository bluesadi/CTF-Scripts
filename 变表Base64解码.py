import base64
import string

str1 = "PalXPrhnOrLZT6PVQJ1oNr9dSqDVTbo="

string1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/+abcdefghijklmnopqrstuvwxyz"
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print (base64.b64decode(str1.translate(str.maketrans(string1,string2))))