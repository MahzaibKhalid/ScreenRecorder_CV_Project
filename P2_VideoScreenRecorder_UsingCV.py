import cv2
import tkinter as tk
import numpy as np
import pyautogui
from PIL import Image,ImageTk
from tkinter import*
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import time
import sys




#To Start Screen Recording
def run():
    
    # To Capture Screen Size
    rs= pyautogui.size() 
    
    #Define the codec
    
    fourcc= cv2.VideoWriter_fourcc(*"XVID")
    
    # Create Video Write Object
    
    fn=asksaveasfilename(confirmoverwrite=False,defaultextension=".avi")
    out= cv2.VideoWriter(fn,fourcc,20.0,rs)
    print("Recording Started..\n")
    
    count=1
    while True:
        count+=1
        #Create Screenshot
        img=pyautogui.screenshot()
        #Converting these Screen shots into Numpy Array
        frame=np.array(img)
        
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        if(count==10):
            cv2.imshow("Recording..",frame)
            count=1
        
        #To exit the Recording Window
        
        if cv2.waitKey(1) == ord("q"):
        #Writing the frame
          out.write(frame)
          out.release()
          
          sys.exit(0)

#To take the Screenshot 

def screenshot():
    root.destroy()
    print("Screen Shot..\n")
    time.sleep(1)
    myScreenshot=pyautogui.screenshot()
    fn=asksaveasfilename(confirmoverwrite=False,defaultextension=".png")
    myScreenshot.save(fn)
    sys.exit(0)

    
# To Exit the Program
def Exit():
    exit1=messagebox.askyesno("Error","Are you sure want to Exit?")
    if exit1>0:
        root.destroy()
    else:
        return
    
    
root=tk.Tk()
root.geometry("640x320+0+0")
root.title("Screen Recorder")

#Background Image
img=Image.open("MainPage.png")
img=img.resize((640,320),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(img)

f_lbl=Label(root,image=photoimg1)
f_lbl.place(x=0,y=0,width=640,height=320)


#Screen Recording Button
TakeRecorder_img=Image.open("S_Rec.png")
TakeRecorder_img=TakeRecorder_img.resize((200,60),Image.ANTIALIAS)
photoimg2=ImageTk.PhotoImage(TakeRecorder_img)

b = Button(root,image=photoimg2,command=run,cursor="hand2",border=0)
b.place(x=400,y=80,width=200,height=60)

#ScreenShot Button Area                 
ScreenShot_img=Image.open("S_Shot.png")
ScreenShot_img=ScreenShot_img.resize((200,60),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(ScreenShot_img)

b1 = Button(root,image=photoimg3,command=screenshot,cursor="hand2",border=0)
b1.place(x=400,y=150,width=200,height=60)

#Exit Button
Exit_img=Image.open("Exit.png")
Exit_img=Exit_img.resize((100,40),Image.ANTIALIAS)
photoimg4=ImageTk.PhotoImage(Exit_img)

b3 = Button(root,image=photoimg4,command=exit,cursor="hand2",border=0)
b3.place(x=530,y=275,width=100,height=40)

#Uploading Favicon
root.iconbitmap(default="favicon.ico")

root.mainloop()