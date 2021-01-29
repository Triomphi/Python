from tkinter import *
# everything is a widget in tkinter

root = Tk() #create the layout
my_label = Label(root, text = 'Hello world!') #create a label
my_label.pack()  #put the label on the screen in the first available space

root.mainloop()  #an event loop to know cursor position