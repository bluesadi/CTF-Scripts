import os

zfile = open("daolnwod.zip","rb")
out = open("download.zip","wb")

out.write(zfile.read()[::-1])
out.close()

