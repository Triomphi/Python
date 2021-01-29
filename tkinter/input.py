from tkinter import *
# everything is a widget in tkinter
root = Tk() #create the layout
User_input = Entry(root, width = 50, borderwidth = 5 ) #accept users input
User_input.pack() #display space for users input 
User_input.insert(0, 'Enter your fist name: ') #works just like a place holder for the first input box

def myClick():
    msg = 'Hi ' + User_input.get() + ' your account has been created'  #.get() retrives the user input 
    my_label = Label(root, text = msg)
    my_label.pack()

#create a button that has play again as its identifier and runs the comman in the myClick function
my_button = Button(root, text = 'Submit', command = myClick, fg ='white', bg = 'purple')
my_button.pack()  #display the button
#fg adds colour to foreground, bg adds colour to background
#my_button = Button(root, text = 'Submit', command = myClick, state = DISABLED, padx = 50, pady=30)
#state disables the button making it unclickable, padx and pady hepl resize the x and y axis of the button

root.mainloop()  #an event loop to know cursor position