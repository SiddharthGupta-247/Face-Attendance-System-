from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root  #home window 
        self.root.geometry("1530x790+0+0")  #window size 
        self.root.title("Face Recognition System") #window title 
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #BACK BUTTON
        back_btn=Button(title_lbl,text="Back",command=self.backbutton,font=("times new roman",12,"bold"),fg="white",bg="blue")
        back_btn.place(x=1400,y=10,width=100,height=40)

        img_top=Image.open(r"images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #Frame 
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)


        img_dev=Image.open(r"images\chat.jpg")
        img_dev=img_dev.resize((200,200),Image.LANCZOS)
        self.photoimg_dev=ImageTk.PhotoImage(img_dev)
        f_lbl=Label(main_frame,image=self.photoimg_dev)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer INFO
        dev_label=Label(main_frame,text="My Name is Siddharth Gupta",bg="white",font=("times new roman",15,"bold"))
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="My Name is Rishabh Pandey",bg="white",font=("times new roman",15,"bold"))
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="My Name is Vijay Raj Singh",bg="white",font=("times new roman",15,"bold"))
        dev_label.place(x=0,y=75)

        img2=Image.open(r"E:\Face Recognition System\images\BestFacialRecognition.jpg")
        img2=img2.resize((500,390),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)
    
    def backbutton(self):
        self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()