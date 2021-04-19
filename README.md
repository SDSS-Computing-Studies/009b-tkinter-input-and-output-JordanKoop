## SDSS Computing Studies Python Assignment
### Assignment #009b Input and Output with TKinter (12 marks)

Objectives:
* Get input from a tkinter Entry widget using Entry.get()
* Put data into a tkinter entry widget using Entry.insert()
* Remove contents of an entry widget using Entry.delete()
* Update the contents of a label using textvariable instead of text
* Add an event to a button using the command option

A GUI is supposed to make input and output easier for the user, so
we had better learn how to send and receive data from some of the
widgets.

Today, we will be looking at creating our first event driven programs
that use the command option for button widgets.  This allows us to have
the program execute specific code when the button is clicked.

Some of the code that we will be executing today involves retrieving
data from an Entry widget and doing something with it.  This is how
our GUI will receive its input.  However, we will also need to produce
output, so we will be using the Entry.insert() and Entry.delete()
methods to help us update the contents of an Entry widget.

### 3 Tasks (8 points)

##### Task 1 (4 points)
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment


##### Task 2
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
(4 points) 

