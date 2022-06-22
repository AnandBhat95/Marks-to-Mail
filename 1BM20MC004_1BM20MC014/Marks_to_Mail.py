import mysql.connector
from tkinter import *
from tkinter import simpledialog
import  smtplib
from email.message import EmailMessage


u=''
usn=''
sub=''
marks=0
ma=''
root=Tk()
root.title("Marks DB")
f = Frame(root, height=400, width=600)
f.propagate(0)
f.pack()
l1=Label(text='USN',font=('Courier', -13,'bold'))
l2=Label(text='E-mail ',font=('Courier', -13,'bold'))
l3=Label(text='Marks',font=('Courier', -13,'bold'))
l4=Label(text='Subject',font=('Courier', -13,'bold'))
         
e1=Entry(f,width=25,fg='blue',bg='lightgrey')
e2=Entry(f,width=25,fg='blue',bg='lightgrey')
e3=Entry(f,width=25,fg='blue',bg='lightgrey')
e4=Entry(f,width=25,fg='blue',bg='lightgrey')
 
l1.place(x=70,y=100)
e1.place(x=200,y=100)
l2.place(x=70,y=150)
e2.place(x=200,y=150)
l3.place(x=70,y=200)
e3.place(x=200,y=200)
l4.place(x=70,y=50)
e4.place(x=200,y=50)


def mail():
    global sub,ma,marks,usn
    for i in range(True):
        sub=e4.get()
        ma=e2.get()
        marks= int(e3.get())
        usn=e1.get()
        
        msg=EmailMessage()
        msg['Subject']='Marks for {} '.format(sub)
        msg['From']='teacher'
        msg['to']=ma
        msg.set_content('Marks for {} is {}'.format(sub,marks))
        
        s=smtplib.SMTP_SSL('smtp.gmail.com',465)
        s.login('your_gmail','your_password')
        s.send_message(msg)
        s.quit()

        

def insert():
   sub=e4.get()
   ma=e2.get()
   marks= int(e3.get())
   usn=e1.get()
   
   c=mysql.connector.connect(host='localhost',database='world',user='root',password='root')
   cursor=c.cursor()

   st='insert into st(usn,sub,mail,marks) values ("%s","%s","%s","%d")'
   args=(usn,sub,ma,marks)
   try:
     cursor.execute(st % args)
     c.commit()
   except:
     c.rollback()
    
   finally:
     cursor.close()
     c.close()

   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e4.delete(0,END)

        
def view():
    c=mysql.connector.connect(host='localhost',database='world',user='root',password='root')
    cursor=c.cursor()
    cursor.execute('select * from st')
    r=cursor.fetchall()
    
    print("\n USN        Sub          Mail                     Marks")
    print('_______________________________________________________')
    for i in r:
        usn=i[0]
        sub=i[1]
        mail=i[2]
        marks=i[3]
        print("%-10s %-10s %-30s %-3s"%(usn,sub,mail,marks))
    cursor.close()
    c.close()
        

def msg():
   global u
   u=simpledialog.askstring(title="To delete",prompt="Enter the usn")


def dele(u):
      c=mysql.connector.connect(host='localhost',database='world',user='root',password='root')
      cursor=c.cursor()
      str='delete from st where usn= "%s"' 
      args=(u)

      try:
        cursor.execute(str % args)
        c.commit()
      except:
        c.rollback()
      finally:
        c.close()
        cursor.close()

def msg1():
   global a,b
   a=simpledialog.askstring(title="To update",prompt="Enter USN")
   b=int(simpledialog.askstring(title="To update",prompt="marks"))

   
def up(m,un):
    c=mysql.connector.connect(host='localhost',database='world',user='root',password='root')
    cursor=c.cursor()
    str='update st set marks= "%d" where usn ="%s"' 
    args=(m,un)
    try:
        cursor.execute(str % args)
        c.commit()
    except:
        c.rollback()
    finally:
        c.close()
        cursor.close()


B1= Button(text='Send mail',activebackground='#345',activeforeground='white',command =mail,width=10,height=1 ,bg='#F0E68C',font=('Times', -12,'bold'))
B1.place(x=130,y=250)
 
B2= Button(text ="View",command = view,width=10,height=1,bg='lightblue',activebackground='#345',activeforeground='white')
B2.place(x=70,y=300)

 
B2= Button(text ="Update",command = lambda:[msg1(),up(b,a)],width=10,height=1,bg='lightblue',activebackground='#345',activeforeground='white')
B2.place(x=180,y=300)

 
B1= Button(text ="Delete",command = lambda:[msg(), dele(u)],width=10,height=1,bg='lightblue',activebackground='#345',activeforeground='white')
B1.place(x=280,y=300)


B1= Button(text='Add',activebackground='#345',activeforeground='white',command = insert,width=10,height=1 ,bg='#F0E68C',font=('Times', -12,'bold'))
B1.place(x=230,y=250)



