from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=7,padx=w//3.0)
Label(root,text="Online Bus Booking System",font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=0,columnspan=7)
Label(root,text="Add Bus Route Details",font='Cosmic 25 italic',fg='deepskyblue4').grid(row=2,column=0,columnspan=7,pady=5)
Label(root,text="Route Id:",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=0)
ri=Entry(root)
ri.grid(row=3,column=1)
Label(root,text="Station Name:",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=2)
st=Entry(root)
st.grid(row=3,column=3)
Label(root,text="Station Id:",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=4)
si=Entry(root)
si.grid(row=3,column=5)
def cd():
    routeid=ri.get()
    sname=st.get()
    sid=si.get()
    connection=sqlite3.Connection('Busbookingpythongui')
    c=connection.cursor()
    c.execute(''' insert into routedetails(routeid,sname,sid) values(?,?,?)''',(routeid,sname,sid))
    connection.commit()
    connection.close()
    messagebox.showinfo('Route Entry Completed','Bus Route Added Successfully')
Button(root,text="Add Route",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=cd).grid(row=3,column=6,padx=5)
def dd():
    routeid=ri.get()
    sname=st.get()
    sid=si.get()
    connection=sqlite3.Connection('Busbookingpythongui')
    c=connection.cursor()
    c.execute(''' delete from route_details where rid=? and sid=?''',(routeid,sid))
    connectioncommit()
    connection.close()
    showinfo('Route Removed','Bus Route Deleted Succesfully')
Button(root,text="Remove This Route",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=dd).grid(row=3,column=7)
def hi():
    root.destroy()
    import Home
h=PhotoImage(file='.\\home.png')
Button(root,image=h,bg='turquoise4',command=hi).grid(row=4,column=7,padx=5,pady=5)
root.mainloop()
