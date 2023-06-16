import tkinter as tk
from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.title('Online Bus Booking System')
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=0)
root.columnconfigure(2,weight=0)
root.columnconfigure(3,weight=1)
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1)
Label(root,text='Online Bus Booking System',font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=1)
Label(root,text='Add New Details To DataBase',font='Cosmic 15 italic',fg='deepskyblue4').grid(row=2,column=1)
def cmd1():
    root.destroy()
    import newoperator
def cmd2():
    root.destroy()
    import newbus
def cmd3():
    root.destroy()
    import newroute
def cmd4():
    root.destroy()
    import newrun
Button(root,text='New Operator',command=cmd1,font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4').grid(row=3,column=0)
Button(root,text='New Bus',command=cmd2,font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4').grid(row=3,column=1)
Button(root,text='New Route',command=cmd3,font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4').grid(row=3,column=2)
Button(root,text='New Run',command=cmd4,font='cosmic 12 bold',bg='lightblue1',fg='turquoise4').grid(row=3,column=3)
def hi():
    root.destroy()
    import Home
h=PhotoImage(file='.\\home.png')
Button(root,image=h,bg='turquoise4',command=hi).grid(row=4,column=3,padx=5,pady=5)
root.mainloop()
