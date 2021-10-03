



def check_baggage(w):
    if (w>=0 and w<=40):
        return True
    else:
        return False
        
def check_immigration(d):
    if(d>=2030 and d<=2050):
        return True
    else:
        return False
        
def check_security(s):
    if (s=='valid' or s=='VALID'):
        return True
    else:
        return False
        
def traveler(t_id,name,wgt,date,sec):
    check_baggage(wgt)
    check_immigration(date)
    check_security(sec)
    if (check_baggage(wgt)==True and check_immigration(date)==True and check_security(sec)==True):
        print("traveller_id :",t_id)
        print("traveller name :",name)
        print("allow traveller to fly")
    else:
        print("traveller_id",t_id)
        print("traveller name :",name)
        print("detain traveller for rechecking")
        
name=input("enter the name :")
iden=input("enter the traveller id :")
wt=int(input("enter the bag weight:"))
yr=int(input("enter the expiry year :"))
st=input("enter the noc status :")
traveler(iden,name,wt,yr,st)
