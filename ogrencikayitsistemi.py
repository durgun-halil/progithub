from cgitb import text
import tkinter as tk
from tkinter import Y, Label, StringVar, Tk, ttk
from turtle import pen

from numpy import pad
pencere=Tk()
pencere.title("UYGULAMA")
pencere.geometry("1350x700+0+0")
pencere.config(bg="white")#arka plan rengi
title_lbl=tk.Label(pencere,text="Öğrenci Sistemi",font=("arial",25,"bold"),border=12,relief=tk.GROOVE,bg="red",fg="pink")
title_lbl.pack(side=tk.TOP,fill=tk.X)
datail_frame=tk.LabelFrame(pencere,text="giriş frame",font=("arial",25,"bold"),bg="red",fg="pink")
datail_frame.place(x=20,y=80,width=420,height=560)
data_frame=tk.Frame(pencere,bd=12,bg="red",relief=tk.GROOVE)
data_frame.place(x=460,y=80,width=810,height=575)


# string var

rool_no=StringVar()
Name=StringVar()
Class=StringVar()
Section=StringVar()
Contac=StringVar()
Father=StringVar()
Adress=StringVar()
Gender=StringVar()
Dob=StringVar()
search_by=StringVar()













     
      # entry

roolno_lbl=tk.Label(datail_frame,text="school ID",font=("arial",17),bg="red",fg="white")   
roolno_lbl.grid(row=0,column=0,padx=2,pady=2)
roolno_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=rool_no)
roolno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(datail_frame,text="Name",font=("arial",17),bg="red",fg="white")
name_lbl.grid(row=1,column=0,padx=2,pady=2)
name_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

class_lbl=tk.Label(datail_frame,text="Class",font=("arial",17),bg="red",fg="white")
class_lbl.grid(row=2,column=0,padx=2,pady=2)
class_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Class)
class_ent.grid(row=2,column=1,padx=2,pady=2)


section_lbl=tk.Label(datail_frame,text="Section",font=("arial",17),bg="red",fg="white")
section_lbl.grid(row=3,column=0,padx=2,pady=2)
section_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Section)
section_ent.grid(row=3,column=1,padx=2,pady=2)

contac_lbl=tk.Label(datail_frame,text="Contac",font=("arial",17),bg="red",fg="white")
contac_lbl.grid(row=4,column=0,padx=2,pady=2)
contac_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Contac)
contac_ent.grid(row=4,column=1,padx=2,pady=2)


father_lbl=tk.Label(datail_frame,text="Father",font=("arial",17),bg="red",fg="white")
father_lbl.grid(row=5,column=0,padx=2,pady=2)
father_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Father)
father_ent.grid(row=5,column=1,padx=2,pady=2)

father_lbl=tk.Label(datail_frame,text="Adress",font=("arial",17),bg="red",fg="white")
father_lbl.grid(row=6,column=0,padx=2,pady=2)
father_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Adress)
father_ent.grid(row=6,column=1,padx=2,pady=2)


gender_lbl=tk.Label(datail_frame,text="Gender",font=("arial",17),bg="red",fg="white")
gender_lbl.grid(row=7,column=0,padx=2,pady=2)
gender_ent=ttk.Combobox(datail_frame,font=("arial",17),textvariable=Gender)
gender_ent['values']=("kız","erkek")
gender_ent.grid(row=7,column=1,padx=2,pady=2)


dob_lbl=tk.Label(datail_frame,text="e-mail",font=("arial",17),bg="red",fg="white",border=1)
dob_lbl.grid(row=8,column=0,padx=2,pady=2)
dob_ent=tk.Entry(datail_frame,bd=7,font=("arial",17),textvariable=Dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)


# BUTONLARRRRRRR********************//////////////////////

btn_frame=tk.Frame(datail_frame,bg="red",bd=10,relief=tk.GROOVE)
btn_frame.place(x=20,y=410,width=360,height=100)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15)
add_btn.grid(row=0,column=0,padx=2,pady=2)

updata_btn=tk.Button(btn_frame,bg="lightgrey",text="updata",bd=7,font=("Arial",13),width=15)
updata_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn=tk.Button(btn_frame,bg="lightgrey",text="delete",bd=7,font=("Arial",13),width=15)
delete_btn.grid(row=1,column=0,padx=3,pady=2)

clear_btn=tk.Button(btn_frame,bg="lightgrey",text="clear",bd=7,font=("Arial",13),width=15)
clear_btn.grid(row=1,column=1,padx=3,pady=2)

##SEARCH**********//////////////------------/////
search_frame=tk.Frame(data_frame,bg="red",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)
searc_lbl=tk.Label(search_frame,text="Search",bg="red",font=("arial",14))
searc_lbl.grid(row=0,column=0,padx=2,pady=2)

search_in=ttk.Combobox(search_frame,font=("arial",14),state="readonly",textvariable=search_by)
search_in["values"]=("school ID", "Name", "Class", "Section","Contac", "Father", "Adress", "Gender", "e-mail")
search_in.grid(row=0,column=1,padx=12,pady=2)

searc_btn=tk.Button(search_frame,text="Search",font=("arial",13),bd=9,width=14,bg="lightgrey")
searc_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="Show all",font=("arial",13),bd=9,width=14,bg="lightgrey")
showall_btn.grid(row=0,column=3,padx=12,pady=2)

#**************** DATABASE FRAME
main_frame=tk.Frame(data_frame,bg="red",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll= tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll= tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)


student_table=ttk.Treeview(main_frame,columns=("school ID", "Name", "Class", "Section","Contac", "Father",  "Gender", "e-mail","Adress"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.pack(fill=tk.BOTH,expand=True)

student_table.heading("school ID",text="school ID")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("Contac",text="Contac")
student_table.heading("Father",text="Father")
student_table.heading("Gender",text="Gender")
student_table.heading("e-mail",text="e-mail")
student_table.heading("Adress",text="Adress")

student_table['show']='headings'

student_table.column("school ID",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contac",width=100)
student_table.column("Father",width=100)
student_table.column("Gender",width=100)
student_table.column("e-mail",width=100)
student_table.column("Adress",width=150)


student_table.pack(fill=tk.BOTH,expand=True)


















pencere.mainloop() 