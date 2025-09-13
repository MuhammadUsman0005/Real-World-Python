from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")




shutdown = Tk()
shutdown.title("ShutDown App")
shutdown.geometry("500x500")
shutdown.config(bg="Blue")

restart_btn = Button(shutdown,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",border= 5,bg="yellow",activebackground="red",activeforeground="white",command=restart)
restart_btn.place(x=170,y=80,height=70,width=160)
restart_btn = Button(shutdown,text="Restart Time",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="plus",border= 5,bg="yellow",activebackground="red",activeforeground="white",command=restart_time)
restart_btn.place(x=170,y=160,height=70,width=160)
restart_btn = Button(shutdown,text="Log-out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",border= 5,bg="yellow",activebackground="red",activeforeground="white",command=logout)
restart_btn.place(x=170,y=240,height=70,width=160)
restart_btn = Button(shutdown,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",border= 5,bg="yellow",activebackground="red",activeforeground="white",command=shutdown)
restart_btn.place(x=170,y=320,height=70,width=160)

shutdown.mainloop()
