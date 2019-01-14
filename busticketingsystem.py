from Tkinter import *
import sqlite3
from tkMessageBox import *
con=sqlite3.connect('database')
cur=con.cursor()
c=0
cur.execute("create table if not exists pasbus(id integer ,pname varchar(20),age number,gender char(10),mobile_no number,boarding_point char(10),destination_point char(10),doj number)")
def intro():
    splash=Tk()
    splash.title('ABOUT THE DEVELOPER')
    splash.state('zoomed')
    icon1=PhotoImage(file="spl.gif")
    l2=Label(splash,image=icon1)
    l2.pack()            
    Label(splash,text='WAIT FOR 5 SECONDS.......',font='times 22 bold',fg="white",bg='black').place(relx=0.7,rely=0.85)

    def dest():
        splash.destroy()
    splash.after(5000,dest)
    splash.mainloop()
intro()
app=Tk()
app.state("zoomed")
icon=PhotoImage(file="test.gif")
label1=Label(app,image=icon)
label1.pack()
Label(app, text="WELCOME TO BUS TICKET BOOKING SYSTEM", bg="black", fg="white", font=('times 30 bold'),relief='flat', height=2, width=50).place(relx=0.0,rely=0.0)
########################################################...................BOOKING...............###############################################################################################################
def book():
    root=Toplevel()
    root.title("BOOK TICKET")
    root.state("zoomed")
    root.configure(background='aliceblue')
    root.geometry("1000x700")
    #....f1.............................................................................................................................................
    f1=Frame(root,height=137,width=500,bd=4,relief="raised",bg='black')
    f1.place(relx=0.135,rely=0)
    Label(f1,text='PASSENGER DETAILS',font='times 20 bold underline',bg='black',fg='white').place(relx=0.25,rely=0.65)

    #.........root1...........................................................................................................................
    root1=Frame(root,height=700,width=500,bd=4,relief="raised")
    root1.place(relx=0.135,rely=0.19)
    #...............
    Label(root1,text='Enter name of passenger',font='times 16').place(relx=0.02,rely=0.19)
    e1=Entry(root1,width=22,bd=2,justify="right",font='times 13')
    e1.place(relx=0.53,rely=0.19)
    #..............
    Label(root1,text='Select your Gender:',font='times 16').place(relx=0.02,rely=0.27)
    v1=IntVar()
    r=Radiobutton(root1,text='Male',font='times 13',variable=v1,value=1)
    r.place(relx=0.53,rely=0.27)
    r1=Radiobutton(root1,text='Female',font='times 13',variable=v1,value=2)
    r1.place(relx=0.66,rely=0.27)
    r2=Radiobutton(root1,text='Third',font='times 13',variable=v1,value=3)
    r2.place(relx=0.81,rely=0.27)
    #.................
    Label(root1,text='Enter age of passenger',font='times 16').place(relx=0.02,rely=0.35)
    e2=Entry(root1,width=16,bd=2,justify="right",font='times 13')
    e2.place(relx=0.53,rely=0.35)
    #............................
    Label(root1,text='Enter your mobile no:',font='times 16').place(relx=0.02,rely=0.43)
    e3=Entry(root1,width=16,bd=2,justify="right",font='times 13')
    e3.place(relx=0.53,rely=0.43)
    #....f2...................................................................................................................................................
    f2=Frame(root,height=137,width=500,bd=4,bg='black',relief="raised")
    f2.place(relx=0.5,rely=0)
    Label(f2,text='JOURNEY DETAILS',font='times 20 bold underline',bg='black',fg='white').place(relx=0.25,rely=0.65)

    #......................................root2...............................................................................................................
    root2=Frame(root,height=700,width=500,bd=4,relief="raised")
    root2.place(relx=0.5,rely=0.19)
    #..................................
    Label(root2,text='Select the Boarding point',font='times 16 ').place(relx=0.02,rely=0.19)
    var1 = StringVar(root)
    var1.set("Choose station")
    def grab_and_assign(event):
        option = var1.get()
        Label(root2, text=option,font='times 15').place(relx=0.7,rely=0.19)
    OptionMenu(root2, var1,  "Satna", "Katni", "Ajmer", "Guna",command=grab_and_assign).place(relx=0.53,rely=0.19)
    #.................................
    Label(root2,text='Select the Destination point',font='times 16 ').place(relx=0.02,rely=0.27)
    var2 = StringVar(root)
    var2.set("Choose station")
    def grab_and_assign1(event):
        option = var2.get()
        Label(root2, text=option,font='times 15').place(relx=0.7,rely=0.27)
    OptionMenu(root2, var2,  "Satna", "Katni", "Ajmer", "Guna",command=grab_and_assign1).place(relx=0.53,rely=0.27)
    Label(root2,text='Enter Valid date of Journey',font='times 16').place(relx=0.02,rely=0.35)
    Label(root2,text='(dd/mm/yyyy)',font='times 16 bold').place(relx=0.15,rely=0.38)
    e4=Entry(root2,width=16,bd=2,justify="right",font='times 13')
    e4.place(relx=0.53,rely=0.35)
    def f():
        global c
        c=c+1
        li=[(c,str(e1.get()),str(e2.get()),str(v1.get()),str(e3.get()),str(var1.get()),str(var2.get()),str(e4.get()))]
        cur.executemany("insert into pasbus values(?,?,?,?,?,?,?,?)",li)
        con.commit()
        cur.execute('select * from pasbus')
        l=cur.fetchall()
        si=len(l)
        f=Tk()
        f.title("BOOKED")
        f.configure(background='aliceblue')
        f.geometry("1000x700")
        Label(f,text='Congragtulation, your ticket is booked...!',font='times 20',bg='aliceblue').place(relx=0.25,rely=0.05)
        Label(f,text='--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',font='times 20 bold',bg='aliceblue').place(relx=0,rely=0.1)
        Label(f,text='Your ticket id is: '+"SRC"+ str(l[si-1][0])+str(l[si-1][0]+1)+"B1",font='times 16',bg='aliceblue').place(relx=0.02,rely=0.24)
        Label(f,text='Your UNIQUE id is: '+ str(l[si-1][0]),font='times 16',bg='aliceblue').place(relx=0.3,rely=0.24)
        
        Label(f,text='Name of passenger: '+str(l[si-1][1]),font='times 16',bg='aliceblue').place(relx=0.02,rely=0.34)
        if str(l[si-1][3])=="1":
            s1="Male"
        elif str(l[si-1][3])=="2":
            s1="Female"
        else:
            s1="Others"
        Label(f,text='Gender: '+s1,font='times 16',bg='aliceblue').place(relx=0.60,rely=0.34)
        Label(f,text='Age: '+str(l[si-1][2]),font='times 16',bg='aliceblue').place(relx=0.45,rely=0.34)
        Label(f,text='Boarding Point: '+str(l[si-1][5]),font='times 16',bg='aliceblue').place(relx=0.02,rely=0.44)
        Label(f,text='Destination Point: '+str(l[si-1][6]),font='times 16',bg='aliceblue').place(relx=0.38,rely=0.44)
        Label(f,text='Date of Journey: '+str(l[si-1][7]),font='times 16',bg='aliceblue').place(relx=0.7,rely=0.44)
        Button(f,text='.......................Contact to conductor with your ticket id for your seat no..........................',font='times 20 bold',bg='black',fg='white').place(relx=0,rely=0.7)
        Button(f,text='OK',font='times 20',relief='raised',command=lambda:f.destroy()).place(relx=0.45,rely=0.8)
        f.mainloop()
    def error():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or (v1.get())==0:
            showerror("error","fields can't be left empty")
        elif len(e3.get())!=10:
            showerror("error","incorrect mobile no")
        else:
            f()
    Button(root2,text="BOOK",font='times 16 bold',relief='raised',bd=3,command=error).place(relx=0.6,rely=0.6)
    
    Button(root2,text="EXIT",command=lambda:root.destroy(),font='times 16 bold',relief='raised',bd=3).place(relx=0.6,rely=0.7)
    root.mainloop()
