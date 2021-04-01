#import tuple
import os

"""""
print("digraph G {")
for i in os.walk('/Users/felikstitov'):
     for j in i[2]:
         str = i[0].replace('/', '->')
         j = j.replace('.', '_')
         str = str[2:len(str)]
         print(str +'->'+j)

print("}")
"""""

def banner(text):
    res = []
    with open ("standard.txt") as fi:
        linesBruh = fi.read()
        lines = linesBruh.split("@@")

    lines.pop()

    i = 0
    for line in lines:
        res.append(line.split("@\n"))

        if(res[i][0][:1] == "@\n"):
            res[i][0] = res[i][0].replace("\n","")

        i += 1
    for j in range(6):
        temp = ""
        for i in range(len(text)):
            cIndex = ord(text[i])

            if 97 <= cIndex <=122:
                temp += res[cIndex -71][j]

        print(temp)


print(banner("kis python 13"))