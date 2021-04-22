"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""


import tkinter as tk 
from tkinter import *
import math
win = tk.Tk()
win.title("Factoring Trinomials")
#textvaribles
binput = StringVar()
cinput = StringVar()
eoutput = StringVar()
eoutput.set("Answer will be put here!")
#instructions
inst1 = Label (win, text = "Today we are going to factor trinomials. \n 1. Enter two values for the b-coefficient and c-coefficient. \n 2. Hit the factor button and the answer will appear. \n *** If you want to make the b or c values negative, select it in the dropmenu.*** \n      ", anchor = W, justify = LEFT)
entry = Label(win, text = "Enter your values:")
#entry boxes
a = Label (win, text = "x^2 ")
bentry = Entry (win, textvariable = binput, width = 3)
b = Label (win, text = "x")
centry = Entry (win, textvariable = cinput, width = 3)
#dropdown boxes
option1 = StringVar(win)
option1.set("+")
option2 = StringVar(win)
option2.set("+")
w = OptionMenu(win, option1, "+", "-")
w2 = OptionMenu(win, option2, "+", "-")
def quadratic():
    b = int(bentry.get())
    c = int(centry.get())
    bsign = option1.get()
    csign = option2.get()
    if bsign == "-" and csign == "+":
        b = b*-1
        d = (b**2) - (4*c)
    elif bsign == "-" and csign == "-":
        c = c*(-1)
        b = b*(-1)
        d = (b**2) - (4*c)
    elif bsign == "+" and csign == "-":
        c = c*(-1)
        d = (b**2) - (4*c)
    else:
        d = (b**2) - (4*c)
    answer1 = (-b-math.sqrt(d))/(2)
    answer2 = (-b+math.sqrt(d))/(2)
    answer1 = round(answer1, 5)
    answer2 = round(answer2, 5)
    if answer1 > 0:
        x = "(x " + str(answer1*-1) + ")"
    elif answer1 < 0:
        v = answer1*(-1)
        x = "(x + " + str(answer1*-1) + ")"
    elif answer == 0:
        x = "(x)"
    if answer2 > 0:
        y = "(x " + str(answer2*-1) + ")"
    elif answer2 < 0:
        y = "(x +" + str(answer2*-1) + ")"
    elif amswer2 == 0:
        y = "(x)"
    line = x +" " + y
    line2 = "  The values of x:  " + str(answer1) +" and " + str(answer2)
    a_entry.delete(0,END)
    a_entry.insert(0, line + line2)
#bottomcode
bottomcode = Label(win, text = "\n ")
button1 = Button(win, text = "Solve!", command = quadratic)
a_entry = Entry(win, width = 40, textvariable=eoutput, relief = FLAT)
#grid
inst1.grid(row = 1, column = 1, columnspan = 15)
entry.grid( row = 6, column = 1, columnspan = 2, sticky = W)
a.grid(row = 7, column = 1, sticky = E)
w.grid(row = 7, column = 2)
bentry.grid(row = 7, column = 3, sticky = E)
b.grid(row = 7, column = 4, sticky = W)
w2.grid(row = 7, column = 5)
centry.grid (row = 7, column = 6, sticky = E)
bottomcode.grid (row = 8, column = 1)
button1.grid(row = 9, column = 1)
a_entry.grid(row = 10, column = 1, columnspan = 4, sticky = W)

win.mainloop()