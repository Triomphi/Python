from tkinter import *
from random import randint
from PIL import ImageTk, Image
# everything is a widget in tkinter
root = Tk() #create the layout 
root.title('Dice Roller')
root.geometry("500x400")
root.configure(bg="Lime Green")

images =[]
def roll():
    num1 = randint(0,5)
    num2 = randint(0,5)
    label1.configure(image = images[num1])
    label2.configure(image = images[num2])
    return

img = ImageTk.PhotoImage(Image.open('images/dice1.jpeg'))
images.append(img)
img = ImageTk.PhotoImage(Image.open('images/dice2.jpeg'))
images.append(img)
img = ImageTk.PhotoImage(Image.open('images/dice3.jpeg'))
images.append(img)
img = ImageTk.PhotoImage(Image.open('images/dice4.jpeg'))
images.append(img)
img = ImageTk.PhotoImage(Image.open('images/dice5.jpeg'))
images.append(img)
img = ImageTk.PhotoImage(Image.open('images/dice6.jpeg'))
images.append(img)

label1 = Label(root, image=img, bg = 'Lime Green')
label1.grid(column = 0, row = 0, padx  = 10, pady = 10)
label2 = Label(root, image=img, bg = 'Lime Green')
label2.grid(column = 1, row = 0, padx  = 10, pady = 10)

#roll button
button_roll = Button(root, text = 'Roll Dice', command = roll, bg = 'Dark Green', fg = 'white', padx = 20, pady = 10)
button_roll.grid(column = 0, row = 1, columnspan = 2)


root.mainloop()