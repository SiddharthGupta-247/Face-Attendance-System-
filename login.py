from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     #pip install pillow
from tkinter import messagebox
from main import FaceRecognitionSystem
from register import Register
import mysql.connector

def main():
    win=Tk()
    app=LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")

        #background Image
        
         #first image 
        img=Image.open(r"E:\Face Recognition System\images\united3.png")
        img=img.resize((510,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)


        #second image 
        img1=Image.open(r"E:\Face Recognition System\images\facialrecognition.png")
        img1=img1.resize((510,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)


        #third image 
        img2=Image.open(r"E:\Face Recognition System\images\united4.png")
        img2=img2.resize((510,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)


        #background image 
        img3=Image.open(r"E:\Face Recognition System\images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1530,height=700)

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDACE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=450)

        img1=Image.open(r"E:\Face Recognition System\images\loginpage.png")
        img1.resize((150,150),Image.LANCZOS)
        self.photoImage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoImage1,bg="black",borderwidth=0)
        lbl_img1.place(x=735,y=205,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=100,y=100)

        #labels for authorization
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username_lbl.place(x=70,y=155)

        self.userEntry=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.userEntry.place(x=37,y=185,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password_lbl.place(x=70,y=225)

        self.passEntry=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")
        self.passEntry.place(x=37,y=250,width=270)


        #----------icon of images ------------
        img2=Image.open(r"E:\Face Recognition System\images\LoginIconApp11.png")
        img2.resize((25,25),Image.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoImage2,bg="black",borderwidth=0)
        lbl_img2.place(x=650,y=355,width=25,height=25)

        img3=Image.open(r"E:\Face Recognition System\images\lock-5122.png")
        img3.resize((25,25),Image.LANCZOS)
        self.photoImage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoImage3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=425,width=25,height=25)

        #login button
        login_btn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=110,y=300,width=120,height=35)

        reg_btn=Button(frame,text="Register New User",command=self.register_window,font=("times new roman",10,"bold"),bd=3,border=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        reg_btn.place(x=16,y=350,width=160)

        forget_btn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),bd=3,border=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forget_btn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.userEntry.get()=="" or self.passEntry.get()=="":
            messagebox.showerror("Error","Username or Password cannot be empty")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="login")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                        self.userEntry.get(),
                                                                        self.passEntry.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_windom=Toplevel(self.root)
                    self.app=FaceRecognitionSystem(self.new_windom)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password 
    def reset_pass(self):
        if self.combo_security.get()=="select":
            messagebox.showerror("Error","Select a security question",parent=self.root2)
        elif self.security_A_Entry.get()=="":
            messagebox.showerror("Error","Please enter your answer",parent=self.root2)
        elif self.password_Entry.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.userEntry.get(),self.combo_security.get(),self.security_A_Entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.password_Entry.get(),self.userEntry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password changed successfully",parent=self.root2)
                self.root2.destroy()

    

#forget password window 
    def forgot_password_window(self):
        if self.userEntry.get()=="":
            messagebox.showerror("Error","Please enter the username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.userEntry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Reset Password")
                self.root2.geometry("340x450+610+170")

                

                lbl=Label(self.root2,text="Reset Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                lbl.place(x=0,y=10,relwidth=1)

                #--------Row 3
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select Question","What is your birth place ?","What is your school name ?","What is your pet name ?")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black")
                security_A.place(x=50,y=150)
                self.security_A_Entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_A_Entry.place(x=50,y=180,width=250)

                #--------Row 4
                password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black")
                password.place(x=50,y=220)
                self.password_Entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.password_Entry.place(x=50,y=250,width=250)

                reset_btn=Button(self.root2,text="RESET",command=self.reset_pass,font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
                reset_btn.place(x=100,y=290,width=120,height=35)


#Register class 
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
         #first image 
        img=Image.open(r"E:\Face Recognition System\images\united3.png")
        img=img.resize((510,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)


        #second image 
        img1=Image.open(r"E:\Face Recognition System\images\facialrecognition.png")
        img1=img1.resize((510,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)


        #third image 
        img2=Image.open(r"E:\Face Recognition System\images\united4.png")
        img2=img2.resize((510,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)


        #background image 
        img3=Image.open(r"E:\Face Recognition System\images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1530,height=700)

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDACE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        #main frame
        frame=Frame(self.root,bg="black")
        frame.place(x=420,y=200,width=680,height=550)


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

        login_btn=Button(frame,text="LOGIN",command=self.return_login,font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
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
    
    def return_login(self):
        self.root.destroy()


if __name__=="__main__":
    main()