from tkinter import *
from tkinter import messagebox
from pygame import mixer
from PIL import ImageTk, Image
import json
import random
import copy

# Initialize, set the geometry and title of the app's window
win = Tk()
win.geometry('800x800')
win.title('Learning with Bunny')

# Change the background color
win.config(background='#76D7EA')


# Import music
# mixer.init()
# mixer.music.load('bunnySound.mp3')
# mixer.music.set_volume(0.1)
# mixer.music.play(-1)

flashcard_score_get = 0
user_data = {}
user = None
topic_choose = {}
word_have = []

box1, box2, box3, box4, box5 = [], [], [], [], []
#########################################################################


def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

#########################################################################


def mainScreen():
    for widgets in win.winfo_children():
        widgets.destroy()

    bunny.background_draw()

    log_in = Button(win, text='Log In', height=1, width=10,
                    font=('Klee', 20, 'bold'),
                    command=Username_log_in_input)
    log_in.place(x=300, y=400)

    sign_up = Button(win, text='Sign Up',
                     height=1, width=10,
                     font=('Klee', 20, 'bold'),
                     command=Username_sign_up_input)
    sign_up.place(x=500, y=400)


class Draw_bunny():
    def __init__(self):
        pass

    def background_draw(self):
        self.label = Label(win, text='Learning With Bunny',
                           font=('Klee', 60, 'bold'),
                           bg='#76D7EA')
        self.label.pack(padx=50, pady=70)

        self.img = Image.open('image/bunnylogo.png')
        self.img_resize = self.img.resize((200, 300), Image.LANCZOS)
        self.new_image = ImageTk.PhotoImage(self.img_resize)
        self.image_Label = Label(win, image=self.new_image, bg='#76D7EA')
        self.image_Label.image = self.new_image
        self.image_Label.place(relx=0.3, rely=0.55, anchor='e')

    def bunny_ask(self):
        for widgets in win.winfo_children():
            widgets.destroy()

        self.img = Image.open('image/bunnylogo.png')
        self.img_resize = self.img.resize((150, 200), Image.LANCZOS)
        self.new_image = ImageTk.PhotoImage(self.img_resize)
        self.image_Label = Label(win, image=self.new_image, bg='#76D7EA')
        self.image_Label.image = self.new_image
        self.image_Label.place(relx=0.2, rely=0.25, anchor='e')


bunny = Draw_bunny()


class Username_sign_up_input():
    def __init__(self):
        for widgets in win.winfo_children():
            widgets.destroy()

        self.user_name_label = Label(win, text='Username:',
                                     font=('Klee', 20, 'bold'),
                                     bg='#76D7EA')

        self.user_name = Entry(win, font=('Klee', 16, 'bold'))

        self.user_password_label = Label(win, text='Password:',
                                         font=('Klee', 20, 'bold'),
                                         bg='#76D7EA')

        self.user_password_label = Label(win, text='Password:',
                                         font=('Klee', 20, 'bold'),
                                         bg='#76D7EA')
        self.user_password_label.place(x=220, y=300)

        self.password = Checkbutton(win, text='Show password',
                                    font=('Klee', 16, 'bold'),
                                    bg='#76D7EA',
                                    command=self.show_password)

        self.cancel_button = Button(win, text='Cancel',
                                    height=1,
                                    width=10,
                                    font=('Klee', 16, 'bold'),
                                    command=mainScreen)

        self.enter_button = Button(win, text='Enter',
                                   height=1,
                                   width=10,
                                   font=('Klee', 16, 'bold'),
                                   command=self.save_new_user_data)

        self.user_name_label.place(x=220, y=200)
        self.user_name.place(x=350, y=200, height=60, width=300)
        self.user_password_label.place(x=220, y=300)
        self.user_password.place(x=350, y=300, height=60, width=300)
        self.password.place(x=350, y=370)
        self.cancel_button.place(x=150, y=450)
        self.enter_button.place(x=550, y=450)

    def show_password(self):
        if self.user_password.cget('show') == '*':
            self.user_password.config(show='')
        else:
            self.user_password.config(show='*')

    def save_new_user_data(self):
        user_data = load_json('user_data.json')

        if self.user_name.get() in user_data:
            warning_message('Account has already existed')

        elif self.user_password.get() == '' or self.user_name.get() == '':
            warning_message('Password or username can not be empty')
        else:
            user_data[self.user_name.get()] = self.user_password.get()
            write_json('user_data.json', user_data)

            user = self.user_name.get()
            after_enter_sign_up_screen()


