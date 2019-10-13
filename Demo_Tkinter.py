import tkinter
import tkinter.messagebox as mb
from tkinter import *
tk=tkinter.Tk()
def Message():
    print("hii")
    mb.showinfo("broooo","You are Fired")
tk.title("My First GUI")
b1=Button(tk,text="Click Here",command=Message).grid(column="1",row="5")
b2=Button(tk,text="Show time",bg="blue").grid(column="2",row="7")
tk.geometry("1500x1000")
tk.mainloop()