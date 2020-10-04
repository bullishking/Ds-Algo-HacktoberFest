import tkinter
from tkinter import*
from tkinter import messagebox
import mysql.connector as ms
from PIL import ImageTk,Image
import time
import datetime
import random

h=2
w=300
db = ms.connect(host="localhost",user="root",password='dev1312',database='school_project')
cur = db.cursor()
screen1 = Tk()

   
class HoverButton(tkinter.Button):
    def __init__(self, master, **kw):
        tkinter.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def quit_screen():
    msg=messagebox.askquestion ('Exit Application','Are you sure you want to exit the application ?',icon = 'warning')
    if(msg=='yes'):
        screen1.destroy()
        quit()


def studentlogin():
    canvas2.destroy()
    l2.destroy()
    def login_verify():
        a=0
        cur.execute("select * from student")
        results=cur.fetchall()
        for row in results:
            if(username.get()==row[0]):
                a=1
                if(password.get()==row[5]):
                    global adm,name,cl,sec,phone,dob,email
                    adm=row[0]
                    name=row[1]
                    cl=row[2]
                    sec=row[3]
                    phone=row[4]
                    dob=row[5]
                    email=row[6]
                    std_login()

                    
                else:
                    messagebox.showerror("","Invalid Password")
          
        if(a==0):
            messagebox.showerror("","Invalid User ID")
                       
                      
    def reset():
        username.set('')
        password.set('')

    frame1=LabelFrame(screen1,width = 600 , height =400,bg='white').place(x=650,y=370)
    global username,password
    username = StringVar()
    password = StringVar()

    Label(frame1,text = "Student Login Panel" , width = 15 , height = 1,
          font = ("times new roman", 30) ,anchor=N,
           fg = "deepskyblue4",bg='white').place(x=800,y=395)
    
    Label(frame1, text = "User ID :",font = ("Calibri", 18),bg='white').place(x=700, y = 470)
    username_entry= Entry(frame1, textvariable = username,
                            width = "35",font = ("Calibri", 16),bg='grey70').place(x=700, y=520)
    Label(frame1, text = "Ex: 20012345",font = ("Calibri", 14),bg='white').place(x=1100, y = 515)
   
    Label(frame1, text="Password :",font = ("Calibri", 18),bg='white').place(x=700, y=570)   
    password_entry= Entry(frame1, textvariable = password,
                          show="*",width = "35",font = ("Calibri", 16),bg='grey70').place(x=700, y=615)
    Label(frame1, text = "Ex: 21-OCT-2003",font = ("Calibri", 14),bg='white').place(x=1100, y = 610)
    
    login=HoverButton(frame1,text = "Login", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=login_verify).place(x=750 , y=700)
    reset=HoverButton(frame1,text = "Reset", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=reset).place(x=1000 , y=700)



def stafflogin():
    canvas2.destroy()
    l2.destroy()
    def login_verify():
        a=0
        cur.execute("select * from staff")
        results=cur.fetchall()
        for row in results:
            if(username.get()==row[0]):
                a=1
                if(password.get()==row[4]):
                    global name,sub,email
                    name=row[1]
                    sub=row[2]
                    email=row[3]
                    staff_login()

                    
                else:
                    messagebox.showerror("","Invalid Password")
          
        if(a==0):
            messagebox.showerror("","Invalid User ID")
                 
                      
    def reset():
        username.set('')
        password.set('')

    frame1=LabelFrame(screen1,width = 600 , height =400,bg='white').place(x=650,y=370)
    global username,password
    username = StringVar()
    password = StringVar()

    Label(frame1,text = "Staff Login Panel" , width = 15 , height = 1,
          font = ("times new roman", 30) ,anchor=N,
           fg = "deepskyblue4",bg='white').place(x=800,y=395)
    
    Label(frame1, text = "User ID :",font = ("Calibri", 18),bg='white').place(x=700, y = 470)
    username_entry= Entry(frame1, textvariable = username,
                            width = "40",font = ("Calibri", 16),bg='grey70').place(x=700, y=520)
    
    Label(frame1, text="Password :",font = ("Calibri", 18),bg='white').place(x=700, y=570)   
    password_entry= Entry(frame1, textvariable = password,
                          show="*",width = "40",font = ("Calibri", 16),bg='grey70').place(x=700, y=615)
   
    login=HoverButton(frame1,text = "Login", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=login_verify).place(x=750 , y=700)
    reset=HoverButton(frame1,text = "Reset", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 15),command=reset).place(x=1000 , y=700)

