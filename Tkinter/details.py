from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('450x550')
root.title("Welcome To Student Info Center")
root.configure(background="silver")

#Entry widget object

textin=StringVar()

#Dictionaries

exlist={'Abhishek':'Information Tech','Sam':'Mechanical','Jack':'Computer','Erik':'Electronics','john':'Robotics',
        'Mayur':'Information Tech','Akshay':'Robotics','Bhavesh':'Computer','Sameer':'Electronics','Sagar':'Robotics','Tushar':'CS GOD'}

def clk():
     entered = ent.get()
     output.delete(0.0,END)
     try:
          textin = exlist[entered]
     except:
          textin = 'SORRY NO INFO \n AVAILABLE!!!!!!!!\n'
     output.insert(0.0,textin)

def ex():
   tkinter.messagebox.showinfo("Program",'Exit')
   exit()
     
def exitt():
     tkinter.messagebox.showinfo("Program",'Exit')
     exit()   

def me():
     text='\n XYZ \n OKAY DEXTER \n Nice'
     saveFile=open('text.txt','w')
     saveFile.write(text)
     print('This are the entries::',text)
     
   
def hel():
   help(tkinter)
   
def cont():
     tkinter.messagebox.showinfo("S/W Contributors",'\n 1.Abhishek\n 2.Erik \n 3.Sam \n 4.Jack \n 5.John \n ___Version 1.0___')
     
def clr():
     textin.set(" ")
     

menu = Menu(root)
root.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label="File",menu=subm)
subm.add_command(label="Memo",command=me)
subm.add_command(label="Save")
subm.add_command(label="Save As")
subm.add_command(label="Print")
subm.add_command(label="Exit",command=ex)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Tkinter Help",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=cont)


lab=Label(root,text='Name :',font=('none 20 bold'))
lab.grid(row=0,column=1,sticky=W)

ent=Entry(root,width=20,font=('none 18 bold'),textvar=textin,bg='white')
ent.grid(row=0,column=2,sticky=W)


but=Button(root,padx=2,pady=2,text='Submit',command=clk,bg='powder blue',font=('none 18 bold'))
but.place(x=100,y=90)


but4=Button(root,padx=2,pady=2,text='Clear',font=('none 18 bold'),bg='powder blue',command=clr)
but4.place(x=220,y=90)



output=Text(root,width=20,height=8,font=('Time 20 bold'),fg="black")
output.place(x=100,y=200)


labb=Label(root,text='Results',font=('non 18 bold'))
labb.place(x=0,y=180)


but1=Button(root,padx=2,pady=2,text='Exit',command=exitt,bg='powder blue',font=('none 18 bold'))
but1.place(x=200,y=470)


root.mainloop()
