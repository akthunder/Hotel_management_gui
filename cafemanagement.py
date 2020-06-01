from tkinter import *
import random
import time;
import sqlite3

win=Tk()
win.geometry("1400x700")

win.title("This is cafe management system")
f1=Frame(win, width=1400 ,height=100, bd=14, relief="raise")
f1.pack(side=TOP)
label=Label(f1, text="Cafe Management Systems", font=("arial","40","bold"),fg="black")
label.place(x=250,y=0)
f2=Frame(win, width=900 ,height=600, relief="raise")
f2.pack(side=LEFT)
f3=Frame(win, width=470 ,height=600, bd=8, relief="raise")
f3.pack(side=RIGHT)

# ON FRAME F2 CODING......................

f4=Frame(f2, width=450, height=450 , bd=10, relief="raise")
f4.place(x=0,y=0)
f5=Frame(f2, width=450, height=450 , bd=10, relief="raise")
f5.place(x=450,y=0)
f6=Frame(f2, width=450, height=150 , bd=8, relief="raise")
f6.place(x=0,y=450)
f7=Frame(f2, width=450, height=150 , bd=8, relief="raise")
f7.place(x=450,y=450)

#Here are the all variabels declaration....................
vale_var=IntVar()
capp_var=IntVar()
african_var=IntVar()
american_var=IntVar()
iced_var=IntVar()
coff_var=IntVar()
red_var=IntVar()
black_var=IntVar()
lagos_var=IntVar()
queen_var=IntVar()
cod_var=StringVar()
cok_var=StringVar()
serv_var=StringVar()
paid_var=StringVar()
sub_var=IntVar()
tot_var=IntVar()

# here are the labels ....................................
label_list=["vale coffee","Cappuccino","African coffee","American coffee","Iced cappuccino"]
f4_labelposition=30
for i in label_list:
    f4_label=Label(f4,text=i, font=("ariel","20","bold"))
    f4_label.place(x=10,y=f4_labelposition)
    f4_labelposition+=70

vale_entry=Entry(f4, width="10",font="bold",bd="10",textvariable=vale_var,justify="left")
vale_entry.place(x=315,y=30)

capp_entry=Entry(f4,width="10",font="bold",bd="10",textvariable=capp_var,justify="left")
capp_entry.place(x=315,y=100)

african_entry=Entry(f4,width="10",font="bold",bd="10",textvariable=african_var,justify="left")
african_entry.place(x=315,y=170)

american_entry=Entry(f4,width="10",font="bold",bd="10",textvariable=american_var,justify="left")
american_entry.place(x=315,y=240)

iced_entry=Entry(f4,width="10",font="bold",bd="10",textvariable=iced_var,justify="left")
iced_entry.place(x=315,y=310)

list2=["Coffee cake","Red valvet cake","Black forest cake","Lagos chocolae cake","Queen chocolate cake"]

f5_labelposition=30
for j in list2:
    f5_label=Label(f5,text=j, font=("ariel","20","bold"))
    f5_label.place(x=10,y=f5_labelposition)
    f5_labelposition+=70


coff_entry=Entry(f5,width="10",font="bold",bd="10",textvariable=coff_var,justify="left")
coff_entry.place(x=315,y=30)

red_entry=Entry(f5,width="10",font="bold",bd="10",textvariable=red_var,justify="left")
red_entry.place(x=315,y=100)

black_entry=Entry(f5,width="10",font="bold",bd="10",textvariable=black_var,justify="left")
black_entry.place(x=315,y=170)

lagos_entry=Entry(f5,width="10",font="bold",bd="10",textvariable=lagos_var,justify="left")
lagos_entry.place(x=315,y=240)

queen_entry=Entry(f5,width="10",font="bold",bd="10",textvariable=queen_var,justify="left")
queen_entry.place(x=315,y=310)

# f6 Label are  here................

f6_label=["Cost of Drinks","Cost of cakes","Service charge"]
f6_labelposition=5
for i in f6_label:
    labels=Label(f6, text=i, font=("ariel","15","bold"))
    labels.place(x=10,y=f6_labelposition)
    f6_labelposition+=40

cod_entry=Entry(f6, width="10",font="bold",bd="10",textvariable=cod_var,justify="left")
cod_entry.place(x=315,y=5)
cok_entry=Entry(f6, width="10",font="bold",bd="10",textvariable=cok_var,justify="left")
cok_entry.place(x=315,y=45)
serv_entry=Entry(f6, width="10",font="bold",bd="10",textvariable=serv_var,justify="left")
serv_entry.place(x=315,y=85)

# Here are the cost  declaration for the drinks and cakes..........
cod_var.set("30/piece")
cok_var.set("50/piece")
serv_var.set("1%")
paid_var.set("2%")

f7_label=["Paid Tax","Sub Total","Total Cost"]
f7_labelposition=5
for k in f7_label:
    f7_labels=Label(f7, text=k, font=("ariel","15","bold"))
    f7_labels.place(x=10,y=f7_labelposition)
    f7_labelposition+=40
    
paid_entry=Entry(f7,width="10",font="bold",bd="10",textvariable=paid_var,justify="left")
paid_entry.place(x=315,y=5)
sub_entry=Entry(f7,width="10",font="bold",bd="10",textvariable=sub_var,justify="left")
sub_entry.place(x=315,y=45)
tot_entry=Entry(f7,width="10",font="bold",bd="10",textvariable=tot_var,justify="left")
tot_entry.place(x=315,y=85)
f3_yspace=10
for i in label_list:
    f3_labels=Label(f3, text=i, font=("ariel","20","bold"))
    f3_labels.place(x=5,y=f3_yspace)
    f3_yspace+=50
