from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root  #home window 
        self.root.geometry("1530x790+0+0")  #window size 
        self.root.title("Face Recognition System") #window title 
        self.root.wm_iconbitmap("face.ico")

        #variables 
        self.var_attendId=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

        #first image 
        img=Image.open(r"E:\Face Recognition System\images\smart-attendance.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        #second image 
        img1=Image.open(r"E:\Face Recognition System\images\face-recognition.png")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)


        #background image 
        img3=Image.open(r"E:\Face Recognition System\images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=200,width=1530,height=700)


        title_lbl=Label(bg_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
       
        #BACK BUTTON
        back_btn=Button(title_lbl,text="Back",command=self.backbutton,font=("times new roman",12,"bold"),fg="white",bg="blue")
        back_btn.place(x=1400,y=0,width=100,height=40)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)


        #left frame window 
        left_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_label_frame.place(x=10,y=10,width=730,height=580)

        #left frame image 
        img_left=Image.open(r"E:\Face Recognition System\images\unnamed.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_label_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=720,height=130)


        left_inside_frame=Frame(left_label_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=135,width=720,height=370)



        #labels and entrys

        #student ID
        student_ID_label=Label(left_inside_frame,text="Student ID:",bg="white",font=("times new roman",12,"bold"))
        student_ID_label.grid(row=0,column=0,padx=10,pady=5)
        studentID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendId,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5)

        #RollNo
        RollNo_label=Label(left_inside_frame,text="Roll No:",bg="white",font=("times new roman",12,"bold"))
        RollNo_label.grid(row=0,column=2,padx=4,pady=8)
        RollNo_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        RollNo_entry.grid(row=0,column=3,pady=8)


        #Name 
        name_label=Label(left_inside_frame,text="Student Name:",bg="white",font=("times new roman",12,"bold"))
        name_label.grid(row=1,column=0)
        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8)


        #Department
        dep_label=Label(left_inside_frame,text="Department:",bg="white",font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=2)
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)


        #time
        time_label=Label(left_inside_frame,text="Time:",bg="white",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=0)
        time_label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=1,pady=8)


        #Date
        date_label=Label(left_inside_frame,text="Date:",bg="white",font=("times new roman",12,"bold"))
        date_label.grid(row=2,column=2)
        date_label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        date_label.grid(row=2,column=3,pady=8)


        #attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status:",bg="white",font=("times new roman",12,"bold"))
        attendance_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attendance,font=("times new roman",13,"bold"),state="readonly",width=16)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        #addsave button 
        save_btn=Button(btn_frame,text="Import",command=self.importCSV,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        save_btn.grid(row=0,column=0)

        #Update button 
        update_btn=Button(btn_frame,text="Export",command=self.exportCSV,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        update_btn.grid(row=0,column=1)


        #delete button 
        delete_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        delete_btn.grid(row=0,column=2)

        #reset button 
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),fg="white",bg="blue",width=19)
        reset_btn.grid(row=0,column=3)
        





        #right frame window 
        right_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        right_label_frame.place(x=750,y=10,width=720,height=580)


        #table frame
        table_frame=Frame(right_label_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=705,height=455)



        #------------Scroll bar and table----------
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll No","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)



        self.attendanceReportTable.heading("ID",text="Attendance ID")
        self.attendanceReportTable.heading("Roll No",text="Roll No")
        self.attendanceReportTable.heading("Name",text="Name")
        self.attendanceReportTable.heading("Department",text="Department")
        self.attendanceReportTable.heading("Time",text="Time")
        self.attendanceReportTable.heading("Date",text="Date")
        self.attendanceReportTable.heading("Attendance",text="Attendance")

        self.attendanceReportTable["show"]="headings"
        self.attendanceReportTable.column("ID",width=100)
        self.attendanceReportTable.column("Roll No",width=100)
        self.attendanceReportTable.column("Name",width=100)
        self.attendanceReportTable.column("Department",width=100)
        self.attendanceReportTable.column("Time",width=100)
        self.attendanceReportTable.column("Date",width=100)
        self.attendanceReportTable.column("Attendance",width=100)


        self.attendanceReportTable.pack(fill=BOTH,expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>",self.get_Cursor)

    #-----------Face Data------------
    def fetchdata(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)


    #import CSV file
    def importCSV(self):
        global mydata
        mydata.clear()
        fileName=filedialog.askopenfilename(initialdir=os.getcwd(),title="Import CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fileName) as myFile:
            csvRead=csv.reader(myFile,delimiter=",")
            for i in csvRead:
                mydata.append(i)
            self.fetchdata(mydata)


    #export CSV file
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found to Export",parent=self.root)
                return False
            fileName=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Export CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fileName,mode="w",newline="") as myFile:
                exp_write=csv.writer(myFile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your Data Exported to "+os.path.basename(fileName)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_Cursor(self,event=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content.get("values",[])
        if rows:
            self.var_attendId.set(rows[0])
            self.var_roll.set(rows[1])
            self.var_name.set(rows[2])
            self.var_dep.set(rows[3])
            self.var_time.set(rows[4])
            self.var_date.set(rows[5])
            self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_attendId.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

    def backbutton(self):
        self.root.destroy()
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()