import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
root=Tk()
root.title("Text to Speech")
root.geometry("550x650+100+200")
root.resizable(False,False)
root.configure(bg="#B266FF")

engine=pyttsx3.init()
def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voices',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voices',voices[1].id)
            engine.say(text)
            engine.runAndWait()    
    if(text):
        if(speed=="Fast"):
            engine.setProperty("rate",250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',170)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()        



def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voices',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voices',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()    
    if(text):
        if(speed=="Fast"):
            engine.setProperty("rate",250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()              
#icon
image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)
#top frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)
Logo=PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)
text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=25,y=150,width=500,height=200)
Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=130,y=400)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=330,y=400)
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=100,y=450)
gender_combobox.set('Male')
speed_combobox=Combobox(root,values=['Fast','normal','slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=300,y=450)
speed_combobox.set('Normal')
imageicon=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=95,y=500)
imageicon2=PhotoImage(file="download.png")
save=Button(root,text="save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=295,y=500)




root.mainloop()