class Username_log_in_input():
    def __init__(self):
        for widgets in win.winfo_children():
            widgets.destroy()

        self.user_name_label = Label(win, text='Username:',
                                     font=('Klee', 20, 'bold'),
                                     bg='#76D7EA')

        self.user_name = Entry(win, font=('Klee', 16, 'bold'))

        self.user_password_label = Label(win, text='Password:',
                                         font=('Klee', 20, 'bold'),
                                         bg='#76D7EA')

        self.user_password = Entry(win, font=('Klee', 16, 'bold'), show='*')

        self.password = Checkbutton(win, text='Show password',
                                    font=('Klee', 16, 'bold'),
                                    bg='#76D7EA',
                                    command=self.show_password)

        self.cancel_button = Button(win, text='Cancel',
                                    height=1,
                                    width=10,
                                    font=('Klee', 16, 'bold'),
                                    command=mainScreen)

        self.enter_button = Button(win, text='Enter',
                                   height=1,
                                   width=10,
                                   font=('Klee', 16, 'bold'),
                                   command=self.check_valid_user_input)

        self.user_name_label.place(x=220, y=200)
        self.user_name.place(x=350, y=200, height=60, width=300)
        self.user_password_label.place(x=220, y=300)
        self.user_password.place(x=350, y=300, height=60, width=300)
        self.password.place(x=350, y=370)
        self.cancel_button.place(x=150, y=450)
        self.enter_button.place(x=550, y=450)

    def show_password(self):
        if self.user_password.cget('show') == '*':
            self.user_password.config(show='')
        else:
            self.user_password.config(show='*')

    def check_valid_user_input(self):
        user_data = load_json('user_data.json')

        if self.user_name.get() in user_data and self.user_password.get() == user_data[self.user_name.get()]:
            user = self.user_name.get()
            after_enter_log_in_screen()

        else:
            if (warning_message('Incorrect username or password. Do you want to log in again?')):
                Username_log_in_input()
            else:
                mainScreen()


def warning_message(s):
    return messagebox.askretrycancel(title='Warning Error', message=s)

#########################################################################


def after_enter_sign_up_screen():
    for widgets in win.winfo_children():
        widgets.destroy()

    bunny.background_draw()

    practice_or_not = Label(win, text='''Do you want to use Bunny's wordlist \n or create your own?''',
                            font=('Klee', 30, 'bold'),
                            bg='#76D7EA')
    practice_or_not.place(x=240, y=250)

    bunny_wordlist_button = Button(win, text="Bunny's wordlist", height=1,
                                   width=12,
                                   font=('Klee', 16, 'bold'),
                                   bg='#76D7EA',
                                   command=topic_choice_sign_up)
    bunny_wordlist_button.place(x=300, y=450)

    restore_my_dataset = Button(win, text='My wordlist ', height=1,
                                width=12,
                                font=('Klee', 16, 'bold'),
                                bg='#76D7EA',
                                command=add_words)
    restore_my_dataset.place(x=500, y=450)


