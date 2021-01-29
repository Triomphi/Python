from tkinter import *
# everything is a widget in tkinter

root = Tk() #create the layout
my_label1 = Label(root, text = 'Hello world!') #create a label
my_label2 = Label(root, text = 'this is my second tkinter work') #create a label

my_label1.grid(row = 0, column = 0)  #grid puts the label on the screen in aspecified row and column space
my_label2.grid(row = 1, column = 1)  

root.mainloop()  #an event loop to know cursor position