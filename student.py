from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root  #home window 
        self.root.geometry("1530x790+0+0")  #window size 
        self.root.title("Face Recognition System") #window title 
        self.root.wm_iconbitmap("face.ico")


        #-------------Variables---------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #first image 
        img=Image.open(r"E:\Face Recognition System\images\smart-attendance.jpg")
        img=img.resize((510,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)


        #second image 
        img1=Image.open(r"E:\Face Recognition System\images\face-recognition.png")
        img1=img1.resize((510,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)


        #third image 
        img2=Image.open(r"E:\Face Recognition System\images\image1.jpg")
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

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #BACK BUTTON
        back_btn=Button(title_lbl,text="Back",command=self.backbutton,font=("times new roman",12,"bold"),fg="white",bg="blue")
        back_btn.place(x=1400,y=0,width=100,height=40)

            
        #mainframe for student details 
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left frame window 
        left_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_label_frame.place(x=10,y=10,width=730,height=580)

        #left frame image 
        img_left=Image.open(r"E:\Face Recognition System\images\computer.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_label_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=720,height=130)
        

        #current course
        current_course_frame=LabelFrame(left_label_frame,bd=2,bg="white",relief=RIDGE,text="COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=3,y=135,width=720,height=115)

        #department combobox
        dep_label=Label(current_course_frame,text="Department",bg="white",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","IT","ME","EE","CE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Course combobox
        course_label=Label(current_course_frame,text="Course",bg="white",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","ME","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year combobox
        year_label=Label(current_course_frame,text="Year",bg="white",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester combobox
        semester_label=Label(current_course_frame,text="Semester",bg="white",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Student information
        class_student_course_frame=LabelFrame(left_label_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_course_frame.place(x=3,y=250,width=720,height=300)

        #student id 
        student_id_label=Label(class_student_course_frame,text="StudentID:",bg="white",font=("times new roman",12,"bold"))
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentID_entry=ttk.Entry(class_student_course_frame,textvariable=self.va_std_id,width=25,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_name_label=Label(class_student_course_frame,text="Student Name:",bg="white",font=("times new roman",12,"bold"))
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentname_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_std_name,width=25,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Section entry
        class_div_label=Label(class_student_course_frame,text="Section:",bg="white",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_course_frame,textvariable=self.var_section,font=("times new roman",13,"bold"),state="readonly",width=20)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       # class_div_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_section,width=25,font=("times new roman",12,"bold"))
       # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #class roll number entry 
        roll_no_label=Label(class_student_course_frame,text="Roll No:",bg="white",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        roll_no_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_roll,width=25,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender Entry 
        gender_label=Label(class_student_course_frame,text="Gender:",bg="white",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_course_frame,textvariable=self.var_gen,font=("times new roman",13,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #gender_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_gen,width=25,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB Entry 
        dob_label=Label(class_student_course_frame,text="DOB:",bg="white",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dob_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_dob,width=25,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email Entry 
        email_label=Label(class_student_course_frame,text="Email:",bg="white",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_email,width=25,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phoneNo Entry 
        phoneNo_label=Label(class_student_course_frame,text="Phone No:",bg="white",font=("times new roman",12,"bold"))
        phoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phoneNo_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_phone,width=25,font=("times new roman",12,"bold"))
        phoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address Entry 
        address_label=Label(class_student_course_frame,text="Address:",bg="white",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        address_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_address,width=25,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name Entry 
        teacher_name_label=Label(class_student_course_frame,text="Teacher Name:",bg="white",font=("times new roman",12,"bold"))
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacher_name_entry=ttk.Entry(class_student_course_frame,textvariable=self.var_teacher,width=25,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #Radio Buttons 
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_course_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_course_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        #addsave button 
        save_btn=Button(btn_frame,text="Save",command=self.addData,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        save_btn.grid(row=0,column=0)

        #Update button 
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        update_btn.grid(row=0,column=1)


        #delete button 
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        delete_btn.grid(row=0,column=2)

        #reset button 
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        reset_btn.grid(row=0,column=3)


        #button frame for taking and updating of photo sample 
        btn1_frame=Frame(class_student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=235,width=715,height=35)

        #take a photo sample button 
        take_photo_sample_btn=Button(btn1_frame,text="Take a Photo Sample",command=self.generate_dataset,font=("times new roman",12,"bold"),fg="white",bg="blue",width=39)
        take_photo_sample_btn.grid(row=0,column=0)

        #Update a photo sample button 
        update_photo_sample_btn=Button(btn1_frame,text="Update a Photo Sample",font=("times new roman",12,"bold"),fg="white",bg="blue",width=39)
        update_photo_sample_btn.grid(row=0,column=1)




        #right frame window 
        right_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_label_frame.place(x=750,y=10,width=720,height=580)


        img_right=Image.open(r"E:\Face Recognition System\images\portalimage.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_label_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=720,height=130)


        #----------Search System-----------
        search_frame=LabelFrame(right_label_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        search_frame.place(x=3,y=135,width=710,height=70)


        #search bar label
        search_label=Label(search_frame,text="Search By:",bg="red",fg="white",font=("times new roman",15,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search
        self.var_combosearch=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combosearch,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        #Search button 
        search_btn=Button(search_frame,text="Search",command=self.search_data,font=("times new roman",12,"bold"),fg="white",bg="blue",width=12)
        search_btn.grid(row=0,column=3,padx=4)

        #Show All button 
        show_all_btn=Button(search_frame,text="Show All",command=self.fetch_data,font=("times new roman",12,"bold"),fg="white",bg="blue",width=12)
        show_all_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=LabelFrame(right_label_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=210,width=710,height=350)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","ID","Name","Section","Roll No","Gender","DOB","Email","Phone No","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    #-----------Function Declaration-----------

    def backbutton(self):
            self.root.destroy()

    def addData(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get() 
                                                                                                                
                                                                                                        ))             
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #------------------ Fetch Data--------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.commit()
        conn.close()


    #----------- get cursor-----------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content.get("values",[])
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.va_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_section.set(data[6])
            self.var_roll.set(data[7])
            self.var_gen.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
        else:
            pass

    #update function 
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                upd=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if upd>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(

                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_section.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.va_std_id.get() 
                                                                                                                                                                                                            
                                                                                                                                                                                                                ))
                else:
                    if not upd:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #-------delete data-------
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully deleted student details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #------reset button function--------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("Select Division")
        self.var_roll.set("")
        self.var_gen.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #searchdata
    def search_data(self):
        if self.var_combosearch.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_combosearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #---------generate data set and take photo sample 
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(

                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_section.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.va_std_id.get()==id+1 
                                                                                                                                                                                                            
                                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #-------- load predefined data on face frontals from opencv--------

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                #---------
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #Minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filename_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(filename_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()