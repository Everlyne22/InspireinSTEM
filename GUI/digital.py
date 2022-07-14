
from tkinter import *

import time  

root = Tk()
root.title("My Digital Clock")
root.geometry("350x100")

def current_time():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + ":" + am_or_pm
    lbl.config(text = time_text)
    lbl.after(1000, current_time)

lbl = Label(root, text = "00:00:00" font = ("Algerian Italics", 80), bg = "Black", fg = "cyan")
lbl.pack(anchor = "center")
current_time()

root.mainloop()