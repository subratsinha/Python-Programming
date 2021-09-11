dct = {}
lst = list()
n=int(input("enter number of student :"))
for i in range(0,n):
    name = input("enter a name and marks of 3 subject :");
    lst = name.split()
    key = lst[0]; 
    dct[key]=float((float(lst[1])+float(lst[2])+float(lst[3]))/3);
    
search=input("enter the name of student you want to search :");
print((dct[search]))
