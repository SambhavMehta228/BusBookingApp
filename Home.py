import tkinter as tk
from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.title('Online Bus Booking System')
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1)
Label(root,text='Online Bus Booking System',font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=1)
def cmd1():
    root.destroy()
    import journeydetails  
def cmd2():
     root.destroy()
     import checkbookedseat
    
def cmd3():
     root.destroy()
     import page3
Button(root,text='Seat Booking',command=cmd1,font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4').grid(row=2,column=0,pady=1)
Button(root,text='Check Booked Seat',font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4',command=cmd2).grid(row=2,column=1,pady=1)
Button(root,text='Add Bus Detail',command=cmd3,font='Cosmic 12 bold',bg='lightblue1',fg='turquoise4').grid(row=2,column=2,pady=1)
Label(root,text='For Administrator Only',font='Cosmic 12 bold',fg='cyan4').grid(row=3,column=2)




root.mainloop()