################################################ ..............STATUS.....#############################################################
def status():
    root4=Tk()
    root4.title("CHECK STATUS")
    root4.state("zoomed")
    root4.configure(background='aliceblue')

    #............f5....................
    f5=Frame(root4,height=137,width=500,bd=4,relief="raised",bg='black')
    f5.place(relx=0.34,rely=0)
    Label(f5,text='CHECK STATUS',font='times 30 bold',relief='raised',bd=2,bg='black',fg='white').place(relx=0.17,rely=0.6)
    #...........f6.....................
    f6=Frame(root4,height=500,width=500,bd=4,relief="raised")
    f6.place(relx=0.34,rely=0.19)
    Label(f6,text='PASSENGER UNIQUE ID',font='times 20 bold').place(relx=0.17,rely=0.1)
    e5=Entry(f6,textvariable=IntVar,bd=2,justify="right",font='times 16')
    e5.place(relx=0.269,rely=0.2)
        
    def s():
        #print e5.get()
        s=Tk()
        s.title("STATUS")
        s.configure(background='aliceblue')
        s.geometry("1000x700")
        tiid=[(e5.get())]
        cur.execute("select * from pasbus where id=(?)",tiid)
        ti=cur.fetchall()
        si=len(ti)
        Label(s,text='TICKET STATUS: CONFIRMED..!',font='times 20',bg='aliceblue').place(relx=0.25,rely=0.05)
        Label(s,text='--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',font='times 20 bold',bg='aliceblue').place(relx=0,rely=0.1)
        Label(s,text='Your ticket id is:- '+"SRC"+ str(ti[si-1][0])+str(ti[si-1][0]+1)+"B1",font='times 16',bg='aliceblue').place(relx=0.02,rely=0.24)
        Label(s,text='Your unique id is:- '+ str(ti[si-1][0]),font='times 16',bg='aliceblue').place(relx=0.3,rely=0.24)
        Label(s,text='Name of passenger: '+str(ti[0][1]),font='times 16',bg='aliceblue').place(relx=0.02,rely=0.34)
        if str(ti[0][3])=="1":
            s1="Male"
        elif str(ti[0][3])=="2":
            s1="Female"
        else:
            s1="Others"
        
        Label(s,text='Gender: '+s1,font='times 16',bg='aliceblue').place(relx=0.60,rely=0.34)
        Label(s,text='Age: '+str(ti[0][2]),font='times 16',bg='aliceblue').place(relx=0.45,rely=0.34)
        Label(s,text='Boarding Point: '+str(ti[0][5]),font='times 16',bg='aliceblue').place(relx=0.02,rely=0.44)
        Label(s,text='Destination Point: '+str(ti[0][6]),font='times 16',bg='aliceblue').place(relx=0.38,rely=0.44)
        Label(s,text='Date of Journey: '+str(ti[0][7]),font='times 16',bg='aliceblue').place(relx=0.7,rely=0.44)
        Button(s,text='.......................Contact to conductor with your ticket id for your seat no..........................',font='times 20 bold',bg='black',fg='white').place(relx=0,rely=0.7)
        Button(s,text='OK',font='times 20',relief='raised',command=lambda:s.destroy()).place(relx=0.4,rely=0.8)
        s.mainloop()   
    def test():
        tiid=[(e5.get())]
        cur.execute("select * from pasbus where id=(?)",tiid)
        ti=cur.fetchall()
        if len(ti)==0:
            showerror('error','invalid id')
            
        else:
            s()
            
            
    Button(f6,text='SHOW',bd=2,font='times 16',command=test).place(relx=0.4,rely=0.3)
    Button(root4,text="EXIT",command=lambda:root4.destroy(),font='times 16 bold',relief='raised',bd=3).place(relx=0.6,rely=0.7)

    root4.mainloop()
