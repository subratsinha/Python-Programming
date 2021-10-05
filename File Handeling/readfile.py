with open('file1.txt', 'r',encoding="utf8") as f1:
    data = f1.read()

with open('file2.txt', 'w',encoding="utf8") as f2:
    f2.write(data.replace('\"', '\\\"'))
    f2.close()
f=open("file2.txt","r",encoding="utf8")
data1=f.read()

print(str(data))
print(str(data1))
