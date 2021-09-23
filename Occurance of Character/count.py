

strin = input("enter thr string :")
strin=strin.upper()
dict1 = {}  
    
for i in strin:  
    if i in dict1:  
        dict1[i] += 1
    else:  
        dict1[i] = 1
s=str(dict1)
print ("Occurrence  of character : "+ s)



