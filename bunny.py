from tkinter import *
from tkinter import messagebox, font, ttk

from PIL import ImageTk, Image

# Initialize, set the geometry and title of the app's window
win = Tk()
win.geometry('800x800')
win.title('Learning with Bunny')

# Change the background color
win.config(background = '#76D7EA')

def mainScreen():
    for widgets in win.winfo_children():
            widgets.destroy()
    
    bunny.background_draw() 

    log_in = Button(win, text = 'Log In', height = 1, width = 10,
                            font = ('Klee', 20, 'bold'),
                            command = Username_input)
    log_in.place(x = 300, y = 400)

    sign_up = Button(win, text = 'Sign Up', 
                            height = 1, width = 10, 
                            font = ('Klee', 20, 'bold'),
                            command = Username_input)
    sign_up.place(x = 500, y = 400)  

class Draw_bunny():
    def __init__(self):
        pass

    def background_draw(self):
        self.label = Label(win, text = 'Learning With Bunny', 
                            font = ('Klee', 60, 'bold'), 
                            bg = '#76D7EA')
        self.label.pack(padx = 50, pady = 70)

        self.img = Image.open('image/bunnylogo.png')
        self.img_resize = self.img.resize((200, 300), Image.LANCZOS)
        self.new_image = ImageTk.PhotoImage(self.img_resize)
        self.image_Label = Label(win, image = self.new_image, bg = '#76D7EA')
        self.image_Label.image = self.new_image
        self.image_Label.place(relx = 0.3, rely = 0.55, anchor ='e')

    def bunny_ask(self):
        for widgets in win.winfo_children():
            widgets.destroy()
            
        self.img = Image.open('image/bunnylogo.png')
        self.img_resize = self.img.resize((150, 200), Image.LANCZOS)
        self.new_image = ImageTk.PhotoImage(self.img_resize)
        self.image_Label = Label(win, image = self.new_image, bg = '#76D7EA')
        self.image_Label.image = self.new_image
        self.image_Label.place(relx = 0.2, rely = 0.2, anchor ='e')

bunny = Draw_bunny()

class Username_input():
    def __init__(self):
        for widgets in win.winfo_children():
            widgets.destroy()
        
        self.user_name_label = Label(win, text = 'Username:', 
                                font = ('Klee', 20, 'bold'), 
                                bg = '#76D7EA')
        self.user_name_label.place(x = 220, y = 200)

        self.user_name = Entry(win, font = ('Klee', 16, 'bold'))
        self.user_name.place(x = 350, y = 200, height = 60, width = 300)

        self.user_password_label = Label(win, text = 'Password:', 
                                            font = ('Klee', 20, 'bold'), 
                                            bg = '#76D7EA')
        self.user_password_label.place(x = 220, y = 300)

        self.user_password = Entry(win, font = ('Klee', 16, 'bold'), show = '*')

        self.user_password.place(x = 350, y = 300, height = 60, width = 300)

        self.password = Checkbutton(win, text = 'Show password', 
                                            font = ('Klee', 16, 'bold'), 
                                            bg = '#76D7EA', 
                                            command = self.show_password)
        self.password.place(x = 350, y = 370)

        self.cancel_button = Button(win, text = 'Cancel', 
                                        height = 1, 
                                        width = 10,
                                        font = ('Klee', 16, 'bold'),
                                        command = mainScreen)
        self.cancel_button.place(x = 150, y = 450)

        self.enter_button = Button(win, text = 'Enter', 
                                        height = 1, 
                                        width = 10,
                                        font = ('Klee', 16, 'bold'),
                                        command = after_enter_screen)
        self.enter_button.place(x = 550, y = 450)

    def show_password(self):
        if self.user_password.cget('show') == '*':
            self.user_password.config(show = '')
        else:
            self.user_password.config(show = '*')

def after_enter_screen():
    for widgets in win.winfo_children():
            widgets.destroy()

    bunny.background_draw()
    
    practice_or_not = Label(win, text = '''Do you want to use Bunny's wordlist \n or restore your progress?''', 
                                font = ('Klee', 30, 'bold'),
                                bg = '#76D7EA')
    practice_or_not.place(x = 240, y = 250)

    bunny_wordlist_button = Button(win, text = "Bunny's wordlist", height = 1, 
                                    width = 12,
                                    font = ('Klee', 16, 'bold'),
                                    bg = '#76D7EA',
                                    command = topic_choice)
    bunny_wordlist_button.place(x = 300, y = 450)

    restore_my_dataset = Button(win, text = 'Your wordlist ', height = 1, 
                                    width = 12,
                                    font = ('Klee', 16, 'bold'),
                                    bg = '#76D7EA')
    restore_my_dataset.place(x = 500, y = 450)

def topic_choice():
    bunny.bunny_ask()

    topic_ask = Label(win, text = 'Choose your topic!!!',
                        font = ('Klee', 50, 'bold'),
                        bg = '#76D7EA')
    topic_ask.place(x = 240, y = 100)

    button_1 = Button(win, text = 'Animals', height = 3, width = 10, 
                                    font = ('Klee', 25, 'bold'),
                                    bg = '#76D7EA',
                                    command = practice_option)
    button_2 = Button(win, text = 'Tourism', height = 3, width = 10, 
                                    font = ('Klee', 25, 'bold'),
                                    bg = '#76D7EA',
                                    command = practice_option)
    button_3 = Button(win, text = 'Environment', height = 3, width = 10, 
                                    font = ('Klee', 25, 'bold'),
                                    bg = '#76D7EA',
                                    command = practice_option)
    button_4 = Button(win, text = 'Education', height = 3, width = 10, 
                                    font = ('Klee', 25, 'bold'),
                                    bg = '#76D7EA',
                                    command = practice_option)

    button_1.place(x = 120, y = 310)
    button_2.place(x = 420, y = 310)
    button_3.place(x = 120, y = 480)
    button_4.place(x = 420, y = 480)

def practice_option():
    bunny.bunny_ask()

    option_ask = Label(win, text = 'Do you want to practice by multiple \n choice quesions or flashcards?',
                            font = ('Klee', 30, 'bold'),
                            bg = '#76D7EA')
    option_ask.place(x = 180, y = 100)
    
    multiple_choice = Button(win, text = 'Multiple Choice', 
                                height = 3, width = 13,
                                font = ('Klee', 25, 'bold'),
                                bg = '#76D7EA')
    flashcards = Button(win, text = 'Flashcard', 
                                height = 3, width = 13,
                                font = ('Klee', 25, 'bold'),
                                bg = '#76D7EA')

    multiple_choice.place(x = 120, y = 330)
    flashcards.place(x = 420, y = 330)

class Closing():
    def __init__(self):
        win.protocol('WM_DELETE_WINDOW', self.on_closing)
        win.mainloop()

    def on_closing(self):
        # Message box asks the users if they want to quit
        if messagebox.askyesno(title = 'Quit?', message = 'Do you want to save your progress before quitting?'):
            # Save progress before quitting
            win.destroy()
mainScreen()
