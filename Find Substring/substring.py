



str1 = input("enter the string :")
substr = input("enter the substrings you want to search :")

strlen=len(str1)
sublen=len(substr)
count = 0
for i in range(strlen - sublen +1):
    if str1[i:i + sublen] == substr:
        count += 1
print ("substring occurs",count,"times")
