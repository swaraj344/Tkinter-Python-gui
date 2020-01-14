from tkinter import *
import mysql.connector

root=Tk()
conn=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
rs=conn.cursor()
rs.execute("use swaraj")
def save():
    name=tb1.get()
    cl=tb2.get()
    roll=tb3.get()
    f=rs.execute(f"insert into stu values('{name}','{cl}','{roll}')")


print("Data SAved")
root.geometry("300x500")
Label(root,text="Name").pack()
tb1=Entry(root,)
tb1.pack()
Label(root,text="Class").pack()
tb2=Entry(root)
tb2.pack()
Label(root,text="Roll No.").pack()
tb3=Entry(root)
tb3.pack()
b=Button(root,text="Submit",command=save).pack()
root.mainloop()
