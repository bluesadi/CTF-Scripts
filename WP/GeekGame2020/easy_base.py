import base64
import string

str1 = "UoH+U/DJV/YlQdUOU94JPYxJgdHMUWK="

string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZpqrstlmno56yz234ajk01ubcdefghivwx789+/"
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print (base64.b64decode(str1.translate(str.maketrans(string1,string2))))