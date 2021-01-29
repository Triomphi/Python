from tkinter import *
# everything is a widget in tkinter
from PIL import ImageTk, Image #pythons library for images
root = Tk() #create the layout 
root.title('Simple Calculator')
#adding an icon 
#root.iconbitmap('C:/Users/defaultuser0/Desktop/tkinter/apple-touch-icon-144x144.ico')

#adding images
img1 = ImageTk.PhotoImage(Image.open('DC.png'))
label1 = Label(image = img1)
label1.pack()

#exit button
button_quit = Button(root, text = 'Exit', command = root.quit)
button_quit.pack()

#using images

root.mainloop()