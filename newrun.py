from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
h=PhotoImage(file='.\\home.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=7,padx=w//2.9
                           )
Label(root,text="Online Bus Booking System",font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=0,columnspan=7)
Label(root,text="Add Bus Running Details",font='Cosmic 25 italic',fg='deepskyblue4').grid(row=2,column=0,columnspan=7,pady=25)
Label(root,text="Bus Id",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=0)
bi=Entry(root)
bi.grid(row=3,column=1)
Label(root,text="Running Date",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=2)
rd=Entry(root)
rd.grid(row=3,column=3)
Label(root,text="Seat Available",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=4)
s=Entry(root)
s.grid(row=3,column=5)
def cd():
    if bi.get()=='':
        showerror('Error','Please enter Correct Bus Unique Number')
    elif rd.get()=='':
        showerror('Error','Please enter Correct Running Date')
    elif s.get()=='':
        showerror('Error','Please enter How Many Seat Available ?')
    else:
        rbid=bi.get()
        rdate=rd.get()
        seat=s.get()
        connection=sqlite3.Connection('Busbookingpythongui')
        c=connection.cursor()

        c.execute('''insert into runningdetails(rbid,running_date,seat_available) values(?,?,?)''',(rbid,rdate,seat))
        connection.commit()
        connection.close()
        showinfo('Running bus details','Bus running details added successfully')
    
Button(root,text="Add Run",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=cd).grid(row=3,column=6,padx=20)
def dd():
    if bi.get()=='':
        showerror('Error','Please enter Correct Bus Unique Number')
    elif rd.get()=='':
        showerror('Error','Please enter Correct Running Date')
    else:
        rbid=bi.get()
        rdate=rd.get()
        connection=sqlite3.Connection('Busbookingpythongui')
        cur=connection.cursor()

        cur.execute('''delete from running_details where rbid=? and running_date=?''',(rbid,rdate))
        connection.commit()
        connection.close()
        showinfo('Running details','Bus running details deleted successfully')
        
Button(root,text="Delete Run",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=dd).grid(row=3,column=7)
def hi():
    root.destroy()
    import Home
Button(root,image=h,bg='turquoise4',command=hi).grid(row=4,column=7,padx=20,pady=30)
root.mainloop()
