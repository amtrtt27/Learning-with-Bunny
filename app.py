from tkinter import *

win = Tk()
win.geometry('800x800')
win.title('Learning with Bunny')

# Change the background color
win.config(background = '#76D7EA')

class Label():
    def __init__(self):
        self.app_label = Label(win, 'Your Message', 'Arial 18')
        self.app_label.pack(padx = 10, pady = 10)
Label()
win.mainloop()