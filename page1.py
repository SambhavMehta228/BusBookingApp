import tkinter as tk
from tkinter import *
root=tk.Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.title('Online Bus Booking System')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).pack()
Label(root,text='Online Bus Booking System',font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').pack()
Label(root,text='Name : Mr.Sambhav Mehta',font='Cosmic 15 italic',fg='steelblue4').pack()
Label(root,text='Enrollment Number : 211B268',font='Cosmic 15 italic',fg='steelblue4').pack()
Label(root,text='Contact Number : 8529631306',font='Cosmic 15 italic',fg='steelblue4').pack()
Label(root,text='Submitted To : Dr.Mahesh Kumar And Dr.Nilesh Patel',font='Cosmic 15 italic',fg='deepskyblue3').pack()
def hi(e):
    root.destroy()
    import Home
root.bind('<KeyPress>',lambda e:hi(e))




root.mainloop()
