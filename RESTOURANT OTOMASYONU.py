from ast import operator
from cProfile import label
from cgitb import text
from email.utils import localtime
from tkinter import*
import random
import time
from tkinter import font
from turtle import right

from numpy import pad
pencere=Tk()
pencere.geometry("900x500+0+0")
pencere.title("KAFE OTOMATI")

text_Input=StringVar()
operator=""

Tops=Frame(pencere,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(pencere,width=800,height=700,bg="powder blue",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(pencere,width=300,height=300,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)
#********************** TİME *************************
localtime=time.asctime(time.localtime(time.time()))
#********************* info *************************
lblınfo=Label(Tops,font=("arial",50,"bold"),text="RESTOURANT OTOMASYONU",fg="steel blue",bd=10,anchor='w')
lblınfo.grid(row=0,column=0)

lblınfo=Label(Tops,font=("arial",20,"bold"),text=localtime,fg="steel blue",bd=10,anchor='w')
lblınfo.grid(row=1,column=0)

# *************************** CALCULATOR ******************************
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btncleardisplay():
    global operator
    operator=""    
    text_Input.set("")

def btnesittir():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""    

def Ref():
    x=random.randint(10908,50076)
    randomRef=str(x)
    rand.set(randomRef)
    Cof=float(Fries.get())
    Cod=float(Drinks.get())
    Cofilet=float(Filet.get())
    Coburger=float(Burger.get())
    coCohicburger=float(Chicken_burger.get())
    coCheese=float(Cheese_burger.get())
    
    CostofFries= Cof*0.99
    CostofDrinks= Cod*1.00
    CostofFilet= Cofilet*2.99
    CostofBURGER= Coburger*2.89
    Costochicken= coCohicburger*3.00
    Costofcheese= coCheese*2.99

    CostoMeal="₺",str('%.2f' % (CostofFries+CostofDrinks+CostofFilet+CostofBURGER+Costochicken+Costofcheese))

    PayTax=((CostofFries+CostofDrinks+CostofFilet+CostofBURGER+Costochicken+Costofcheese)*0.2)
    TotalCost=(CostofFries+CostofDrinks+CostofFilet+CostofBURGER+Costochicken+Costofcheese)
    Ser_Charge=((CostofFries+CostofDrinks+CostofFilet+CostofBURGER+Costochicken+Costofcheese)/99)

    Servicet="₺",str('%.2f' % Ser_Charge) 
    OverAllCost="₺",str('%.2f' % (PayTax+TotalCost+Ser_Charge))
    PaidTax="₺",str('%.2f' % PayTax)
    
    Service.get(Servicet)
    Cost.get(CostoMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostoMeal)
    Total.set(OverAllCost)




def Exit():
    pencere.destroy()

def Reset():
 rand.set("")
 Fries.set("")
 Burger.set("")
 Filet.set("")
 Subtotal.set("")
 Total.set("")
 Service.set("")
 Drinks.set("")
 Tax.set("")
 Cost.set("")
 Chicken_burger.set("")
 Cheese_burger.set("")





txtDisplay=Entry(f2,font=("arial",20,"bold"),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify="right")
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",bg="powder blue",command=lambda:btnClick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",bg="powder blue",command=lambda:btnClick(8))
btn8.grid(row=2,column=1)


btn9=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",bg="powder blue",command=lambda:btnClick(9))
btn9.grid(row=2,column=2)

btnarti=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",bg="powder blue",command=lambda:btnClick('+'))
btnarti.grid(row=2,column=3)




btn4=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",bg="powder blue",command=lambda:btnClick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",bg="powder blue",command=lambda:btnClick(5))
btn5.grid(row=3,column=1)


btn6=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",bg="powder blue",command=lambda:btnClick(6))
btn6.grid(row=3,column=2)

btneksi=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",bg="powder blue",command=lambda:btnClick('-'))
btneksi.grid(row=3,column=3)



btn1=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",bg="powder blue",command=lambda:btnClick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",bg="powder blue",command=lambda:btnClick(2))
btn2.grid(row=4,column=1)


btn3=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",bg="powder blue",command=lambda:btnClick(3))
btn3.grid(row=4,column=2)

btncarp=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",bg="powder blue",command=lambda:btnClick('*'))
btncarp.grid(row=4,column=3)




btn0=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",bg="powder blue",command=lambda:btnClick(0))
btn0.grid(row=5,column=0)