def staff_login():
      
    
    username.set('')
    password.set('')

    screen2=Toplevel(screen1)
    screen2.attributes('-fullscreen',True)  
    screen2.title("School Mangement System")
    screen1.withdraw()
    Label(screen2,text = "DAV Public School, Pushpanjali Enclave" ,padx=290,pady=10, width = 50 , height = 100,
          font = ("times new roman", 45) ,anchor=NW,
          bg='deepskyblue4',fg = "white").place(x=0,y=0)
    Label(screen2,text = "Pitampura, Delhi, Delhi- 110034 , 27018261- 27010377" ,padx=290,pady=0, width = 30 , height = 5,
          font = ("times new roman", 15) ,anchor=NW,
          bg='deepskyblue4',fg = "white").place(x=0,y=82)
    
    Label(screen2,width = 1000 , height = 1, bg='white').place(x=0,y=120)
    Label(screen2,width =1 , height = 1000, bg='white').place(x=350,y=120)

    def profile():
        Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=200)
        Label(screen2,text = '_'*17,padx=25,pady=0, width = 16, height = 4,
              font = ("times new roman", 50) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=240)

        Label(screen2,text = name,padx=0,pady=10, width = 29, height = 0,
              font = ("times new roman", 30) ,anchor=N,
              bg='white',fg = "deepskyblue4").place(x=600,y=240)
        
        Label(screen2,text = 'Role :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=340)

        Label(screen2,text = 'Staff',padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=340)

        Label(screen2,text = 'Subject :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=390)

        Label(screen2,text =sub ,padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=390)

        Label(screen2,text = 'Email :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=440)

        Label(screen2,text = email,padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=440)

    profile()   


    
    def add_staff():
        def add():
            add='insert into staff values(%s,%s,%s,%s,%s)'
            data=(add_name.get(),add_userid.get(),add_password.get(),add_sub.get(),add_email.get())
            cur.execute(add,data)
            db.commit()
            add_name.set('')
            add_userid.set('')
            add_password.set('')
            add_email.set('')
            add_sub.set('')
        def reset():
            add_name.set('')
            add_userid.set('')
            add_password.set('')
            add_email.set('')
            add_sub.set('')

        global add_name,add_userid,add_password,add_sub,add_email
  
        add_name =StringVar()
        add_userid = StringVar()
        add_password = StringVar()
        add_email = StringVar()
        add_sub=StringVar()
        
        Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=300)
        Label(screen2,padx=25,pady=0, width = 16, height = 5,
          font = ("times new roman", 50) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=300)

        Label(screen2,text = 'Name :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=350)

        Label(screen2,text = 'User ID :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=400)

        Label(screen2,text = 'Password :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=450)

        Label(screen2,text = 'Subject :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=500)

        Label(screen2,text = 'Email :',padx=50,pady=0, width = 30, height = 1,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=550)

        name_entry= Entry(screen2, textvariable = add_name,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=350)
        userid_entry= Entry(screen2, textvariable = add_userid,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=400)
        password_entry= Entry(screen2, textvariable = add_password,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=450)
        sub_entry= Entry(screen2, textvariable = add_sub,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=500)
        email_entry= Entry(screen2, textvariable = add_email,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=550)

        b1=HoverButton(screen2,text = "Add", borderwidth=1,height = "1", width = "18",
               activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
               activeforeground='white',font = ("Calibri", 15),command=add).place(x=640 , y=615)

        b2=HoverButton(screen2,text = "Reset", borderwidth=1,height = "1", width = "18",
               activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
               activeforeground='white',font = ("Calibri", 15),command=reset).place(x=950 , y=615)
   
    def add_st():            
        def add():
            add='insert into student values(%s,%s,%s,%s,%s,%s,%s)'
            data=(add_adm.get(),add_stname.get(),add_cl.get(),add_sec.get(),add_phone.get(),add_dob.get(),add_email.get())
            cur.execute(add,data)
            db.commit()
            add_adm.set('')
            add_stname.set('')
            add_phone.set('')
            add_dob.set('')
            add_email.set('')
            add_cl.set('')
            add_sec.set('')
        def reset():
            add_adm.set('')
            add_stname.set('')
            add_phone.set('')
            add_dob.set('')
            add_email.set('')
            add_cl.set('')
            add_sec.set('')
        global add_adm,add_stname,add_phone,add_dob,add_email,add_cl,add_sec
        add_adm = StringVar()
        add_stname =StringVar()
        add_phone = StringVar()
        add_dob = StringVar()
        add_email = StringVar()
        add_cl=StringVar()
        add_sec=StringVar()
        
        Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=300)
        Label(screen2,padx=25,pady=0, width = 16, height = 6,
          font = ("times new roman", 50) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=300)

        Label(screen2,text = 'Admission No. :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=350)

        Label(screen2,text = 'Name :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=400)

        Label(screen2,text = 'Class :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=450)

        Label(screen2,text = 'Section :',padx=50,pady=0, width = 10, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=900,y=450)

        Label(screen2,text = 'Phone :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=500)

        Label(screen2,text = 'DOB :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=550)

        Label(screen2,text = 'Email :',padx=50,pady=0, width = 30, height = 1,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=600)

        adm_entry= Entry(screen2, textvariable = add_adm,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=350)

        name_entry= Entry(screen2, textvariable = add_stname,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=400)

        cl_entry= Entry(screen2, textvariable = add_cl,
                        width = "7",font = ("Calibri", 16),bg='grey70').place(x=750,y=455)

        sec_entry= Entry(screen2, textvariable = add_sec,
                        width = "7",font = ("Calibri", 16),bg='grey70').place(x=1070,y=455)

        
        phone_entry= Entry(screen2, textvariable = add_phone,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=500)

        dob_entry= Entry(screen2, textvariable = add_dob,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=550)

        email_entry= Entry(screen2, textvariable = add_email,
                        width = "20",font = ("Calibri", 16),bg='grey70').place(x=900, y=600)

        b1=HoverButton(screen2,text = "Add", borderwidth=1,height = "1", width = "18",
               activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
               activeforeground='white',font = ("Calibri", 15),command=add).place(x=640 , y=680)

        b2=HoverButton(screen2,text = "Reset", borderwidth=1,height = "1", width = "18",
               activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
               activeforeground='white',font = ("Calibri", 15),command=reset).place(x=950 , y=680)
    
    
    def add():
        
        Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=200) 
        R1 = Radiobutton(screen2, text="Staff", value=1,font = ("times new roman", 20),
                         bg="deepskyblue4",fg='white',activebackground="deepskyblue4",command=add_staff).place(x=600,y=230)
        
        R2 = Radiobutton(screen2, text="Student", value=1,font = ("times new roman", 20),
                         bg="deepskyblue4",fg='white',activebackground="deepskyblue4",command=add_st).place(x=950,y=230)
        add_staff()

        
    def existing():
        def update():

            cur.execute("select * from student")
            results=cur.fetchall()
            for row in results:
                if(up_stname.get()!=''):
                    string=(up_stname.get(),search1.get())
                    upd="update student set name=%s where admn=%s"
                    cur.execute(upd,string)
                    db.commit()

                if(up_cl.get()!=''):
                    string=(up_cl.get(),search1.get())
                    upd="update student set class=%s where admn=%s"
                    cur.execute(upd,string)
                    db.commit()

                if(up_sec.get()!=''):
                    string=(up_sec.get(),search1.get())
                    upd="update student set sec=%s where admn=%s"
                    cur.execute(upd,string)
                    db.commit()

                if(up_phone.get()!=''):
                    string=(up_phone.get(),search1.get())
                    upd="update student set phone=%s where admn=%s"
                    cur.execute(upd,string)
                    db.commit()

                if(up_dob.get()!=''):
                    string=(up_dob.get(),search1.get())
                    upd="update student set dob=%s where admn=%s"
                    cur.execute(upd,string)
                    db.commit()

                if(up_email.get()!=''):
                    string=(up_email.get(),search1.get())
                    upd="update student set email=%s where admn=%s"
                    cur.execute(upd,string)
                    db.commit()

            existing()
        
        def reset():
            up_adm.set('')
            up_stname.set('')
            up_phone.set('')
            up_dob.set('')
            up_email.set('')
            up_cl.set('')
            up_sec.set('')

        def delete():
            msg=messagebox.askquestion ('Delete Details','Are you sure you want to delete all the details ?',icon = 'warning')
            if(msg=='yes'):
                string=(search1.get(),)
                upd="delete from student where admn=%s"
                cur.execute(upd,string)
                db.commit()
                Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=200)

                Label(screen2 , width = 30 , height = 6,
          font = ("times new roman", 30) ,anchor=N,
           fg = "deepskyblue4",bg='white').place(x=600,y=350)
    
                Label(screen2,text = 'All the details have been \ndeleted successfully',width = 20, height = 3,
                  font = ("times new roman",35) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=720,y=420)

            
        global up_adm,up_stname,up_phone,up_dob,up_email,up_cl,up_sec
        flag=0
        up_adm = StringVar()
        up_stname =StringVar()
        up_phone = StringVar()
        up_dob = StringVar()
        up_email = StringVar()
        up_cl=StringVar()
        up_sec=StringVar()

        cur.execute("select * from student")
        results=cur.fetchall()
        for row in results:
            if(search1.get()==row[0]):
                
                global s_adm,s_name,s_cl,s_sec,s_phone,s_dob,s_email
                flag=1
                s_adm=row[0]
                s_name=row[1]
                s_cl=row[2]
                s_sec=row[3]
                s_phone=row[4]
                s_dob=row[5]
                s_email=row[6]
        

                Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=300)
                Label(screen2,padx=25,pady=0, width = 120, height = 40,
                  font = ("times new roman", 10) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=200)

                Label(screen2,text = 'Edit',padx=70,pady=0, width = 5, height = 2,
                  font = ("times new roman",30) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=800,y=220)

                Label(screen2,text = 'Admission No. :',padx=50,pady=0, width = 30, height = 2,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=300)

                Label(screen2,text = s_adm,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW,
                      bg='white',fg = "deepskyblue4").place(x=820,y=300)
                
                Label(screen2,text = 'Name :',padx=50,pady=0, width = 30, height = 2,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=350)

                Label(screen2,text = s_name,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW,
                      bg='white',fg = "deepskyblue4").place(x=820,y=350)
                
                Label(screen2,text = 'Class :',padx=50,pady=0, width = 30, height = 2,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=400)

                Label(screen2,text = s_cl,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW,
                      bg='white',fg = "deepskyblue4").place(x=820,y=400)
                
                Label(screen2,text = 'Section :',padx=50,pady=0, width = 10, height = 2,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=450)

                Label(screen2,text = s_sec,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW,
                      bg='white',fg = "deepskyblue4").place(x=820,  y=450)
                
                Label(screen2,text = 'Phone :',padx=50,pady=0, width = 30, height = 2,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=500)

                Label(screen2,text = s_phone,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW,
                      bg='white',fg = "deepskyblue4").place(x=820,y=500)
                
                Label(screen2,text = 'DOB :',padx=50,pady=0, width = 30, height = 2,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=550)

                Label(screen2,text = s_dob,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW,
                      bg='white',fg = "deepskyblue4").place(x=820,y=550)
                
                Label(screen2,text = 'Email :',padx=50,pady=0, width = 30, height = 1,
                  font = ("times new roman", 22) ,anchor=NW,
                  bg='white',fg = "deepskyblue4").place(x=500,y=600)

                Label(screen2,text = s_email,padx=0,pady=0, width = 29, height = 0,
                      font = ("times new roman", 22) ,anchor=NW ,
                      bg='white',fg = "deepskyblue4").place(x=820,y=600)
                
                name_entry= Entry(screen2, textvariable = up_stname,
                                width = "15",font = ("Calibri", 16),bg='grey70').place(x=1150, y=350)

                cl_entry= Entry(screen2, textvariable = up_cl,
                                width = "15",font = ("Calibri", 16),bg='grey70').place(x=1150,y=405)

                sec_entry= Entry(screen2, textvariable = up_sec,
                                width = "15",font = ("Calibri", 16),bg='grey70').place(x=1150,y=455)

                
                phone_entry= Entry(screen2, textvariable = up_phone,
                                width = "15",font = ("Calibri", 16),bg='grey70').place(x=1150, y=500)

                dob_entry= Entry(screen2, textvariable = up_dob,
                                width = "15",font = ("Calibri", 16),bg='grey70').place(x=1150, y=550)

                email_entry= Entry(screen2, textvariable = up_email,
                                width = "15",font = ("Calibri", 16),bg='grey70').place(x=1150, y=600)

                b1=HoverButton(screen2,text = "Update", borderwidth=1,height = "1", width = "18",
                       activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                       activeforeground='white',font = ("Calibri", 15),command=update).place(x=600 , y=680)
                
                b2=HoverButton(screen2,text = "Delete", borderwidth=1,height = "1", width = "18",
                       activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                       activeforeground='white',font = ("Calibri", 15),command=delete).place(x=850 , y=680)
        
                b2=HoverButton(screen2,text = "Reset", borderwidth=1,height = "1", width = "18",
                       activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                       activeforeground='white',font = ("Calibri", 15),command=reset).place(x=1100 , y=680)
        if(flag==0):
            messagebox.showerror("","Invalid Admission Number")

    def search():
        def reset():
            search1.set('')

        global search1
        search1 = StringVar()
        Label(screen2,width = 500 , height = 500, bg='deepskyblue4').place(x=500,y=150)

        Label(screen2,padx=25,pady=0, width = 200, height = 35,
          font = ("times new roman", 5) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=500,y=300)

        Label(screen2,text = 'Enter the Admission Number of the student :',padx=50,pady=0, width = 30, height = 2,
          font = ("times new roman", 22) ,anchor=NW,
          bg='white',fg = "deepskyblue4").place(x=600,y=350)
        search_entry= Entry(screen2, textvariable = search1,
                        width = "15",font = ("Calibri", 16),bg='grey70').place(x=820,y=400)

        b1=HoverButton(screen2,text = "Search", borderwidth=1,height = "1", width = "18",
               activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
               activeforeground='white',font = ("Calibri", 15),command=existing).place(x=660 , y=500)

        b2=HoverButton(screen2,text = "Reset", borderwidth=1,height = "1", width = "18",
               activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
               activeforeground='white',font = ("Calibri", 15),command=reset).place(x=970 , y=500)
        
    def logout():
        msg=messagebox.askquestion ('Logout','Are you sure you want to logout ?',icon = 'warning')
        if(msg=='yes'):
            
            screen2.withdraw()
            screen1.deiconify() 
            main_screen1()
            quit()


            

        
    b1=HoverButton(screen2,text = "Profile", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                   activeforeground='white',font = ("Calibri", 28),command=profile).place(x=0 , y=140)

    b2=HoverButton (screen2,text = "Add" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=add).place(x=0 , y=218)

    b3=HoverButton (screen2,text = "Search" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=search).place(x=0 , y=296)

    b4=HoverButton (screen2,text = "Logout" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=logout).place(x=0 ,y=374)
    

   
    screen2.mainloop()



def std_login():
      
    
    username.set('')
    password.set('')

    screen2=Tk()
    screen2.attributes('-fullscreen',True)  
    screen2.title("School Mangement System")
    screen1.withdraw()
    Label(screen2,text = "DAV Public School, Pushpanjali Enclave" ,padx=290,pady=10, width = 50 , height = 100,
          font = ("times new roman", 45) ,anchor=NW,
          bg='deepskyblue4',fg = "white").place(x=0,y=0)
    Label(screen2,text = "Pitampura, Delhi, Delhi- 110034 , 27018261- 27010377" ,padx=290,pady=0, width = 30 , height = 5,
          font = ("times new roman", 15) ,anchor=NW, 
          bg='deepskyblue4',fg = "white").place(x=0,y=82)
    
    Label(screen2,width = 1000 , height = 1, bg='white').place(x=0,y=120)
    Label(screen2,width =1 , height = 1000, bg='white').place(x=350,y=120)

    def profile():
        Label(screen2,width = 500 , height = 300, bg='deepskyblue4').place(x=400,y=200)
        Label(screen2,text = '_'*17,padx=25,pady=0, width = 16, height = 5,
              font = ("times new roman", 50) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=240)

        Label(screen2,text = name,padx=0,pady=10, width = 29, height = 0,
              font = ("times new roman", 30) ,anchor=N,
              bg='white',fg = "deepskyblue4").place(x=600,y=240)
        
        Label(screen2,text = 'Role :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=340)

        Label(screen2,text = 'Student',padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=340)

        Label(screen2,text = 'Class/Section :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=390)

        Label(screen2,text =(cl,'/',sec) ,padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=390)

        Label(screen2,text = 'Phone No :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=440)

        Label(screen2,text = phone,padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=440)

        Label(screen2,text = 'DOB :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=490)

        Label(screen2,text = dob,padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=490)

        Label(screen2,text = 'Email :',padx=50,pady=0, width = 30, height = 2,
              font = ("times new roman", 22) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=600,y=540)

        Label(screen2,text = email,padx=0,pady=0, width = 21, height = 2,
              font = ("times new roman", 22) ,anchor=NE,
              bg='white',fg = "deepskyblue4").place(x=850,y=540)

        
    profile()

    def fees():
        Label(screen2,width = 500 , height = 300, bg='deepskyblue4').place(x=400,y=200)
        Label(screen2,padx=25,pady=0, width = 20, height = 8,
              font = ("times new roman", 50) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=550,y=200)

        f=open('Fees.txt','r')
        lines =f.readlines()
        Label(screen2,text = lines[0], width = 17, height = 0,
              font = ("times new roman", 36) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=720,y=215)

        Label(screen2,text = lines[1], width = 60, height = 0,
              font = ("times new roman", 13) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=720,y=270)

        Label(screen2,text = '_'*37, width = 35, height = 0,
              font = ("times new roman",24 ,"bold") ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=300)

        Label(screen2,text = lines[2], width = 60, height = 0,
              font = ("times new roman", 13) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=695,y=290)

        Label(screen2,text = lines[3], width = 44, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=350)

        Label(screen2,text = adm, width = 44, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=700,y=350)

        Label(screen2,text = lines[5], width = 10, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1160,y=350)

        Label(screen2,text = '_'*37, width = 35, height = 0,
              font = ("times new roman",24 ,"bold") ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=400)

        Label(screen2,text = lines[6], width = 15, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=380)

        Label(screen2,text = name, width = 44, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=710,y=380)

        Label(screen2,text = lines[4], width = 10, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=350)

        Label(screen2,text = lines[7], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=380)

        Label(screen2,text = (cl,'-',sec) , width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1170,y=380)

        Label(screen2,text = '_'*37, width = 35, height = 0,
              font = ("times new roman",24 ,"bold") ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=460)

        Label(screen2,text = lines[8], width = 10, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=440)

        Label(screen2,text = lines[9], width = 10, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=440)

        Label(screen2,text = lines[10], width = 10, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=500)

        Label(screen2,text = lines[11], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=500)

        Label(screen2,text = lines[12], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=530)

        Label(screen2,text = lines[13], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=530)

        Label(screen2,text = lines[14], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=560)

        Label(screen2,text = lines[15], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=560)

        Label(screen2,text = lines[16], width = 15, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=590)

        Label(screen2,text = lines[17], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=590)

        Label(screen2,text = lines[18], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=620)

        Label(screen2,text = lines[19], width = 15, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=620)

        Label(screen2,text = '_'*37, width = 35, height = 0,
              font = ("times new roman",24 ,"bold") ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=670)

        Label(screen2,text = lines[20], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=650)

        Label(screen2,text = lines[21], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=650)

        Label(screen2,text = '_'*37, width = 35, height = 0,
              font = ("times new roman",24 ,"bold") ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=725)

        Label(screen2,text = lines[22], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=645,y=710)

        Label(screen2,text = lines[23], width = 13, height = 0,
              font = ("times new roman", 15) ,anchor=NW,
              bg='white',fg = "deepskyblue4").place(x=1045,y=710)


    def logout():
        msg=messagebox.askquestion ('Logout','Are you sure you want to logout ?',icon = 'warning')
        if(msg=='yes'):
            screen2.withdraw()
            screen1.deiconify()
            main_screen1()
            quit()

        

        
    b1=HoverButton(screen2,text = "Profile", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                   activeforeground='white',font = ("Calibri", 28),command=profile).place(x=0 , y=140)

    b2=HoverButton (screen2,text = "Fees" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=fees).place(x=0 , y=218)

    b4=HoverButton (screen2,text = "Logout" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=logout).place(x=0 , y=296)
    

   
    screen2.mainloop()


    
def main_screen1():
    global canvas1,canvas2,l1,l2
   
    
    screen1.attributes('-fullscreen',True)  
    screen1.title("School Mangement System")

    Label(screen1,text = "Welcome to DAV Public School" ,padx=390,pady=20, width = 50 , height = 100,
          font = ("times new roman", 45) ,anchor=NW,
          bg='deepskyblue4',fg = "white").place(x=0,y=0)
    Label(screen1,width = 1000 , height = 1, bg='white').place(x=0,y=120)
    Label(screen1,width =1 , height = 1000, bg='white').place(x=350,y=120)

    canvas1 = Canvas(screen1, width = 900, height = 116)  
    canvas1.place(x=500,y=180)  
    img1 = ImageTk.PhotoImage(Image.open("dav_resized.png"))
    canvas1.create_image(0, 0, anchor=NW, image=img1) 
    global canvas2,l2
    canvas2 = Canvas(screen1, width = 900, height = 238)  
    canvas2.place(x=500,y=340)  
    img2 = ImageTk.PhotoImage(Image.open("Webp.net-resizeimage.png"))
    canvas2.create_image(0, 0, anchor=NW, image=img2)

    l2=Label(screen1,text = "We at D.A.V. believe in setting clear visions and challenges\n in keeping with the new millennium and laying a healthy\n foundation by creating a sustainable environment, that is the\n key to human existence...." ,
                 width = 50 , height = 100,
                 font = ("times new roman", 28) ,anchor=NW,
                 bg='deepskyblue4',fg = "white")
    l2.place(x=500,y=650)
    
    b1=HoverButton(screen1,text = "Home", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=main_screen1).place(x=0 , y=140)

    b2=HoverButton(screen1,text = "Staff Login", borderwidth=1,height = "1", width = "18",
                   activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=stafflogin).place(x=0 , y=218)

    b3=HoverButton (screen1,text = "Student Login" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=studentlogin).place(x=0 , y=296)
  
    b4=HoverButton (screen1,text = "Exit" ,borderwidth=1,height = "1", width = "18",
                    activebackground='deepskyblue3',bg='deepskyblue4',fg='white',
                    activeforeground='white',font = ("Calibri", 28),command=quit_screen).place(x=0 , y=374)

    screen1.mainloop()
main_screen1()

