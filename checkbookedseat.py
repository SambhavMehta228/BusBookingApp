from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
s,x=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(x,s))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=x//2.4,pady=30)
Label(root,text="Online Bus Booking System",font='Cosmic 30 bold',bg='skyblue2',fg='slategray1').grid(row=1,column=0,columnspan=3)
Label(root,text="Check Your Online Booking",font='Cosmic 15 italic',fg='deepskyblue4').grid(row=2,column=0,columnspan=3,pady=15)
Label(root,text="Enter Your Mobile Number",font='Cosmic 15 italic',fg='deepskyblue4').grid(row=3,column=0)
mn=Entry(root)
mn.grid(row=3,column=1)
cb=''
def cbooking():
    connection=sqlite3.Connection('Busbookingpythongui')
    c=connection.cursor()
    cb=mn.get()
    if cb=='':
        messagebox.showerror('Error','Please Enter Correct Mobile Number')
    else:
        frame=Frame(root,relief='groove',bd=5)
        frame.grid(row=5,column=0,columnspan=3,pady=s//70)
        Label(frame,text='Passengers:',font='Cosmic 15 italic').grid(row=5,column=0)
        Label(frame,text='Gender:',font='Cosmic 15 italic').grid(row=5,column=3)
        Label(frame,text='No. of seats:',font='Cosmic 15 italic').grid(row=6,column=0)
        Label(frame,text='Mobile Number:',font='Cosmic 15 italic').grid(row=6,column=3)
        Label(frame,text='Age:',font='Cosmic 15 italic').grid(row=7,column=0)
        Label(frame,text='Fare Rs:',font='Cosmic 15 italic').grid(row=7,column=3)
        Label(frame,text='Booking Ref.:',font='Cosmic 15 italic').grid(row=8,column=0)
        Label(frame,text='Bus details:',font='Cosmic 15 italic').grid(row=8,column=3)
        Label(frame,text='Travel on:',font='Cosmic 15 italic').grid(row=9,column=0)
        
        c.execute('''select * from bookinghistory where mobile=?''',[cb])
        res=c.fetchall()
        
        for i in res:
            Label(frame,text=i[0],font='Cosmic 15 italic').grid(row=5,column=2,padx=x//60)
            Label(frame,text=i[1],font='Cosmic 15 italic').grid(row=5,column=4)
            Label(frame,text=i[7],font='Cosmic 15 italic').grid(row=6,column=2)
            Label(frame,text=i[3],font='Cosmic 15 italic').grid(row=6,column=4)
            Label(frame,text=i[2],font='Cosmic 15 italic').grid(row=7,column=2)
            Label(frame,text=i[8],font='Cosmic 15 italic').grid(row=7,column=4)
            Label(frame,text=i[9],font='Cosmic 15 italic').grid(row=8,column=2)
            Label(frame,text=i[4],font='Cosmic 15 italic').grid(row=8,column=4)
            Label(frame,text=i[5],font='Cosmic 15 italic').grid(row=9,column=2)
            R=str(i[8])
        Label(frame,text='Total amount of Rs '+R+' to be paid at the time of boarding',font='Cosmic 15 italic').grid(row=9,column=1,columnspan=4)
        connection.commit()
        connection.close()        
        
        
Button(root,text="Check Booking",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=cbooking).grid(row=3,column=2)

root.mainloop()
