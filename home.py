from tkinter import *
from PIL import Image,ImageTk
import pylint


root=Tk()
root.geometry("1000x650")
root.resizable(False,False)
bgphoto=Image.open("./img/background.jpg")
bg_image=ImageTk.PhotoImage(bgphoto)

f1=Frame(root,bg="red").pack()
f2=Frame(root).pack()

lo=Image.open("./img/logo.png")
lo=lo.resize((150,100),Image.ANTIALIAS)
logo=ImageTk.PhotoImage(lo)
Label(f1,image=logo).pack(anchor="nw")
Label(f1,text="Company Name",font="forte 35").place(x=350,y=15)

def register():

    root.destroy()
    import reg
# slide show code start-------------------------------------------
img1=Image.open("./img/1.jpg")
img1=img1.resize((1000,350),Image.ANTIALIAS)

img2=Image.open("./img/2.jpg")
img2=img2.resize((1000,350),Image.ANTIALIAS)
img3=Image.open("./img/3.jpg")
img3=img3.resize((1000,350),Image.ANTIALIAS)
img4=Image.open("./img/4.jpg")
img4=img4.resize((1000,350),Image.ANTIALIAS)
img5=Image.open("./img/5.jpg")
img5=img5.resize((1000,350),Image.ANTIALIAS)
img6=Image.open("./img/6.jpg")
img6=img6.resize((1000,350),Image.ANTIALIAS)
img7=Image.open("./img/7.jpg")
img7=img7.resize((1000,350),Image.ANTIALIAS)
img8=Image.open("./img/8.jpg")
img8=img8.resize((1000,350),Image.ANTIALIAS)
img9=Image.open("./img/9.jpg")
img9=img9.resize((1000,350),Image.ANTIALIAS)
img10=Image.open("./img/10.jpg")
img10=img10.resize((1000,350),Image.ANTIALIAS)

img1=ImageTk.PhotoImage(img1)
img2=ImageTk.PhotoImage(img2)
img3=ImageTk.PhotoImage(img3)
img4=ImageTk.PhotoImage(img4)
img5=ImageTk.PhotoImage(img5)
img6=ImageTk.PhotoImage(img6)
img7=ImageTk.PhotoImage(img7)
img8=ImageTk.PhotoImage(img8)
img9=ImageTk.PhotoImage(img9)
img10=ImageTk.PhotoImage(img10)

l=Label(f2,)
l.place(x=-1,y=100)
x=1
def a():
    global x
    if x==11:
        x=1
    if x==1:
        l.config(image=img1)
    elif x==2:
        l.config(image=img2)
    elif x==3:
        l.config(image=img3)
    elif x==4:
        l.config(image=img4)
    elif x==5:
        l.config(image=img5)
    elif x==6:
        l.config(image=img6)
    elif x==7:
        l.config(image=img7)
    elif x==8:
        l.config(image=img8)
    elif x==9:
        l.config(image=img9)
    elif x==10:
        l.config(image=img10)
    x+=1
    root.after(2000,a)
a()
# slider ended----

f3=Frame(root,height="150",width="380",bg="gray").place(x=300,y=460)
Label(f3,text="User Name",font="bill 12 bold",bg="gray").place(x=350,y=480)
tb1=Entry(f3,font="bill 11 bold")
tb1.place(x=470,y=480)
Label(f3,text="Password",font="bill 12 bold",bg="gray").place(x=350,y=510)
tb2=Entry(f3,font="bill 11 bold")
tb2.place(x=470,y=510)
Button(f3,text="Login",font="bill 13 bold").place(x=470,y=560)
Button(f3,text="Register",font="bill 13 bold",command=register).place(x=550,y=560)




root.mainloop()