def topic_choice_sign_up():
    bunny.bunny_ask()

    topic_ask = Label(win, text='Choose your topic!!!',
                      font=('Klee', 50, 'bold'),
                      bg='#76D7EA')
    button_1 = Button(win, text='Job', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Job'))
    button_2 = Button(win, text='Tourism', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Tourism'))
    button_3 = Button(win, text='Environment', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Environment'))
    button_4 = Button(win, text='Education', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Education'))

    topic_ask.place(x=240, y=100)
    button_1.place(x=120, y=310)
    button_2.place(x=420, y=310)
    button_3.place(x=120, y=480)
    button_4.place(x=420, y=480)

    back_button(after_enter_sign_up_screen)

#########################################################################


def after_enter_log_in_screen():
    for widgets in win.winfo_children():
        widgets.destroy()

    bunny.background_draw()

    bunny_wordlist_button = Button(win, text="Bunny's wordlist", height=1,
                                   width=12,
                                   font=('Klee', 16, 'bold'),
                                   bg='#76D7EA',
                                   command=topic_choice_log_in)
    bunny_wordlist_button.place(x=300, y=450)

    restore_my_dataset = Button(win, text='My wordlist ', height=1,
                                width=12,
                                font=('Klee', 16, 'bold'),
                                bg='#76D7EA',
                                command=new_or_old_practice)
    restore_my_dataset.place(x=500, y=450)


def topic_choice_log_in():
    bunny.bunny_ask()

    topic_ask = Label(win, text='Choose your topic!!!',
                      font=('Klee', 50, 'bold'),
                      bg='#76D7EA')

    button_1 = Button(win, text='Job', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Job'))
    button_2 = Button(win, text='Tourism', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Tourism'))
    button_3 = Button(win, text='Environment', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Environment'))
    button_4 = Button(win, text='Education', height=3, width=10,
                      font=('Klee', 25, 'bold'),
                      bg='#76D7EA',
                      command=lambda: practice_option_bunny('Education'))

    topic_ask.place(x=240, y=100)
    button_1.place(x=120, y=310)
    button_2.place(x=420, y=310)
    button_3.place(x=120, y=480)
    button_4.place(x=420, y=480)

    back_button(after_enter_log_in_screen)


def new_or_old_practice():
    for widgets in win.winfo_children():
        widgets.destroy()

    bunny.background_draw()
    new_or_old_practice = Label(win, text='''Do you want to keep practicing \n or add new words?''',
                                font=('Klee', 30, 'bold'),
                                bg='#76D7EA')
    new_or_old_practice.place(x=240, y=250)

    keep_practice_button = Button(win, text='Keep practicing', height=1,
                                  width=12,
                                  font=('Klee', 16, 'bold'),
                                  bg='#76D7EA',
                                  command=practice_option_mywordlist)
    keep_practice_button.place(x=300, y=450)

    add_new_words = Button(win, text='Add new words ', height=1,
                           width=12,
                           font=('Klee', 16, 'bold'),
                           bg='#76D7EA',
                           command=add_words)
    add_new_words.place(x=500, y=450)

    back_button(after_enter_log_in_screen)

#########################################################################


def add_words():
    for widgets in win.winfo_children():
        widgets.destroy()
    word = Label(win, text='Word:',
                 font=('Klee', 20, 'bold'),
                 bg='#76D7EA')
    word.place(x=100, y=200)

    definition = Label(win, text='Definition:',
                       font=('Klee', 20, 'bold'),
                       bg='#76D7EA')
    definition.place(x=100, y=300)

    word_input = Entry(win, font=('Klee', 16, 'bold'))
    word_input.place(x=220, y=200, height=60, width=400)

    definition_input = Text(win, font=('Klee', 16, 'bold'))
    definition_input.place(x=220, y=300, height=200, width=400)

    save_button = Button(win, text='Save',
                         height=1,
                         width=12,
                         font=('Klee', 16, 'bold'))
    save_button.place(x=150, y=550)

    start_practice = Button(win, text='Start to practice',
                            height=1,
                            width=12,
                            font=('Klee', 16, 'bold'))
    start_practice.place(x=450, y=550)

    my_word_list = Button(win, text='My word list',
                          height=1,
                          width=12,
                          font=('Klee', 16, 'bold'))
    my_word_list.place(x=550, y=50)


def practice_option_bunny(topic):
    bunny.bunny_ask()

    global topic_choose, word_have, flashcard_score_get
    topic_choose = {}
    word_have = []
    flashcard_score_get = 0
    topic_choose = load_json('bunny_word_list.json')[topic]

    for word in topic_choose:
        word_have.append(word)

    option_ask = Label(win, text='Do you want to practice by multiple \n choice quesions or flashcards?',
                       font=('Klee', 30, 'bold'),
                       bg='#76D7EA')
    multiple_choice = Button(win, text='Multiple Choice',
                             height=3, width=13,
                             font=('Klee', 25, 'bold'),
                             bg='#76D7EA',
                             command=lambda: multiple_display(0))
    flashcards = Button(win, text='Flashcard',
                        height=3, width=13,
                        font=('Klee', 25, 'bold'),
                        bg='#76D7EA',
                        command=lambda: flashcard_display(0))
    show_list_box = Button(win, text='Show word list',
                           height=2, width=13,
                           font=('Klee', 25, 'bold'),
                           bg='#76D7EA',
                           command=lambda: show_word_list('bunny', topic))
    option_ask.place(x=180, y=100)
    multiple_choice.place(x=120, y=330)
    flashcards.place(x=420, y=330)
    show_list_box.place(x=280, y=480)

    back_button(topic_choice_log_in)


def practice_option_mywordlist():
    bunny.bunny_ask()

    option_ask = Label(win, text='Do you want to practice by multiple \n choice quesions or flashcards?',
                       font=('Klee', 30, 'bold'),
                       bg='#76D7EA')
    option_ask.place(x=180, y=100)

    multiple_choice = Button(win, text='Multiple Choice',
                             height=3, width=13,
                             font=('Klee', 25, 'bold'),
                             bg='#76D7EA',
                             command=lambda: multiple_question(topic_choose))
    flashcards = Button(win, text='Flashcard',
                        height=3, width=13,
                        font=('Klee', 25, 'bold'),
                        bg='#76D7EA',
                        command=lambda: flashcard_display(0))

    back_button(new_or_old_practice)

#########################################################################


def back_button(screenBack):

    back = Image.open('image/backarrow.png')
    back_resize = back.resize((100, 80), Image.LANCZOS)
    new_back = ImageTk.PhotoImage(back_resize)

    back_button = Label(win, image=new_back, bg='#76D7EA')

    back_button.bind('<Button>', lambda e: button_event(screenBack))
    back_button.place(x=30, y=670)
    back_button.image = new_back


def next_button(screenNext):

    next = Image.open('image/nextarrow.png')
    next_resize = next.resize((100, 80), Image.LANCZOS)
    new_next = ImageTk.PhotoImage(next_resize)

    next_button = Label(win, image=new_next, bg='#76D7EA')

    next_button.bind('<Button>', lambda e: button_event(screenNext))
    next_button.place(x=650, y=670)
    next_button.image = new_next


def exit_button(screenExit):
    exit = Image.open('image/exitButton.png')
    exit_resize = exit.resize((60, 60), Image.LANCZOS)
    exit_new = ImageTk.PhotoImage(exit_resize)

    exit_button = Label(win, image=exit_new, bg='#76D7EA')

    exit_button.bind('<Button>', lambda e: button_event(screenExit))
    exit_button.place(x=20, y=10)
    exit_button.image = exit_new


def button_event(event):
    event()

#########################################################################


def multiple_display(multiple_number):
    for widgets in win.winfo_children():
        widgets.destroy()

    temp_word_have = copy.deepcopy(word_have)
    multiple_question(temp_word_have[multiple_number], multiple_number)


def multiple_question(word, multiple_number):
    bunny.bunny_ask()

    ques_ask = Label(win, text=f"Question {multiple_number + 1}: What is the meaning of \n '{word}'?",
                     font=('Klee', 30, 'bold'),
                     bg='#76D7EA')
    ques_ask.place(x=180, y=100)

    random_abcd(multiple_number)

    if multiple_number != len(word_have) - 1:
        next_button(lambda: multiple_display((multiple_number + 1)))

    exit_button(topic_choice_sign_up)


def random_abcd(multiple_number):
    global topic_choose

    temp_topic_choose = copy.deepcopy(topic_choose)

    temp_definition = []
    for word in temp_topic_choose:
        temp_definition.append(temp_topic_choose[word])

    ans = ['A', 'B', 'C', 'D']
    correct_letter = 0
    correct_answer_definition = topic_choose[word_have[multiple_number]]
    temp_definition.remove(topic_choose[word_have[multiple_number]])

    random_answer = [correct_answer_definition]

    for i in range(3):
        ans_def = random.choice(temp_definition)
        temp_definition.remove(ans_def)
        random_answer.append(ans_def)

    random.shuffle(random_answer)

    for i in range(4):
        if random_answer[i] == correct_answer_definition:
            correct_letter = i

    list_button = []
    for i in range(4):
        button = Button(win, text=f'{ans[i]}. {random_answer[i]}', height=2, width=60,
                        font=('Klee', 16, 'bold'),
                        bg='#76D7EA',
                        anchor='w')
        list_button.append(button)
        if i == correct_letter:
            list_button[i].config(command=lambda button=list_button[i], color='green': change_color_button(
                button, color))
        else:
            list_button[i].config(command=lambda button=list_button[i], color='red': change_color_button(
                button, color))

    list_button[0].place(x=120, y=310)
    list_button[1].place(x=120, y=390)
    list_button[2].place(x=120, y=470)
    list_button[3].place(x=120, y=550)


def change_color_button(button, color):
    button.config(fg=color)

#########################################################################


def flashcard_display(flashcard_number):
    for widgets in win.winfo_children():
        widgets.destroy()

    flashcard_frame_word(word_have[flashcard_number], flashcard_number)


def flashcard_frame_word(word, flashcard_number):
    flashcard_frame = Button(win, text=word,
                             font=('Klee', 20, 'bold'),
                             height=10,
                             width=40,
                             bg='white',
                             command=lambda: flashcard_frame_definition(word, flashcard_number))
    flashcard_frame.place(x=135, y=150)

    show_word_number(flashcard_number + 1)

    next_button(lambda: flashcard_score(flashcard_number))

    back_flashcard_number = flashcard_number - 1
    if back_flashcard_number <= 0:
        back_flashcard_number = 0
    back_button(lambda: flashcard_display(back_flashcard_number))

    exit_button(topic_choice_log_in)


def flashcard_frame_definition(word, flashcard_number):
    for widgets in win.winfo_children():
        widgets.destroy()

    flashcard_frame = Button(win, text=f'Definition: \n {topic_choose[word]}',
                             font=('Klee', 20, 'bold'),
                             height=10,
                             width=40,
                             bg='white',
                             command=lambda: flashcard_frame_word(word, flashcard_number))
    flashcard_frame.place(x=135, y=150)

    show_word_number(flashcard_number + 1)

    next_button(lambda: flashcard_score(flashcard_number))

    back_flashcard_number = flashcard_number - 1
    if back_flashcard_number <= 0:
        back_flashcard_number = 0
    back_button(lambda: flashcard_frame_word(
        word_have[back_flashcard_number], back_flashcard_number))

    exit_button(topic_choice_log_in)


def flashcard_score(flashcard_number):
    if (messagebox.askyesno(title='Next?', message='Are you sure you know this word?')):
        global flashcard_score_get
        flashcard_score_get += 1
        next_flashcard_number = (flashcard_number + 1) % len(word_have)
        flashcard_display(next_flashcard_number)


def show_word_number(flashcard_number):
    current_word = Label(win, text=f'Word: {flashcard_number}',
                         font=('Klee', 20, 'bold'),
                         bg='#76D7EA')
    current_word.place(x=650, y=50)

#########################################################################


def show_word_list(bunny_or_user, topic):
    for widgets in win.winfo_children():
        widgets.destroy()

    my_list_box = Listbox(win, width=60, height=17, font=('Klee', 20, 'bold'))
    my_list_box.place(x=30, y=30)

    global topic_choose
    i = 1
    for word in topic_choose:
        my_list_box.insert(END, f'{i}. {word}: {topic_choose[word]}')
        i += 1

    if bunny_or_user == 'bunny':
        back_button(lambda: practice_option_bunny(topic))


class Closing():
    def __init__(self):
        win.protocol('WM_DELETE_WINDOW', self.on_closing)
        win.mainloop()

    def on_closing(self):
        # Message box asks the users if they want to quit
        if messagebox.askyesno(title='Quit?', message='Do you want to save your progress before quitting?'):
            # Save progress before quitting
            win.destroy()


            # mixer.music.stop()
mainScreen()
win.mainloop()
# Closing()
