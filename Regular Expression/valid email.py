



expression = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

 
 
email=input("enter your email id :")


if(re.search(expression, email)):
    print("valid email address")
 
else:
    print("invalid email address")
