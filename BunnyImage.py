from tkinter import *
from PIL import ImageTk, Image
# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry('800x800')

frame = Frame(win, width = 800, height = 800)
frame.place(anchor = 'c', relx = 0.5, rely = 0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open('image/studybunnylogo.png'))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
win.mainloop()