btnesit=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",bg="powder blue",command=btnesittir)
btnesit.grid(row=5,column=1)


btnclear=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",bg="powder blue",command=btncleardisplay)
btnclear.grid(row=5,column=2)

btnbol=Button(f2,padx=2,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",bg="powder blue",command=lambda:btnClick('/'))
btnbol.grid(row=5,column=3)


#*************************************
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
Subtotal=StringVar()
Total=StringVar()
Service=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_burger=StringVar()
Cheese_burger=StringVar()

lblreferance=Label(f1,font=("arial",16,"bold"),text="referance",bd=16,anchor='w')
lblreferance.grid(row=0,column=0)
txtreferance=Entry(f1,font=("arial",16,"bold"),textvariable=rand,bd=10,insertwidth=4,bg="powder blue")
txtreferance.grid(row=0,column=1)

lblFries=Label(f1,font=("arial",16,"bold"),text="Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=("arial",16,"bold"),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue")
txtFries.grid(row=1,column=1)

lblBurger=Label(f1,font=("arial",16,"bold"),text="Burger",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=("arial",16,"bold"),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue")
txtBurger.grid(row=2,column=1)

lblFilet=Label(f1,font=("arial",16,"bold"),text="Filet",bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=("arial",16,"bold"),textvariable=Filet,bd=10,insertwidth=4,bg="powder blue")
txtFilet.grid(row=3,column=1)


lblSubtotal=Label(f1,font=("arial",16,"bold"),text="Subtotal",bd=16,anchor='w')
lblSubtotal.grid(row=4,column=0)
txtSubtotal=Entry(f1,font=("arial",16,"bold"),textvariable=Subtotal,bd=10,insertwidth=4,bg="powder blue")
txtSubtotal.grid(row=4,column=1)


lbltotal=Label(f1,font=("arial",16,"bold"),text="Total",bd=16,anchor='w')
lbltotal.grid(row=5,column=0)
txttotal=Entry(f1,font=("arial",16,"bold"),textvariable=Total,bd=10,insertwidth=4,bg="powder blue")
txttotal.grid(row=5,column=1)


lblservice=Label(f1,font=("arial",16,"bold"),text="Service",bd=16,anchor='w')
lblservice.grid(row=6,column=0)
txtservice=Entry(f1,font=("arial",16,"bold"),textvariable=Service,bd=10,insertwidth=4,bg="powder blue")
txtservice.grid(row=6,column=1)


lbldrinks=Label(f1,font=("arial",16,"bold"),text="Drinks",bd=16,anchor='w')
lbldrinks.grid(row=7,column=0)
txtdrinks=Entry(f1,font=("arial",16,"bold"),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue")
txtdrinks.grid(row=7,column=1)

lbltax=Label(f1,font=("arial",16,"bold"),text="Tax",bd=16,anchor='w')
lbltax.grid(row=8,column=0)
txttax=Entry(f1,font=("arial",16,"bold"),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue")
txttax.grid(row=8,column=1)

lblcost=Label(f1,font=("arial",16,"bold"),text="Cost",bd=16,anchor='w')
lblcost.grid(row=0,column=2)
txtcost=Entry(f1,font=("arial",16,"bold"),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue")
txtcost.grid(row=0,column=3)

lblcburger=Label(f1,font=("arial",16,"bold"),text="Chicken_burger",bd=16,anchor='w')
lblcburger.grid(row=1,column=2)
txtcburger=Entry(f1,font=("arial",16,"bold"),textvariable=Chicken_burger,bd=10,insertwidth=4,bg="powder blue")
txtcburger.grid(row=1,column=3)

lblcb=Label(f1,font=("arial",16,"bold"),text="Cheese_burger",bd=16,anchor='w')
lblcb.grid(row=2,column=2)
txtcb=Entry(f1,font=("arial",16,"bold"),textvariable=Cheese_burger,bd=10,insertwidth=4,bg="powder blue")
txtcb.grid(row=2,column=3)
#****************************** BUTONLAR************
btntotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("arial",20,"bold"),width=10,text="Total",bg="red",command=Ref)
btntotal.grid(row=10,column=1)

btnreset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("arial",20,"bold"),width=10,text="Reset",bg="red",command=Reset)
btnreset.grid(row=10,column=2)

btnrexit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("arial",20,"bold"),width=10,text="EXİT",bg="red",command=Exit)
btnrexit.grid(row=10,column=3)
















pencere.mainloop()
