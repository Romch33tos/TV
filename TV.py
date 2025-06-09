import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk 
import random

def start():
    S.configure(state = DISABLED )
    l1.configure(image = frame_2)
    root.after(1000, change1)
    
def change1():
    l1.configure(image = frame_3)
    root.after(500, change2)

def change():
    l1.configure(image = frame_4)
    root.after(500, change2)

def change2():    
    l1.configure(image = frame_5)
    root.after(500, change3)
 
def change3():    
    l1.configure(image = frame_6)
    root.after(500, change4)   

def change4():    
    l1.configure(image = frame_7)
    root.after(500, change5)

def change5():    
    l1.configure(image = frame_8)
    root.after(500, change6)
    
def change6():    
    l1.configure(image = frame_9)
    root.after(500, change7)
    
def change7():    
    l1.configure(image = frame_10)
    root.after(1000, change8)
 
def change8():    
    l1.configure(image = frame_1)
    S.configure(state = NORMAL)

root = Tk()
root.title("Телевизор")
root.configure(bg = "salmon4")
root.geometry("400x280")
root.resizable(width = False, height = False)

frame_1 = ImageTk.PhotoImage(file = "frames/frame_1.jpg")
frame_2 = ImageTk.PhotoImage(file = "frames/frame_2.jpg")
frame_3 = ImageTk.PhotoImage(file = "frames/frame_3.jpg")
frame_4 = ImageTk.PhotoImage(file = "frames/frame_4.jpg")
frame_5 = ImageTk.PhotoImage(file = "frames/frame_5.jpg")
frame_6 = ImageTk.PhotoImage(file = "frames/frame_6.jpg")
frame_7 = ImageTk.PhotoImage(file = "frames/frame_7.jpg")
frame_8 = ImageTk.PhotoImage(file = "frames/frame_8.jpg")
frame_9 = ImageTk.PhotoImage(file = "frames/frame_9.jpg")
frame_10 = ImageTk.PhotoImage(file = "frames/frame_10.jpg")

l1 = Label(root, image = frame_1)
l1.grid(row = 0, column = 0,
 padx = 15, pady = 10, sticky = NW)
 
S = Button(root, width = 5, height = 1, text = "", command = lambda: start(), bg = "red")
S.grid(row = 0, column = 0, sticky = NW, padx = 350, pady = 242)

S1 = Button(root, height = 14, width = 5, text = ":::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::\n::::::::::")
S1.grid(row = 0, column = 0, sticky = NW, padx = 350, pady = 10)
S1.configure(state = DISABLED, bg = "salmon4", disabledforeground = "black")

root.mainloop()