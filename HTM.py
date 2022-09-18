
from telnetlib import SB
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
import socket
import os, sys,openpyxl
import re, uuid
from tokenize import Name
import hashlib
import mysql.connector
from tkinter import messagebox
import PIL
import pyautogui
import time




#here
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "details"
    )
#end


def getName():
    name = socket.gethostname()
    return name
a1=getName()

def getMachine_addr():
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic bios get serialnumber"
    return os.popen(command).read().replace("\n","").replace(" ","").replace(" ","")
addr = getMachine_addr()
a2 = addr.replace('SerialNumber', '')

def getMac():  
    a = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
    return a
a3=getMac()

def getHash():
    p = getMac() + getMachine_addr() + getName()
    uid = hashlib.sha1(p.encode())
    uuid = uid.hexdigest()    
    return uuid
a4=getHash()

def getIp():
    import socket   
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)      
    return IPAddr 
a5=getIp()



def Login():
    
    #here
    if email.get() != "" and password.get() != "" and e.match(email.get())  :
        mycursor = mydb.cursor()
        sql = "SELECT * FROM HTM WHERE email = '%s' AND  password = '%s'" % (email.get(),password.get())
        mycursor.execute(sql)
        if mycursor.fetchone():
            print("Successfully")
            messagebox.showinfo("Login Successful","Status: Login Successful") 
            def zoom():
                cmd=r"C:\Users\nehas\AppData\Roaming\Zoom\bin\Zoom.exe"
                os.system(cmd)
            zoom()
            time.sleep(1)
            meet="2328655596"
            print(os.getcwd())
            s1 = pyautogui.locateOnScreen('dark.png', confidence=0.9)
            print(s1)
            pyautogui.leftClick(s1)
            time.sleep(1)

            s2 = pyautogui.locateOnScreen('dark2.png', confidence=0.9)
            print(s2)
            pyautogui.leftClick(s2)
            pyautogui.typewrite(meet,interval=0.01)
            time.sleep(1)


            s3 = pyautogui.locateOnScreen('dark3.png', confidence=0.9)
            print(s3)
            pyautogui.leftClick(s3)


            def unique():
                email.get()
                my_wb = openpyxl.Workbook()
                my_sheet = my_wb.active
                a=10
                i=1
                d1='rushilpajni@gmail.com'
                
            
                for i in range(a):
                    b=uuid.uuid4()

                    print(b)
                    i=i+1
                    c1 = my_sheet.cell(row=i+1,column=3)
                    c2 = my_sheet.cell(row=i+1,column=1)
                    b9 = my_sheet.cell(row=i+1,column=4)
                    c1.value = f'{b}'
                    c2.value = f'{i}'
                    c3 = my_sheet.cell(row=2,column=2)
                    c3.value=f'{d1}'
                    
                
                    my_wb.save("C:\\Users\\nehas\\Desktop\\Final01\\Final\\nounce1.xlsx")

                from pathlib import Path
                import smtplib
                conn = smtplib.SMTP('smtp.gmail.com', 587)
                conn.ehlo()
                conn.starttls()
                conn.login('rushilpajni2@gmail.com', 'srtxyyvhdkliyosy')

                xlsx_file = Path('C:\\Users\\nehas\\Desktop\\Final01\\Final', 'nounce1.xlsx')
                wb_obj = openpyxl.load_workbook(xlsx_file) 
                msg='b6F1Wm'
                conn.sendmail(f'rushilpajni2@gmail.com',str(email.get()),msg)
                conn.quit()

                sheet = wb_obj.active
                import cv2
                from datetime import datetime

                
            unique()
        else:
            print("Invalid Credentials")
            messagebox.showinfo("Invalid Credentials","Status: Please try again") 
        
    else:
        messagebox.showinfo("Login error", "*Username and password fields can not be empty Or You have entered a invalid email address*")
    #end
    
    global a
    global b
    a=email.get()
    b=password.get()
    print("Email: ",a)
    print("Password: ",b)
    print("Machine Name : ",a1)
    print("Machine Serial No. : ",a2)
    print("Machine MAC : ",a3)
    print("Hash Generated : ",a4)
    print("Ip Address:",a5)



    

