from tkinter import *
import sqlite3
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=w//2.8)
Label(root,text="Online Bus Booking System",font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=0,columnspan=10)
Label(root,text="Add Bus Details",font='Cosmic 25 italic',fg='deepskyblue4').grid(row=2,column=0,columnspan=10,pady=10)
Label(root,text="Bus Unique Number",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=0)
bi=Entry(root)
bi.grid(row=5,column=1)
Label(root,text="Bus Type",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=2)
btype=StringVar()
types=('AC 2x2','AC 3x2','Non AC 2x2','Non AC 3x2','AC-Sleeper 2x1','Non-AC Sleeper 2x1')
btype.set('Bus Type')
m=OptionMenu(root,btype,*types)
m.config(font='Cosmic 12 italic',fg='dodgerblue3')
m["menu"].config(font='Cosmic 15')
m.grid(row=5,column=2)
Label(root,text="Capacity",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=3)
ca=Entry(root)
ca.grid(row=5,column=4)
Label(root,text="Fair",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=5)
f=Entry(root)
f.grid(row=5,column=6)
Label(root,text="Operator Id",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=7)
oi=Entry(root)
oi.grid(row=5,column=8)
Label(root,text="Route Id",font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=9)
ri=Entry(root)
ri.grid(row=5,column=10)
def cd():
    busid=bi.get()
    bus_type=btype.get()
    capacity=ca.get()
    fare=f.get()
    oid=oi.get()
    rid=ri.get()
    
    if busid=='':
        showerror('Error','Please enter Correct Bus Unique Number')
    elif bus_type=='Bus type':
        showerror('Error','Please select Bus Type')
    elif capacity=='':
        showerror('Error','Please enter Capacity')
    elif fare=='':
        showerror('Error','Please enter Fare')
    elif oid=='':
        showerror('Error','Please enter Operator Id')
    elif rid=='':
        showerror('Error','Please enter Route Id')
    else:
        connection=sqlite3.Connection('Busbookingpythongui')
        c=con.cursor()
        c.execute('''select opname from operatordetails where oid=?''',(oid,))
        res=cur.fetchall()
        c.execute('''insert into busdetails(bid,bustype,opname,operatorid,route_id,seatcapacity,fare) values(?,?,?,?,?,?,?)''',(busid,bus_type,res[0][0],oid,rid,capacity,fare))
        connection.commit()
        connection.close()
        showinfo('Bus entry','Bus record added Successfully')
def ed():
    if busid.get()=='':
        showerror('Error','Please enter Bus Id')
    elif bus_type.get()=='Bus type':
        showerror('Error','Please select Bus Type')
    elif capacity.get()=='':
        showerror('Error','Please enter Capacity')
    elif fare.get()=='':
        showerror('Error','Please enter Fare')
    elif oid.get()=='':
        showerror('Error','Please enter Operator Id')
    elif rid.get()=='':
        showerror('Error','Please enter Route Id')
    else:
        showinfo('Bus updation','Bus record updated successfully')
Button(root,text="Add Bus",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=cd).grid(row=7,column=4,pady=20)
Button(root,text="Edit Bus",font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=ed).grid(row=7,column=5,pady=20)
def hi():
    root.destroy()
    import Home
h=PhotoImage(file='.\\home.png')
Button(root,image=h,command=hi,bg='turquoise4').grid(row=7,column=6,pady=20)
root.mainloop()

