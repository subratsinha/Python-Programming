


file=open("rhyme.txt","r",encoding="utf8")
count=0
for line in file:
    words = line.split(" ");  
    count = count + len(words);  
   
print("Number of words present in given file: " + str(count));  
file.close()

file1=open("rhyme.txt","r",encoding="utf8")
d=dict()
for l in file1:
    l=l.strip()
    l=l.lower()
    words = l.split(" ")
    for w in words: 
        if w in d: 
            d[w] = d[w] + 1
        else: 
            d[w] = 1


file2=open("words.txt","wt",encoding="utf8")

file2.write(str(d))
file2.close()