f3_space=260
for i in list2:
    f3_label=Label(f3, text=i, font=("ariel","20","bold"))
    f3_label.place(x=5,y=f3_space)
    f3_space+=50

# All the value holding variables for the f3's entry boxes.............

f3_vale_var=IntVar()
f3_capp_var=IntVar()
f3_african_var=IntVar()
f3_american_var=IntVar()
f3_iced_var=IntVar()
f3_coff_var=IntVar()
f3_red_var=IntVar()
f3_black_var=IntVar()
f3_lagos_var=IntVar()
f3_queen_var=IntVar()

# All the entry boxes of frame f3...............

f3_vale=Entry(f3,width="10",font="bold",textvariable=f3_vale_var, bd="5")
f3_vale.place(x=315,y=10)

f3_capp=Entry(f3, width="10",font="bold",textvariable=f3_capp_var, bd="5")
f3_capp.place(x=315,y=60)

f3_african=Entry(f3,width="10",font="bold",textvariable=f3_african_var, bd="5")
f3_african.place(x=315,y=110)

f3_american=Entry(f3,width="10",font="bold",textvariable=f3_american_var, bd="5")
f3_american.place(x=315,y=160)

f3_iced=Entry(f3, width="10",font="bold",textvariable=f3_iced_var,bd="5")
f3_iced.place(x=315,y=210)

f3_coff=Entry(f3, width="10",font="bold",textvariable=f3_coff_var, bd="5")
f3_coff.place(x=315,y=260)

f3_red=Entry(f3,width="10",font="bold",textvariable=f3_red_var, bd="5")
f3_red.place(x=315,y=310)

f3_black=Entry(f3,width="10",font="bold",textvariable=f3_black_var, bd="5")
f3_black.place(x=315,y=360)

f3_lagos=Entry(f3,width="10",font="bold",textvariable=f3_lagos_var, bd="5")
f3_lagos.place(x=315,y=410)

f3_queen=Entry(f3,width="10",font="bold",textvariable=f3_queen_var, bd="5")
f3_queen.place(x=315,y=460)
# here are the entered values...............
def total():
    print("Total function is called")
    vale_value=vale_var.get()
    capp_value=capp_var.get()
    african_value=african_var.get()
    american_value=american_var.get()
    coff_value=coff_var.get()
    iced_value=iced_var.get()
    red_value=red_var.get()
    black_value=black_var.get()
    lagos_value=lagos_var.get()
    queen_value=queen_var.get()
    # Frame f3's value ................after call total function.............
    f3_vale_var.set(vale_value)
    f3_capp_var.set(capp_value)
    f3_african_var.set(african_value)
    f3_american_var.set(american_value)
    f3_iced_var.set(iced_value)
    f3_coff_var.set(coff_value)
    f3_red_var.set(red_value)
    f3_black_var.set(black_value)
    f3_lagos_var.set(lagos_value)
    f3_queen_var.set(queen_value) 
    if vale_value:
        vale=vale_value*30
    else:
        vale=vale_value
    if capp_value:
        capp=(capp_value*30)+vale
    else:
        capp=capp_value+vale
    if african_value:
        african=(african_value*30)+capp
    else:
        african=african_value+capp
    if american_value:
        american=(american_value*30)+african
    else:
        american=american_value+african
    if iced_value:
        iced=(iced_value*30)+american
    else:
        iced=iced_value+american
    if coff_value:
        coff=(coff_value*50)+iced
    else:
        coff=coff_value+iced
    if red_value:
        red=(red_value*50)+coff
    else:
        red=red_value+coff
    if black_value:
        black=(black_value*50)+red
    else:
        black=black_value+red
    if lagos_value:
        lagos=(lagos_value*50)+black
    else:
        lagos=lagos_value+black
    if queen_value:
        queen=(queen_value*50)+lagos
        sub_var.set(queen)
    else:
        queen=queen_value+lagos
        sub_var.set(queen)
    serviceNpaid_charge=(queen*3)/100
    tot_var.set(serviceNpaid_charge+queen)
    
    # database connection ............
    con = sqlite3.connect("akthunder.db")
    cursor = con.cursor()
    cursor.execute('insert into info3(vale,capp,african,american,iced,coff,red,black,lagos,queen) values(?,?,?,?,?,?,?,?,?,?)',(vale_value,capp_value,african_value,american_value,iced_value,coff_value,red_value,black_value,lagos_value,queen_value))
    con.commit()
    con.close()
        
        
def clear():
    # here are the setted values.............
    vale_var.set(0)
    capp_var.set(0)
    african_var.set(0)
    american_var.set(0)
    iced_var.set(0)
    coff_var.set(0)
    red_var.set(0)
    black_var.set(0)
    lagos_var.set(0)
    queen_var.set(0)   
    sub_var.set(0)
    tot_var.set(0) 
    # All values of frame f3 deleting here................
    f3_vale_var.set(0)
    f3_capp_var.set(0)
    f3_african_var.set(0)
    f3_american_var.set(0)
    f3_iced_var.set(0)
    f3_coff_var.set(0)
    f3_red_var.set(0)
    f3_black_var.set(0)
    f3_lagos_var.set(0)
    f3_queen_var.set(0)
    
def quit():
    exit(0)

tot_button=Button(f3, width="10" ,bd="5",fg="green", text="Total",font=("ariel","15","bold"), command=lambda:total())
tot_button.place(x=5,y=500)

clear_button=Button(f3, width="10" ,bd="5",fg="brown", text="Clear",font=("ariel","15","bold"), command=lambda:clear())
clear_button.place(x=150,y=500)

quit_button=Button(f3, width="10" ,bd="5",fg="red", text="Quit",font=("ariel","15","bold"), command=lambda:quit())
quit_button.place(x=300,y=500)

win.mainloop()