#################################################..............cancel................################################################3
def cancel():
    root3=Tk()
    root3.title("CANCEL TICKET")
    root3.state("zoomed")
    root3.configure(background='aliceblue')

    #............f3....................
    f3=Frame(root3,height=137,width=500,bd=4,relief="raised",bg='black')
    f3.place(relx=0.34,rely=0)
    Label(f3,text='CANCEL TICKET',font='times 30 bold',relief='raised',bd=2,bg='black',fg='white').place(relx=0.17,rely=0.6)
    #...........f4.....................
    f4=Frame(root3,height=500,width=500,bd=4,relief="raised")
    f4.place(relx=0.34,rely=0.19)
    Label(f4,text='PASSENGER UNIQUE ID',font='times 20 bold').place(relx=0.17,rely=0.1)
    e6=Entry(f4,bd=2,justify="right",font='times 16')
    e6.place(relx=0.269,rely=0.2)
    def delete():
        l=[(e6.get())]
        cur.execute("delete from pasbus where id=(?)",l)
        con.commit()
        showinfo("deleted","deleted succesfully....!")
    def test1():
        tiid=[(e6.get())]
        cur.execute("select * from pasbus where id=(?)",tiid)
        ti=cur.fetchall()
        if len(ti)==0:
            showerror('error','invalid id')
            
        else:
            delete()
    
        
    Button(f4,text='CANCEL',bd=2,font='times 16',command=test1).place(relx=0.4,rely=0.3)
    Button(root3,text="EXIT",command=lambda:root3.destroy(),font='times 16 bold',relief='raised',bd=3).place(relx=0.6,rely=0.7)
    root3.mainloop()

#################################################################################################################################################################
Button(app,bg='blUE',fg='grey',text='CLICK TO BOOK TICKETS',width=30,height=2,font='times 20 bold',command=book).place(relx=0.65,rely=0.4)
Button(app,bg='MAROON',fg='grey',text='CLICK TO CHECK STATUS',width=30,height=2,font='times 20 bold',command=status).place(relx=0.65,rely=0.6)
Button(app,bg='blUE',fg='grey',text='CANCEL TICKETS',width=30,height=2,font='times 20 bold',command=cancel).place(relx=0.65,rely=0.8)
app.mainloop()
#####################...........BUGS..........################
#admin login
#showall button
#set mobile no to integer
#set calender
#show ticket fare
#
