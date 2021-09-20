
s =input("enter your name :") 
l=s.split()
new=""
for i in range(len(l)-1):
    s=l[i]
    new =new + (s[0].upper()+'.')
new =new + l[-1].title()
print (new)
