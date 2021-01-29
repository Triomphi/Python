from tkinter import *
# everything is a widget in tkinter
root = Tk() #create the layout 
root.title('Simple Calculator')

User_input = Entry(root, width = 35, borderwidth = 7 ) #accept users input
User_input.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady= 15) #display space for users input 

def button_click(number):
    current = User_input.get()
    User_input.delete(0, END)
    User_input.insert(0, str(current) + str(number)) 
    
def button_clear():
    User_input.delete(0, END)

num_1 = None
math = None 
def button_add():
    global num_1
    global math 
    math = "addition"
    num1 = User_input.get()
    num_1 = float(num1)
    User_input.delete(0, END)

def button_equal():
    num2 = User_input.get()
    User_input.delete(0, END)
    
    if math == "addition":
        User_input.insert(0, num_1 + float(num2))
    if math == "subtract":
        User_input.insert(0, num_1 - float(num2))
    if math == "multiply":
        User_input.insert(0, num_1 * float(num2))
    if math == "divide":
        User_input.insert(0, num_1 / float(num2))
    
def button_subtract():
    global num_1
    global math 
    math = "subtract"
    num1 = User_input.get()
    num_1 = float(num1)
    User_input.delete(0, END)

def button_multiply():
    global num_1
    global math 
    math = "multiply"
    num1 = User_input.get()
    num_1 = float(num1)
    User_input.delete(0, END)

def button_divide():
    global num_1
    global math 
    math = "divide"
    num1 = User_input.get()
    num_1 = float(num1)
    User_input.delete(0, END)

#define buttons
button1 = Button(root, text = '1', padx = 30, pady = 20, command = lambda: button_click(1))
button2 = Button(root, text = '2', padx = 30, pady = 20, command = lambda: button_click(2))
button3 = Button(root, text = '3', padx = 30, pady = 20, command = lambda: button_click(3))
button4 = Button(root, text = '4', padx = 30, pady = 20, command = lambda: button_click(4))
button5 = Button(root, text = '5', padx = 30, pady = 20, command = lambda: button_click(5))
button6 = Button(root, text = '6', padx = 30, pady = 20, command = lambda: button_click(6))
button7 = Button(root, text = '7', padx = 30, pady = 20, command = lambda: button_click(7))
button8 = Button(root, text = '8', padx = 30, pady = 20, command = lambda: button_click(8))
button9 = Button(root, text = '9', padx = 30, pady = 20, command = lambda: button_click(9))
button0 = Button(root, text = '0', padx = 30, pady = 20, command = lambda: button_click(0))
button_point = Button(root, text = '.', padx = 30, pady = 20, command = lambda: button_click('.'))
button_add = Button(root, text = '+', padx = 30, pady = 20, command = button_add)
button_subtract = Button(root, text = '-', padx = 30, pady = 20, command = button_subtract)
button_multiply = Button(root, text = '*', padx = 30, pady = 20, command = button_multiply)
button_divide = Button(root, text = '/', padx = 30, pady = 20, command = button_divide)
button_equal = Button(root, text = '=', padx = 150, pady = 10, command = button_equal)
button_clear = Button(root, text = 'C', padx = 30, pady = 20, command = button_clear)

#put buttons on the screen
button1.grid(row = 3, column =0)
button2.grid(row = 3, column =1)
button3.grid(row = 3, column =2)
 
button4.grid(row = 2, column =0)
button5.grid(row = 2, column =1)
button6.grid(row = 2, column =2)
 
button7.grid(row = 1, column =0)
button8.grid(row = 1, column =1)
button9.grid(row = 1, column =2)
 
button0.grid(row = 4, column =1)
button_point.grid(row = 4, column =0)
button_clear.grid(row = 4, column =2)
button_equal.grid(row = 5, column = 0, columnspan = 4)

button_add.grid(row = 1, column =3)
button_subtract.grid(row = 2, column =3)
button_multiply.grid(row = 3, column =3)
button_divide.grid(row = 4, column =3)

root.mainloop()  #an event loop to know cursor position