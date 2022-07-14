 #!/usr/bin/python
 #################################
    #Name: Everlyne 
    #Date: 03/06/2022
    #PASSWORD GENERATOR
###################################
from tkinter import Tk
from tkinter import Label

master = Tk()
master.title("Digital Clock")

# clock = label(master, font = "Calibri`1111111")

from tkinter import *    #means everything in the module

window = Tk()
window.title("Welcome to this new app!")
window.configure(bg = "teal")   #background color
window.geometry("400x400") #fixing the size of the window

lbl = Label(window, text = "First Name:", font = ("Algerian", 20))  #creates the font and size of the text
lbl2 =Label(window, text = "Second Name:", font = ("Algerian", 20))
lbl.grid(column = 60, row = 100) #  .grid gives the position of the lbal
lbl2.grid(column = 60, row = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up Window")
    top.configure(bg = "turquoise")
    msg = Label(top, text = "Welcome to the Pop Up", font = "Gothic")

bt_n = Button(window, text = "CLICK ME!", font = ("Arial", 35), bg = "Violet", fg = "Black")  #the word window is where you want the label or the button you want to be placed
bt_n.pack()
bt_n.grid(column = 100, row = 200)
lbl_box = Entry(window, width = 30)
lbl_box.grid(column = 100, row = 100)
lbl2_box = Entry(window, width =30)
lbl2_box.grid(column = 100, row = 100)

window.mainloop()

#CREATE A DIGITAL AND ANALOG CLOCK
#CREATE A CALCULATOR
#USE FIGMA TO CREATE A LIST OF STUDENT DETAILS
#UPLOASD A PHOTO, DESIGN, USE AT LEAST TWO PAGES