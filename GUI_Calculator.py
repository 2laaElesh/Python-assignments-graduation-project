from tkinter import *

# click_button function: used to continuously update the input field whenever you enter a number
def click_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# clear_button function: used to clear the input field

def clear_button(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# evaluate function: used to calculate the expression in input field
 
def evaluate():
    global expression
    result = str(eval(expression)) # eval is used to evaluate the string expression directly
    input_text.set(result)
    expression = ""
 
 # Defining a variable for the input expression - empty string -
expression = ""
 
# ---------------------------------------------------------------------------------------------------

# Creating a basic window
window = Tk() 
#Setting the window size
window.geometry("330x325") 
# Preventing window from resizing
window.resizable(0, 0)  
# Adding a name to the window
window.title("Simple Calculator")

# ---------------------------------------------------------------------------------------------------
 
# Creating a frame for the input field
input_frame = Frame(window, width=50, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)

# StringVar() is used to get the instance of input field
input_text = StringVar()
 
# Create an input field inside the input frame
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=24, bg="white", bd=0, justify=LEFT)
input_field.grid(row=0, column=0)
 # 'ipady' is internal padding to increase the height of input field
input_field.pack(ipady=10) 
 
# Creating another 'Frame' for the button inside the input_frame
btns_frame = Frame(window, width=350, height=350, bg="grey")
btns_frame.pack()

# Defining the buttons of the first row
right_b=Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("("))
right_b.grid(row = 0, column = 0, padx = 1, pady = 1)
left_b=Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button(")"))
left_b.grid(row = 0, column = 1, padx = 1, pady = 1)
clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clear_button())
clear.grid(row = 0, column = 2, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",cursor = "hand2", command = lambda: click_button("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
 
# Defining the buttons of the second row
seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
 
# Defining the buttons of the third row
four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
 
# Defining the buttons of the fourth row
one = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
 
# Defining the buttons of the fifth row
zero = Button(btns_frame, text = "0", fg = "white", width = 21, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(0))
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
D_point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("."))
D_point.grid(row = 4, column = 2, padx = 1, pady = 1)
equal = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: evaluate())
equal.grid(row = 4, column = 3, padx = 1, pady = 1)
 
# ---------------------------------------------------------------------------------------------------
 
 
 # Call the main loop which is used when the application is ready to run to keep the code displaying 
window.mainloop()
