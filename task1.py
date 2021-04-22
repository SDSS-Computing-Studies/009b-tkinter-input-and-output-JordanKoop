"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""







import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("Madlibs")
win.geometry("590x260")

def clickStory():
    a = Adj1.get()
    a = str(a)
    b = verb1.get()
    b = str(b)
    c = Adj2.get()
    c = str(c)
    d = Food1.get()
    d = str(d)
    e = Adj3.get()
    e = str(e)
    f = Noun1.get()
    f = str(f)
    g = Fam.get()
    g = str(g)
    h = Food2.get()
    h = str(h)
    i = Adj4.get()
    i = str(i)
    line1 = "Our school cafeteria has really " + a + " food. Just thinking about it makes my stomach " + b +"."
    line2 =  "The spaghetti is " + c +" and tastes like " + d + ". The turkey tacos are totally " + e + " and they look"
    line3 =  "like old " + f + ". My " + g + " said that they would make my lunches, but on the first day,"
    line4 = "I got a sandwich made of " + h + ". I think I'd rather take my chances with the " + i+ " cafeteria!"
    a_entry.delete(0,END)
    b_entry.delete(0,END)
    c_entry.delete(0, END)
    d_entry.delete(0, END)
    a_entry.insert(0, line1)
    b_entry.insert(0, line2)
    c_entry.insert(0, line3)
    d_entry.insert(0, line4)

    
eoutput = StringVar()
eoutput.set("Finished story goes here")

#text variables for inputs
labelFam = StringVar()
labelFam.set("Family Member")

labelFood1 = StringVar()
labelFood1.set("Food")
labelFood2 = StringVar()
labelFood2.set("Food")

labelAdj = StringVar()
labelAdj.set("Adjective")
labelAdj2 = StringVar()
labelAdj2.set("Adjective")
labelAdj3 = StringVar()
labelAdj3.set("Adjective")
labelAdj4 = StringVar()
labelAdj4.set("Adjective")

labelVerb1 = StringVar()
labelVerb1.set ("Verb")

labelNoun = StringVar()
labelNoun.set("Plural Noun (ends in s)")

#text code - adj
label1 = Label(win, text = "Enter four adjectives:")
Adj1 = Entry(win, textvariable=labelAdj)
Adj2 = Entry(win, textvariable=labelAdj2)
Adj3 = Entry(win, textvariable=labelAdj3)
Adj4 = Entry(win, textvariable=labelAdj4)

#text code - verbs
label2 = Label (win, text = "Enter a verb:")
verb1 = Entry (win, textvariable=labelVerb1)

#text code - food
label3 = Label(win, text = "Enter two types of food:")
Food1 = Entry (win, textvariable=labelFood1)
Food2 = Entry (win, textvariable=labelFood2)


#remainder of code
label4 = Label(win, text = "Enter a plural noun")
label5 = Label(win, text = "Enter a family member:")
Noun1 = Entry(win, textvariable = labelNoun)
Fam = Entry(win, textvariable = labelFam)
button1 = Button(win, text = "Show me the story!", command = clickStory)
a_label = Label(win, text = "Here is your story: ", bg = "#63C5DA", relief = RAISED)
a_entry = Entry(win, width = 95, textvariable=eoutput, relief = FLAT)
b_entry = Entry(win, width = 95, relief = FLAT)
c_entry = Entry(win, width = 95, relief = FLAT)
d_entry= Entry(win, width = 95, relief = FLAT)

#adjectives code
label1.grid(row = 1, column = 1, sticky = W)
Adj1.grid(row = 1, column = 2)
Adj2.grid(row = 1, column = 3)
Adj3.grid(row = 2, column = 2)
Adj4.grid(row = 2, column = 3)
#verbs code
label2.grid(row = 3, column = 1, sticky = W)
verb1.grid(row = 3, column = 2)
#food code
label3.grid(row =4 , column = 1, sticky = W)
Food1.grid(row = 4, column =2)
Food2.grid(row = 4, column = 3)
#noun and family
label4.grid(row = 5, column = 1, sticky = W)
Noun1.grid(row =5, column = 2)
label5.grid(row = 6, column = 1, sticky = W)
Fam.grid(row = 6, column = 2)
#remainder
button1.grid(row = 7, column = 2)
a_label.grid(row = 8, column = 1, sticky = W)
a_entry.grid(row = 9, column = 1, columnspan = 3)
b_entry.grid(row = 10, column = 1, columnspan = 3)
c_entry.grid(row = 11, column = 1, columnspan = 3)
d_entry.grid(row = 12, column = 1, columnspan = 3)



win.mainloop()