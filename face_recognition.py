from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime, timedelta
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root  #home window 
        self.root.geometry("1530x790+0+0")  #window size 
        self.root.title("Face Recognition System") #window title 
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #BACK BUTTON
        back_btn=Button(title_lbl,text="Back",command=self.backbutton,font=("times new roman",12,"bold"),fg="white",bg="blue")
        back_btn.place(x=1400,y=10,width=100,height=40)


        img_top=Image.open(r"images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)


        img_bottom=Image.open(r"images\facial_rec.jpg")
        img_bottom=img_bottom.resize((950,700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)


        b1_1=Button(f_lbl,text="Recognize Face",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)

    #----------Attendance----------
    def backbutton(self):
        self.root.destroy()

   #def mark_attendance(self,i,r,n,d):
   #     with open("AttendanceReport\Attendance.csv","r+",newline="\n") as f:
   #         mydataList=f.readlines()
   #         name_List=[]
   #         for line in mydataList:
   #             entry=line.split((","))
   #             name_List.append(entry[0])
    #        if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
    #            now=datetime.now()
   #             d1=now.strftime("%d/%m/%Y")
   #             dtString=now.strftime("%H:%M:%S")
   #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def mark_attendance(self, i, r, n, d):
        new_data = []
        with open(r"AttendanceReport\Attendance.csv","r+", newline="\n") as f:
            mydataList = f.readlines()
            name_List = []
            current_time = datetime.now()
            cutoff_time = current_time - timedelta(hours=24)
            
        # Filter entries older than 24 hours
        
            for line in mydataList:
                entry = line.split(",")
                if len(entry)>=6:
                    entry_date = datetime.strptime(entry[-2].strip(), "%d/%m/%Y")
                    entry_time = datetime.strptime(entry[-3], "%H:%M:%S")
                    if datetime.combine(entry_date, entry_time.time()) >= cutoff_time:
                        new_data.append(line)
            
            f.seek(0)
            f.truncate()
            f.writelines(new_data)
            
            for line in new_data:
                entry = line.split(",")
                name_List.append(entry[0])

            if (i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            else:
                for line in new_data:
                    entry = line.split(",")
                    if entry[0] == i:
                        # Update arrival time for student i
                        entry[-2] = datetime.now().strftime("%d/%m/%Y")
                        entry[-3] = datetime.now().strftime("%H:%M:%S")  # Update time column index
                        new_data[new_data.index(line)] = ",".join(entry)  # Update line in new_data
                f.seek(0)
                f.truncate()
                f.writelines(new_data)


    #--------Face Recognition function-----------
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                try:

                    conn=mysql.connector.connect(host="localhost",username="root",password="319413",database="face_recognizer")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select Name from student where student_id="+str(id))
                    n=my_cursor.fetchone()
                    n=''+''.join(n)

                    my_cursor.execute("select Roll from student where student_id="+str(id))
                    r=my_cursor.fetchone()  
                    r=''+''.join(r)

                    my_cursor.execute("select Dep from student where student_id="+str(id))
                    d=my_cursor.fetchone()
                    d=''+''.join(d)

                    my_cursor.execute("select student_id from student where student_id="+str(id))
                    i=my_cursor.fetchone()
                    i=''+''.join(i)


                    if confidence>80:
                        cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(i,r,n,d)

                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,y]
                except mysql.connector.Error as e:
                    print("Error connecting to database:",e)

                finally:
                    if 'conn' in locals() and conn.is_connected():
                        my_cursor.close()
                        conn.close()
                
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            
            if not ret:
                print("Error: Failed to capture frame")
                break

            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        cv2.destroyAllWindows()
        video_cap.release()


if __name__=="__main__":
    root=tk.Tk()
    obj=Face_Recognition(root)
    root.mainloop()