from tkinter import * 
from tkinter.ttk import *
from time import strftime 

root = Tk() 
root.title('Digital Clock by Aditya Gupta') 

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

lbl = Label(root, font = ('calibri', 80, 'bold'), 
            background = 'black',  
            foreground = 'red') 

lbl.pack(anchor = 'center') 
time() 
  
mainloop() 