import tkinter as tk
from tkinter import Button, Label, Tk
from PIL import ImageTk

def start_animation():
  start_button.configure(state = "disabled")
  display_label.configure(image = frame_2)
  root.after(1000, show_frame_3)

def show_frame_3():
  display_label.configure(image = frame_3)
  root.after(500, show_frame_4)

def show_frame_4():
  display_label.configure(image = frame_4)
  root.after(500, show_frame_5)

def show_frame_5():
  display_label.configure(image = frame_5)
  root.after(500, show_frame_6)

def show_frame_6():
  display_label.configure(image = frame_6)
  root.after(500, show_frame_7)

def show_frame_7():
  display_label.configure(image = frame_7)
  root.after(500, show_frame_8)

def show_frame_8():
  display_label.configure(image = frame_8)
  root.after(500, show_frame_9)

def show_frame_9():
  display_label.configure(image = frame_9)
  root.after(500, show_frame_10)

def show_frame_10():
  display_label.configure(image = frame_10)
  root.after(1000, reset_animation)

def reset_animation():
  display_label.configure(image = frame_1)
  start_button.configure(state = "normal")

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

display_label = Label(root, image = frame_1)
display_label.grid(row = 0, column = 0, padx = 15, pady = 10, sticky = "nw")

start_button = Button(root, width = 5, height = 1, text = "", command = start_animation, bg = "red")
start_button.grid(row = 0, column = 0, sticky = "nw", padx = 350, pady = 242)

decorative_button = Button(
    root,
    height = 14,
    width = 5,
    text = ":::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::\n"
    "::::::::::",
)

decorative_button.grid(row = 0, column = 0, sticky = "nw", padx = 350, pady = 10)
decorative_button.configure(state = "disabled", bg = "salmon4", disabledforeground = "black")

root.mainloop()