def Register():
    global win2
    win1.destroy()
    win2=Tk()
    win2.geometry('1190x600')  
    win2.title('FRIENDS - Login/Register')
    win2.config(background="lavender")
    win2.resizable(False,False)

    img=PIL.Image.open(r"htm2.png")
    win2.bg=ImageTk.PhotoImage(img)
    win2.bg_image=Label(image=win2.bg).place(x=0,y=0,relwidth=1,relheight=1)
    

    win2.Frame_login=Frame(background="white")
    win2.Frame_login.place(x=165,y=75,height=378,width=700)
    img1=PIL.Image.open(r"Frame3.png")
    win2.Frame_login.img = ImageTk.PhotoImage(img1)
    bg_img=Label(win2.Frame_login,image=win2.Frame_login.img).place(x=-2,y=-2)

    email2Label = Label(win2.Frame_login,font=("Inter",9,"bold"), text="Email*",background = "white", foreground = "#3c3953")
    email2Label.place(x=375,y=40)
    email2 = StringVar()
    email2Entry = Entry(win2.Frame_login,bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT, textvariable=email2)
    email2Entry.place(height=30,width=246,x=375,y=63)
    email_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    email_line.place(x=377,y=90)


    password2Label = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Create Password* ",background = "white", foreground = "#3c3953")
    password2Label.place(x=375,y=104)  
    password2 = StringVar()
    password2Entry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=password2, show='*')
    password2Entry.place(height=30,width=246,x=375,y=129)
    password_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    password_line.place(x=377,y=155)

    password3Label = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Confirm Password*",background = "white", foreground = "#3c3953")
    password3Label.place(x=375,y=169)  
    password3 = StringVar()
    password3Entry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=password3, show='*')
    password3Entry.place(height=30,width=246,x=375,y=194)
    password3_line=Canvas(win2.Frame_login,width=250,height=2.0,bg="black",highlightthickness=0)
    password3_line.place(x=377,y=220)

    nameLabel = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Name*",background = "white", foreground = "#3c3953")
    nameLabel.place(x=375,y=234)  
    name = StringVar()
    nameEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=name)
    nameEntry.place(height=30,width=73,x=375,y=259)
    name_line=Canvas(win2.Frame_login,width=75,height=2.0,bg="black",highlightthickness=0)
    name_line.place(x=377,y=285)

    roll_noLabel = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Roll No*",background = "white", foreground = "#3c3953")
    roll_noLabel.place(x=463,y=234)  
    roll_no = StringVar()
    roll_noEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=roll_no)
    roll_noEntry.place(height=30,width=73,x=463,y=259)
    roll_no_line=Canvas(win2.Frame_login,width=75,height=2.0,bg="black",highlightthickness=0)
    roll_no_line.place(x=465,y=285)
    
    deptLabel = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Programme",background = "white", foreground = "#3c3953")
    deptLabel.place(x=375,y=299)  
    dept = StringVar()
    deptEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=dept)
    deptEntry.place(height=30,width=110,x=375,y=324)
    dept_line=Canvas(win2.Frame_login,width=110,height=2.0,bg="black",highlightthickness=0)
    dept_line.place(x=377,y=350)
    
    streamLabel = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Stream",background = "white", foreground = "#3c3953")
    streamLabel.place(x=553,y=234)  
    stream= StringVar()
    streamEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=stream)
    streamEntry.place(height=30,width=75,x=553,y=259)
    stream_line=Canvas(win2.Frame_login,width=75,height=2.0,bg="black",highlightthickness=0)
    stream_line.place(x=555,y=285)

    specialisationLabel = Label(win2.Frame_login,font=("Inter",9,"bold"),text="Specialisation",background = "white", foreground = "#3c3953")
    specialisationLabel.place(x=498,y=299)  
    specialisation= StringVar()
    specialisationEntry = Entry(win2.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",10),relief=FLAT,textvariable=specialisation)
    specialisationEntry.place(height=30,width=130,x=498,y=324)
    specialisation_line=Canvas(win2.Frame_login,width=130,height=2.0,bg="black",highlightthickness=0)
    specialisation_line.place(x=500,y=350)

    def validation():
    
        
        msg = ''

        if email2.get()=="":
            msg = 'email can\'t be empty'
            
            
            

        elif password2.get() == "" and password3.get()=="":
            msg = 'Password can\'t be empty' 
        
        elif name.get() == "":
            msg = 'name can\'t be empty'

        elif roll_no.get() =="":
            msg='Roll no can\'t be empty' 


        else:
            try:
                f= re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
                if not f.match(email2.get()):
                    msg='Valid email address!'
                elif password2.get() != password3.get(): 
                    msg = 'Please make sure your passwords match'

                elif any(ch.isdigit() for ch in name.get()): 
                    msg = 'Name can\'t have numbers'
                
                elif roll_no.get()!="": 
                    msg = 'Success'

                else:
                    msg = 'Success!'
                    if (msg=='Valid email address!'):
                        print("Successfully Done")

            except Exception as ep:
                messagebox.showerror('error', ep)

        
        messagebox.showinfo('message', msg)


    def details():
        c=name.get()
        d=roll_no.get()
        e2=email2.get()
        f=password2.get()
        g=dept.get()
        h=stream.get()
        i=specialisation.get()
        
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO HTM (Name,Roll_no,Email,Password,Department,Stream,Specialisation,device_name,device_serial,mac,hash,ip) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (c,
               d,
               e2,
               f,
               g,
               h,
               i,
               a1,
               a2,
               a3,
               a4,
               a5
            )

        mycursor.execute(sql,val)
        mydb.commit()
        print("Registeration Successful","Status: Registeration Successful \n *PLease Login To Continue*")


    
    def RegisterSuccess(name,roll_no,email2,password2,password3,dept,stream,specialisation):
        validation()
        details() 
        c=name.get()
        d=roll_no.get()
        e2=email2.get()
        f=password2.get()
        g=dept.get()
        h=stream.get()
        i=specialisation.get()
        j=password3.get()
        print("Name: ",c)
        print("RollNo: ",d)
        print("Email: ",e2)
        print("Password: ",f)
        print("Confirm Password:",j)
        print("Department:",g)
        print("Stream:",h)
        print("Specialisation:",i)       
        print("Machine Name : ",a1)
        print("Machine Serial No. : ",a2)
        print("Machine MAC : ",a3)
        print("Hash Generated : ",a4) 
        print("Ip Address:",a5)
        win2.destroy()     
    RegisterSuccess=partial(RegisterSuccess,name,roll_no,email2,password2,password3,dept,stream,specialisation)
    sb=Image.open(r"Frame4.png")
    photo=ImageTk.PhotoImage(sb)
    sb_label=Label(win2.Frame_login,image=photo,bg="white")
    sb_label.image=photo
    submit= Button(win2, image=photo,text="Submit", borderwidth=0,bg="white",highlightthickness=0,relief=FLAT,command=RegisterSuccess).place(x=580,y=455)
    win2.mainloop()



win1=Tk()
win1.geometry('1190x600')  
win1.title('FRIENDS - Login/Register')
win1.config(background="lavender")
win1.resizable(False,False)

os.chdir(r"C:\Users\nehas\Desktop\FINAL01\FINAL\img")

img=PIL.Image.open(r"htm.png")
win1.bg=ImageTk.PhotoImage(img)
win1.bg_image=Label(image=win1.bg).place(x=0,y=0,relwidth=1,relheight=1)

win1.Frame_login=Frame(background="white")
win1.Frame_login.place(x=350,y=150,height=340,width=500)
img1=PIL.Image.open(r"i2.png")
win1.Frame_login.img = ImageTk.PhotoImage(img1)
bg_img=Label(win1.Frame_login,image=win1.Frame_login.img,background="white").place(x=10,y=15)

win1.Frame_login.txt="FRIENDS"
heading=Label(win1.Frame_login,text=win1.Frame_login.txt,foreground = "#3c3953",font=("OCR A Extended",12,"bold"),bg="white").place(width=300,height=30,x=-12,y=250)

emailLabel = Label(win1.Frame_login,font=("Inter",10,"bold"), text="Username",background = "white", foreground = "#3c3953")
emailLabel.place(x=280,y=60)

email = StringVar()
global e
e= re.compile(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")

emailEntry = Entry(win1.Frame_login,bg="white",foreground = "black",highlightthickness=0,font=("Inter",12),relief=FLAT, textvariable=email)
emailEntry.place(height=30,width=160,x=284,y=88)
email_line=Canvas(win1.Frame_login,width=200,height=2.0,bg="#3c3953",highlightthickness=0)
email_line.place(x=252,y=113)

email_icon=Image.open(r"i1.png")
photo=ImageTk.PhotoImage(email_icon)
email_icon_label=Label(win1.Frame_login,image=photo,bg="white")
email_icon_label.image=photo
email_icon_label.place(x=250,y=88)



passwordLabel = Label(win1.Frame_login,font=("Inter",10,"bold"),text="Password ",background = "white", foreground = "#3c3953")
passwordLabel.place(x=280,y=130)  

password = StringVar()

passwordEntry = Entry(win1.Frame_login, bg="white",foreground = "black",highlightthickness=0,font=("Inter",14),relief=FLAT,textvariable=password, show='*')
passwordEntry.place(height=30,width=200,x=284,y=157)
password_line=Canvas(win1.Frame_login,width=200,height=2.0,bg="#3c3953",highlightthickness=0)
password_line.place(x=252,y=187)

pss_icon=Image.open(r"i12.png")
photo=ImageTk.PhotoImage(pss_icon)
pss_icon_label=Label(win1.Frame_login,image=photo,bg="white")
pss_icon_label.image=photo
pss_icon_label.place(x=250,y=157)

lg=Image.open(r"Frame.png")
photo=ImageTk.PhotoImage(lg)
lg_label=Label(win1.Frame_login,image=photo,bg="white")
lg_label.image=photo
loginButton = Button(win1.Frame_login,image=photo,text="LOGIN",borderwidth=0,command=Login,bg="white",highlightthickness=0,relief=FLAT)
loginButton.place(x=278,y=215)

rg=Image.open(r"Frame2.png")
photo=ImageTk.PhotoImage(rg)
rg_label=Label(win1.Frame_login,image=photo,bg="white")
rg_label.image=photo

txt1="Don't have account?"
heading1=Label(win1.Frame_login,text=txt1,foreground = "#3c3953",font=("Inter",7),bg="white").place(x=281,y=257)

registerButton = Button(win1.Frame_login,image=photo,text="Register",borderwidth=0,command=Register,bg="white",highlightthickness=0,relief=FLAT)
registerButton.place(x=417,y=260)
win1.mainloop()
