from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables 
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cnfpass=StringVar()
        self.var_check=IntVar()

        #background Image
        frame1=Frame(self.root,bg="black")
        frame1.place(x=0,y=0,relwidth=1,relheight=1)


        #main frame
        frame=Frame(self.root,bg="black")
        frame.place(x=420,y=130,width=680,height=550)


        register_lbl=Label(frame,text="REGISTRATION FORM",font=("times new roman",25,"bold"),bg="black",fg="white")
        register_lbl.place(x=165,y=20)


        #Label and Entry


        #_-------------Row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        fname.place(x=50,y=100)
        self.userEntry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.userEntry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        lname.place(x=370,y=100)
        self.lastnameEntry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lastnameEntry.place(x=370,y=130,width=250)


        #-------------Row 2 

        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="black",fg="white")
        contact.place(x=50,y=170)
        self.contactEntry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contactEntry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="white")
        email.place(x=370,y=170)
        self.emailEntry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.emailEntry.place(x=370,y=200,width=250)

        #--------Row 3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_Q.place(x=50,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select Question","What is your birth place ?","What is your school name ?","What is your pet name ?")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_A.place(x=370,y=240)
        self.security_A_Entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.security_A_Entry.place(x=370,y=270,width=250)

        #--------Row 4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=50,y=310)
        self.password_Entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_Entry.place(x=50,y=340,width=250)

        confirmpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        confirmpassword.place(x=370,y=310)
        self.confirmpassword_Entry=ttk.Entry(frame,textvariable=self.var_cnfpass,font=("times new roman",15,"bold"))
        self.confirmpassword_Entry.place(x=370,y=340,width=250)

        #===============Check Button===========
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree with the Terms & Conditions",font=("times new roman",12,"bold"),bg="black",fg="white",activeforeground="white",activebackground="black",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)

        #-----------buttons-----------
        reg_btn=Button(frame,text="REGISTER",command=self.registerData,font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        reg_btn.place(x=170,y=450,width=120,height=35)

        login_btn=Button(frame,text="LOGIN",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=380,y=450,width=120,height=35)
        
    
    #------------- Register Data------------
    def registerData(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_cnfpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our T&Cs")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_fname.get(),
                                                                        self.var_lname.get(),
                                                                        self.var_contact.get(),
                                                                        self.var_email.get(),
                                                                        self.var_securityQ.get(),
                                                                        self.var_securityA.get(),
                                                                        self.var_pass.get()
                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()