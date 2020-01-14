from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
import shutil
import mysql.connector


root1 = Tk()
root1.geometry("600x500")
root1.resizable(False,False)

upload=""
count=0
def up():
    global upload
    upload=filedialog.askopenfilename()
    pimg=Image.open(upload)
    pimg=pimg.resize((120,150),Image.ANTIALIAS)
    ph=ImageTk.PhotoImage(pimg)
    print("WOrking")
    photo.config(text="Working",image=ph,height="150",width="120")
    photo.image=ph

def sub():
    global count
    if count==0 and tb1.get()!="" and tb2.get()!=""and tb3.get()!=""and tb4.get()!="" :
        f=open("./database.txt","a")
        f.write("Name : "+tb1.get()+"| Class : "+tb2.get()+"| Roll No. : "+tb3.get()+"| Email : "+tb4.get()+"\n")
        messagebox.showinfo("Success","Data Saved Success Fully")
        shutil.copy(upload,f"./databasephoto/{tb2.get()+tb3.get()}.jpg")
        count=1
    else:
        messagebox.showwarning("data Stored","please Click clear first for new data or Enter DATA")

def cls():
    global count
    tb1.delete(0,END)
    tb2.delete(0,END)
    tb3.delete(0,END)
    tb4.delete(0,END)
    count=0
Label(root1,text="Register Here",font="algerian 25 bold").place(x=180,y=10)
Label(root1,text="--------------------------------------------------------------------------------",font="bold").place(x=120,y=50)
c=Frame(root1,height="230",width="540",relief=SUNKEN,bg="white").place(x=30,y=100)
Label(c,text="Enter Name",font="bell 14").place(x=50, y=110)
tb1=Entry(c,font="century 12")
tb1.place(x=200, y=110)
Label(c,text="Class",font="bell 14").place(x=50, y=145)
tb2=Entry(c,font="century 12")
tb2.place(x=200, y=145)

Label(c,text="Roll No.",font="bell 14").place(x=50, y=180)
tb3=Entry(c,font="century 12")
tb3.place(x=200, y=180)
Label(c,text="Email ID.",font="bell 14").place(x=50, y=215)
tb4=Entry(c,font="century 12")
tb4.place(x=200, y=215)
Label(c,text="Mobile No.",font="bell 14").place(x=50, y=250)
tb4=Entry(c,font="century 12")
tb4.place(x=200,y=250)

submit=Button(c,text="Submit",font="agency 14 bold",command=sub).place(x=255,y=285)
photo=Button(c,text="Click here \nto upload image",bg="gray",command=up,height="8",width="14")
photo.place(x=420,y=110)
clear=Button(c,text="Clear",command=cls,font="agency 14 bold").place(x=120,y=285)
close=Button(c,text="Close",font="agency 14 bold",command=quit).place(x=425,y=285)

root1.mainloop()
