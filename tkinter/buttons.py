from tkinter import *
# everything is a widget in tkinter

root = Tk() #create the layout
def myClick():
    my_label = Label(root, text = 'you\'ve sucessfully submitted!')
    my_label.pack()

#create a button that has play again as its identifier and runs the comman in the myClick function
my_button = Button(root, text = 'Submit', command = myClick, fg ='white', bg = 'purple')
my_button.pack()  #display the button
#fg adds colour to foreground, bg adds colour to background
#my_button = Button(root, text = 'Submit', command = myClick, state = DISABLED, padx = 50, pady=30)
#state disables the button making it unclickable, padx and pady hepl resize the x and y axis of the button

root.mainloop()  #an event loop to know cursor position