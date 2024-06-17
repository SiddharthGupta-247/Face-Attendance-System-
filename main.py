from tkinter import*
from tkinter import ttk
import tkinter 
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os


class FaceRecognitionSystem:
    def __init__(self,root):
        self.root=root  #home window 
        self.root.geometry("1530x790+0+0")  #window size 
        self.root.title("Face Recognition System") #window title 
        self.root.wm_iconbitmap("face.ico")


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

        

        #studentdetails button
        img4=Image.open(r"E:\Face Recognition System\images\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_lbl,image=self.photoimg4,command=self.studentDetails,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Details",command=self.studentDetails,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #DetectFace button
        img5=Image.open(r"E:\Face Recognition System\images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.detect_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Face Detector",cursor="hand2",command=self.detect_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Attendance Face button
        img6=Image.open(r"E:\Face Recognition System\images\attendance.jpeg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help button
        img7=Image.open(r"E:\Face Recognition System\images\helpdesk.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_lbl,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Help Desk",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #TrainFace button
        img8=Image.open(r"E:\Face Recognition System\images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_lbl,image=self.photoimg8,cursor="hand2",command=self.trainData)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Train Data",cursor="hand2",command=self.trainData,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #PhotoCollection button
        img9=Image.open(r"E:\Face Recognition System\images\traindata.png")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_lbl,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Photo Data",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer Details button
        img10=Image.open(r"E:\Face Recognition System\images\dev.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_lbl,image=self.photoimg10,cursor="hand2",command=self.developer,)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Developer Details",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit button
        img11=Image.open(r"E:\Face Recognition System\images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_image(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #---------------Function Buttons---------------------
    def studentDetails(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def trainData(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def detect_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()