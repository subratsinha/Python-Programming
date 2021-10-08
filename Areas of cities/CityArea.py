


f1=open("city.txt","r+",encoding="utf8")
d=dict()
for line in f1:
    key = line.split() 
    value = line.split()
    d[key[0]] = value[1:] 
print("details of all cities are displayed below:-\n")
print(d)

print("\ncity having population greater than 10 laks are listed below:-\n")
for key, value in d.items():
    
    if(float(value[0])>10):
        print(key)
        
res=0
for key, value in d.items():
    
    res=res+float(value[1])
print("\nsum of area of all cities are =",res)
