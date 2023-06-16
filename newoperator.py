from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
connection=sqlite3.connect('Busbookingpythongui')
c=connection.cursor()


bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=11,padx=w//2.7)
Label(root,text="Online Bus Booking System",font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=0,columnspan=11,pady=5)
Label(root,text="Add operator Details",font='Cosmic 15 italic',fg='deepskyblue4').grid(row=2,column=0,columnspan=11,pady=5)
Label(root,text="Operator Details",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=0)
id=Entry(root)
id.grid(row=3,column=1)
Label(root,text="Name",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=2)
name=Entry(root)
name.grid(row=3,column=3)
Label(root,text="Address",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=4)
add=Entry(root)
add.grid(row=3,column=5)
Label(root,text="Mobile Number",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=6)
mno=Entry(root)
mno.grid(row=3,column=7)
Label(root,text="Electronic Mail",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=8)
email=Entry(root)
email.grid(row=3,column=9)
def cd():
    count=False
    oi=id.get()
    if oi=='':
        showerror('Error','Please Enter Correct Operator Id')
        count=True
    name1=name.get()
    if name1=='':
        showerror('Error','Please Enter Correct Name')
        count=True
    add1=add.get()
    if add1=='':
        showerror('Error','Please Enter Address')
        count=True
    ph1=mno.get()
    if ph1=='':
        showerror('Error','Please Enter Correct Mobile Number')
        count=True
    e=email.get()
    if e=='':
        showerror('Error','Please Enter Correct Electronic Mail')
        count=True
    if count==False :
        c.execute(''' Insert Into operatordetails(opname,oid,address,mobileno,electronicmail) values(?,?,?,?,?)''',(name1,oi,add1,ph1,e))
        c.commit()
        c.close()
def ex():
    root.destroy()
Button(root,text="Add",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=cd).grid(row=3,column=10)
Button(root,text="Exit",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=ex).grid(row=3,column=11)

def hi():
    root.destroy()
    import Home
h=PhotoImage(file='.\\home.png')
Button(root,image=h,bg='turquoise4',command=hi).grid(row=5,column=11,pady=15)
root.mainloop()

