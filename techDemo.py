from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry('800x800')
canvas = Canvas(win, width = 800, height = 800)
canvas.pack()
canvas.place(anchor = 'c', relx = 0.5, rely = 0.5)

# Create an object of tkinter ImageTk: Bunny
img = Image.open('image/studybunnylogo.png')
img_resize = img.resize((200, 300), Image.LANCZOS)
new_image = ImageTk.PhotoImage(img_resize)

# Create an object: Bunny's message
img1 = Image.open('image/cloudMessage.png')
img_resize1 = img1.resize((600, 300), Image.LANCZOS)
new_image1 = ImageTk.PhotoImage(img_resize1)

# Create button
turn_off = Button(win, text = 'X', bg = 'red')
turn_off.pack()
turn_off.place(x = 0, y = 0)

log_in = ttk.Button(win, text = 'Log In')
log_in.place(x = 300, y = 400)

sign_up = ttk.Button(win, text = 'Sign Up')
sign_up.place(x = 500, y = 400)

# Create a Label Widget to display the text or Image
canvas.create_rectangle(0, 0, 800, 800, fill = rgbString(118, 215, 234), outline = '')
canvas.create_image(10, 300, anchor = 'nw', image = new_image)

canvas.create_text(100, 130, anchor = 'nw', text = 'Learning with Bunny',
                    font = 'Consolas 60 bold')



#canvas.create_image(150, 100, anchor = 'nw', image = new_image1)
#canvas.create_text(150, 100, text = '')
win.mainloop()
