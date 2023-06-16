from tkinter import *
from tkinter.messagebox import *
import sqlite3
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.title('Bus ticket')
Label().grid(row=0,column=0,padx=w/5.5)
bus_img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=1,columnspan=4)
Label(root,text="Online Bus Booking System",font='Cosmic 30 bold',fg='slategray1',bg='skyblue2').grid(row=1,column=1,columnspan=4)
Label(root,text='Bus Ticket',font='Cosmic 15 italic',fg='deepskyblue4').grid(row=2,column=1,columnspan=4)
frame=Frame(root,relief='groove',bd=5)
frame.grid(row=3,column=1)
Label(frame,text='Passengers:',font='Cosmic 12 bold',fg='blue1').grid(row=3,column=1)
Label(frame,text='Gender:',font='Cosmic 12 bold',fg='blue1').grid(row=3,column=3)
Label(frame,text='No. of seats:',font='Cosmic 12 bold',fg='blue1').grid(row=4,column=1)
Label(frame,text='Phone:',font='Cosmic 12 bold',fg='blue1').grid(row=4,column=3)
Label(frame,text='Age:',font='Cosmic 12 bold',fg='blue1').grid(row=5,column=1)
Label(frame,text='Fare Rs:',font='Cosmic 12 bold',fg='blue1').grid(row=5,column=3)
Label(frame,text='Booking Ref.:',font='Cosmic 12 bold',fg='blue1').grid(row=6,column=1)
Label(frame,text='Bus details:',font='Cosmic 12 bold',fg='blue1').grid(row=6,column=3)
Label(frame,text='Travel on:',font='Cosmic 12 bold',fg='blue1').grid(row=7,column=1)

con=sqlite3.Connection('Busbookingpythongui')
cur=con.cursor()
cur.execute('''select max(booking_ref_number) from bookinghistory''')
a=cur.fetchone()
num=a[0]
cur.execute('''select * from bookinghistory where booking_ref_number=?''',[num])
res=cur.fetchall()
for i in res:
    Label(frame,text=i[0],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=2,padx=w//60)
    Label(frame,text=i[1],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=3,column=4)
    Label(frame,text=i[7],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=4,column=2)
    Label(frame,text=i[3],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=4,column=4)
    Label(frame,text=i[2],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=2)
    Label(frame,text=i[8],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=5,column=4)
    Label(frame,text=i[9],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=6,column=2)
    Label(frame,text=i[4],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=6,column=4)
    Label(frame,text=i[5],font='Cosmic 12 bold',fg='dodgerblue3').grid(row=7,column=2)
    f=str(i[8])


Label(frame,text='Total amount of Rs '+f+' to be paid at the time of boarding',font='calibri 12 italic').grid(row=9,column=1,columnspan=4)
con.commit()
con.close()
 
showinfo('Success','Seat Booked...')

root.mainloop()
