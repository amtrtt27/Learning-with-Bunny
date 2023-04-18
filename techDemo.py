from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from PIL import ImageTk, Image

######################################################################

# TEST: CREATING BUTTON FOR THE USERS TO CHOOSE THE TOPIC
win = Tk()
win.geometry('600x600')
win.title('Learning with Bunny')
label = Label(win, text = 'Learning with Bunny', font = 'Arial 30')
# Specify the layout 
label.pack(padx = 70, pady = 70)
'''
# Create a text space, you can enter multiple lines
textbox = Text(win, height = 5, font = 'Arial 17')
textbox.pack(padx = 10, pady = 10)

# Receive a single-line text string from the user
# myEntry = Entry(win, width = 100, font = 'Arial 17')
# myEntry.pack()
'''
button = Button(win, text = 'Log In', font = 'Arial 18')
button.pack(padx = 10, pady = 10)

# Initilize a grid button frame
buttonFrame = Frame(win)

# Configure the column index of a grid
buttonFrame.columnconfigure(0, weight = 1)
buttonFrame.columnconfigure(1, weight = 1)
buttonFrame.columnconfigure(2, weight = 1)

# Create a button inside each grid
btn1 = Button(buttonFrame, text = '1', font = 'Arial 18')
# Specify the position of row and column
btn1.grid(row = 0, column = 0, sticky = 'w' + 'e')

btn2 = Button(buttonFrame, text = '2', font = 'Arial 18')
btn2.grid(row = 0, column = 1, sticky = 'w' + 'e')

btn3 = Button(buttonFrame, text = '3', font = 'Arial 18')
btn3.grid(row = 0, column = 2, sticky = 'w' + 'e')

btn4 = Button(buttonFrame, text = '4', font = 'Arial 18')
btn4.grid(row = 1, column = 0, sticky = 'w' + 'e')

btn5 = Button(buttonFrame, text = '5', font = 'Arial 18')
btn5.grid(row = 1, column = 1, sticky = 'w' + 'e')

btn6 = Button(buttonFrame, text = '6', font = 'Arial 18')
btn6.grid(row = 1, column = 2, sticky = 'w' + 'e')

buttonFrame.pack(fill = 'x')

# Other method to change the button's position manually
# anotherbtn = Button(win, text = 'TEST')
# anotherbtn.place(x = 200, y = 200, height = 100, width = 100)
# win.mainloop()

#######################################################################
'''
# TEST: TEXT BOX AND CLOSE WINDOW
class MyGUI(object):
    def __init__(self):
        self.win = Tk()

        self.label = Label(self.win, text = 'Your Message', font = 'Arial 18')
        self.label.pack(padx = 10, pady = 10)

        self.textbox = Text(self.win, font = 'Arial 16')
        self.textbox.pack(padx = 10, pady = 10)

        self.clearbtn = Button(self.win, text = 'Clear', font = 'Arial 18', command = self.clear)
        self.clearbtn.pack(padx = 10, pady =10)

        # IntVar holds int data where can we set int data and retrieve it later, default = 0
        self.check_state = IntVar()

        # CheckButton allows user select many options without uncheck the checked ones
        self.check = Checkbutton(self.win, text = 'Show Messagebox', font = 'Arial 16', variable = self.check_state)
        self.check.pack(padx = 10, pady = 10)

        # RadioButton allows user select only 1 option
        
        self.button = Button(self.win, text = 'Show Message', font = 'Arial 18', command = self.show_message)
        self.button.pack(padx = 10, pady = 10)

        # Method helps the app interacts with the window manager
        self.win.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.win.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:

            # get method takes 2 parameters, starting and ending points
            print(self.textbox.get('1.0', END))
        
        # show the message box window
        else:
            messagebox.showinfo(title = 'Message', message = self.textbox.get('1.0', END))

    def on_closing(self):

        # Message box asks the users if they want to quit
        if messagebox.askyesno(title = 'Quit?', message = 'Do you really want to quit?'):
            self.win.destroy()

    def clear(self):
        self.textbox.delete('1.0', END)
MyGUI()

'''
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

######################################################################
'''
# TEST: IMPORT IMAGE
canvas = Canvas(win, width = 800, height = 800)
canvas.pack()
canvas.place(anchor = 'c', relx = 0.5, rely = 0.5)

# Create an object of tkinter ImageTk: Bunny
img = Image.open('image/bunnylogo.png')
img_resize = img.resize((200, 300), Image.LANCZOS)
new_image = ImageTk.PhotoImage(img_resize)

# Create an object: Bunny's message
# img1 = Image.open('image/cloudMessage.png')
# img_resize1 = img1.resize((600, 300), Image.LANCZOS)
# new_image1 = ImageTk.PhotoImage(img_resize1)

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
'''
win.mainloop()
