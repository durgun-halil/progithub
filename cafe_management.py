from pickle import FRAME
from ssl import PEM_cert_to_DER_cert
from tkinter import*
import tkinter as tk
from turtle import pen, st, width
pencere=Tk()
pencere.geometry("1050x590")
pencere.title("MENÜ")
pencere.resizable(False,False)
Label(text="MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()# MANAGEMENT YAZISININ ÖZELLİKLERİNİ BELİRTTK

#MENÜ KISMI
menu=Frame(pencere,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=310,height=370)# ALAN BELİRTTİK
menu.place(x=10,y=118)

Label(menu,text="MENÜ",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="pizza...........100₺",fg="black",bg="lightgreen").place(x=10,y=80)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="cay...........10₺",fg="black",bg="lightgreen").place(x=10,y=110)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="kahve...........15₺",fg="black",bg="lightgreen").place(x=10,y=140)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="pasta...........30₺",fg="black",bg="lightgreen").place(x=10,y=170)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="hamburger.......100₺",fg="black",bg="lightgreen").place(x=10,y=200)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="doner...........25₺",fg="black",bg="lightgreen").place(x=10,y=230)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="patates...........20₺",fg="black",bg="lightgreen").place(x=10,y=260)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="corba...........20₺",fg="black",bg="lightgreen").place(x=10,y=290)
Label(menu,font=("Lucia Calligraphy",15,'bold'),text="kola...........18₺",fg="black",bg="lightgreen").place(x=10,y=320)
#****************************(((((( ENTRY WORK ))))))*************************************************************
siparis=Frame(pencere,bd=5,width=370,height=360,relief=RAISED)
siparis.pack()

pizza=StringVar()
cay=StringVar()
kahve=StringVar()
hamburger=StringVar()
doner=StringVar()
patates=StringVar()
corba=StringVar()
kola=StringVar()
pasta=StringVar()
toplam=StringVar()
total_bill=StringVar()

# sipariş isimleri
pizzalabel=Label(siparis,font=("aria",20,"bold"),text="Pizza",width=12,fg="blue4")
pizzalabel.grid(row=1,column=0)

caylabel=Label(siparis,font=("aria",20,"bold"),text="cay",width=12,fg="blue4")
caylabel.grid(row=2,column=0)

kahvelabel=Label(siparis,font=("aria",20,"bold"),text="kahve",width=12,fg="blue4")
kahvelabel.grid(row=3,column=0)

pastalabel=Label(siparis,font=("aria",20,"bold"),text="pasta",width=12,fg="blue4")
pastalabel.grid(row=4,column=0)

hamburgerlabel=Label(siparis,font=("aria",20,"bold"),text="hamburger",width=12,fg="blue4")
hamburgerlabel.grid(row=5,column=0)

donerlabel=Label(siparis,font=("aria",20,"bold"),text="doner",width=12,fg="blue4")
donerlabel.grid(row=6,column=0)


patateslabel=Label(siparis,font=("aria",20,"bold"),text="patates",width=12,fg="blue4")
patateslabel.grid(row=7,column=0)

corbalabel=Label(siparis,font=("aria",20,"bold"),text="corba",width=12,fg="blue4")
corbalabel.grid(row=8,column=0)

kolalabel=Label(siparis,font=("aria",20,"bold"),text="kola",width=12,fg="blue4")
kolalabel.grid(row=9,column=0)

# SAĞ TARAF fatura
fatura=Frame(pencere,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
fatura.place(x=690,y=118)

f1=Label(fatura,text="HESAP",font=("calibri",22),bg="lightyellow")
f1.place(x=100,y=10)


#SİPARİŞ GİRİŞLERİ ENTRY

pizzagiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=pizza,bd=6,width=8,bg="lightpink")
pizzagiriş.grid(row=1,column=1)

caygiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=cay,bd=6,width=8,bg="lightpink")
caygiriş.grid(row=2,column=1)

kahvegiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=kahve,bd=6,width=8,bg="lightpink")
kahvegiriş.grid(row=3,column=1)

pastagiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=pasta,bd=6,width=8,bg="lightpink")
pastagiriş.grid(row=4,column=1)

hamburgergiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=hamburger,bd=6,width=8,bg="lightpink")
hamburgergiriş.grid(row=5,column=1)

donergiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=doner,bd=6,width=8,bg="lightpink")
donergiriş.grid(row=6,column=1)

patatesgiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=patates,bd=6,width=8,bg="lightpink")
patatesgiriş.grid(row=7,column=1)

corbagiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=corba,bd=6,width=8,bg="lightpink")
corbagiriş.grid(row=8,column=1)

kolagiriş=Entry(siparis,font=("aria",20,"bold"),textvariable=kola,bd=6,width=8,bg="lightpink")
kolagiriş.grid(row=9,column=1)

#fonksiyonlar
def reset():
    pizzagiriş.delete(0,tk.END)
    caygiriş.delete(0,tk.END)
    kahvegiriş.delete(0,tk.END)
    pastagiriş.delete(0,tk.END)
    hamburgergiriş.delete(0,tk.END)
    donergiriş.delete(0,tk.END)
    patatesgiriş.delete(0,tk.END)
    corbagiriş.delete(0,tk.END)
    kolagiriş.delete(0,tk.END)

def toplam1():
    try:a1=int(pizza.get())
    except:a1=0

    try:a2=int(cay.get())
    except:a=0

    try:a3=int(kahve.get())
    except:a3=0

    try:a4=int(pasta.get())
    except:a4=0

    try:a5=int(hamburger.get())
    except:a5=0

    try:a7=int(doner.get())
    except:a7=0

    try:a8=int(patates.get())
    except:a8=0

    try:a9=int(corba.get())
    except:a9=0

    try:a10=int(kola.get())
    except:a1=0

    lbltoplam=Label(f1,font=("aria",20,"bold"),text="toplam tutar",width=16,fg="lightyellow",bg="black")
    lbltoplam.place(x=0,y=50)

    entry_total=Entry(siparis,font=("aria",20,"bold"),textvariable=toplam,width=15,fg="lightgreen",bd=6)
    entry_total.place(x=20,y=100)
    total_cost=c1+c2+c3+c4+c5+c6+c7+c8+c9
    string_fatura="₺",str('%2.f'%total_cost)
    toplam.get(string_fatura)

# hesaplalama
    c1=a1*100
    c2=a2*10
    c3=a3*15
    c4=a4*30
    c5=a5*100
    c6=a7*25
    c7=a8*20
    c8=a9*20
    c9=a10*18



#BUTON
btn_reset=Button(siparis,bd=3,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="RESET",command=reset)
btn_reset.grid(row=10,column=1)

btn_toplam=Button(siparis,bd=3,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="TOPLAM",command=toplam1)
btn_toplam.grid(row=10,column=2)


pencere.mainloop()