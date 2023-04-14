from tkinter import *
from tkinter import messagebox
from pygame import mixer
from PIL import ImageTk, Image
import json
import random
import copy
import time as Time

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


# Initialize, set the geometry and title of the app's window
win = Tk()
win.geometry('800x800')
win.title('Learning with Bunny')

# Change the background color
win.config(background='#76D7EA')

#########################################################################

# Import music
# mixer.init()
# mixer.music.load('bunnySound.mp3')
# mixer.music.set_volume(0.1)
# mixer.music.play(-1)

########################################################################

user_data = {}
user = None
topic = None
topic_choose = {}
word_have = []

# box - 0 review everytime
# box - 1 review after 2 time
# box - 2 review after 5 times
# box - 3 review after 10 times
# box - 4 review after 20 times
user_checkin_count = load_json('user_checkin_count.json')
bunny_wordlist_box = load_json('bunny_wordlist_box.json')
user_wordlist_box = load_json('user_wordlist_box.json')
user_wordlist = load_json('user_wordlist.json')
bunny_wordlist_box_temp = copy.deepcopy(bunny_wordlist_box)
user_wordlist_box_temp = copy.deepcopy(user_wordlist_box)
user_checkin_count_temp = copy.deepcopy(user_checkin_count)
user_wordlist_temp = copy.deepcopy(user_wordlist)
MCQ_count = {}
word_have_mcq = []
times = [1, 2, 5, 10, 20]

##################################################################


def mainScreen():
    for widgets in win.winfo_children():
        widgets.destroy()

    bunny.background_draw()

    log_in = Button(win, text='Log In', height=1, width=10,
                    font=('Klee', 20, 'bold'),
                    command=Username_log_in_input)

    sign_up = Button(win, text='Sign Up',
                     height=1, width=10,
                     font=('Klee', 20, 'bold'),
                     command=Username_sign_up_input)

    log_in.place(x=300, y=400)
    sign_up.place(x=500, y=400)


class Draw_bunny():
    def __init__(self):
        pass

    def background_draw(self):
        self.label = Label(win, text='Learning With Bunny',
                           font=('Klee', 60, 'bold'),
                           bg='#76D7EA')

        self.img = Image.open('image/bunnylogo.png')
        self.img_resize = self.img.resize((200, 300), Image.LANCZOS)
        self.new_image = ImageTk.PhotoImage(self.img_resize)
        self.image_Label = Label(win, image=self.new_image, bg='#76D7EA')
        self.image_Label.image = self.new_image

        self.label.pack(padx=50, pady=70)
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

            global user, bunny_wordlist_box, user_wordlist_box, user_checkin_count, user_wordlist_box_temp, bunny_wordlist_box_temp, user_checkin_count_temp, user_wordlist, user_wordlist_temp
            user = self.user_name.get()

            bunny_wordlist_box[user] = {}
            user_wordlist_box[user] = {}
            user_checkin_count[user] = 0
            user_wordlist[user] = {}

            user_wordlist_box_temp = copy.deepcopy(user_wordlist_box)
            bunny_wordlist_box_temp = copy.deepcopy(bunny_wordlist_box)
            user_checkin_count_temp = copy.deepcopy(user_checkin_count)
            user_wordlist_temp = copy.deepcopy(user_wordlist)
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
        global user_data
        user_data = load_json('user_data.json')

        if self.user_name.get() in user_data and self.user_password.get() == user_data[self.user_name.get()]:
            global user, user_checkin_count
            user = self.user_name.get()
            user_checkin_count[user] += 1
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

    bunny_wordlist_button = Button(win, text="Bunny's wordlist", height=1,
                                   width=12,
                                   font=('Klee', 16, 'bold'),
                                   bg='#76D7EA',
                                   command=topic_choice_sign_up)

    restore_my_dataset = Button(win, text='My wordlist ', heigh=1,
                                width=12,
                                font=('Klee', 16, 'bold'),
                                bg='#76D7EA',
                                command=add_words)

    practice_or_not.place(x=240, y=250)
    bunny_wordlist_button.place(x=300, y=450)
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

    create_or_bunny = Label(win, text="Do you want to use \n Bunny's wordlist or yours?",
                            font=('Klee', 30, 'bold'),
                            bg='#76D7EA')

    bunny_wordlist_button = Button(win, text="Bunny's wordlist", height=1,
                                   width=12,
                                   font=('Klee', 16, 'bold'),
                                   bg='#76D7EA',
                                   command=topic_choice_log_in)

    restore_my_dataset = Button(win, text='My wordlist ', height=1,
                                width=12,
                                font=('Klee', 16, 'bold'),
                                bg='#76D7EA',
                                command=new_or_old_practice)

    create_or_bunny.place(x=270, y=250)
    bunny_wordlist_button.place(x=300, y=450)
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

    new_or_old_practice.place(x=240, y=250)
    add_new_words.place(x=500, y=450)

    keep_practice_button.config(state=DISABLED)

    if len(user_wordlist[user]) != 0:
        keep_practice_button.config(state=NORMAL)

    back_button(after_enter_log_in_screen)

#########################################################################


def add_words():
    for widgets in win.winfo_children():
        widgets.destroy()

    word = Label(win, text='Word:',
                 font=('Klee', 20, 'bold'),
                 bg='#76D7EA')

    definition = Label(win, text='Definition:',
                       font=('Klee', 20, 'bold'),
                       bg='#76D7EA')

    word_input = Entry(win, font=('Klee', 16, 'bold'))

    definition_input = Entry(win, font=('Klee', 16, 'bold'))

    start_practice = Button(win, text='Start to practice',
                            height=1,
                            width=12,
                            font=('Klee', 16, 'bold'),
                            command=practice_option_mywordlist)

    save_button = Button(win, text='Save',
                         height=1,
                         width=12,
                         font=('Klee', 16, 'bold'),
                         command=lambda: save_word_into_wordlist(word_input.get(), start_practice, definition_input.get()))

    my_word_list = Button(win, text='My word list',
                          height=1,
                          width=12,
                          font=('Klee', 16, 'bold'),
                          command=lambda: show_word_list('user', ''))

    word.place(x=100, y=200)
    definition.place(x=100, y=300)
    word_input.place(x=220, y=200, height=60, width=400)
    definition_input.place(x=220, y=300, height=200, width=400)
    save_button.place(x=150, y=550)
    start_practice.place(x=450, y=550)
    my_word_list.place(x=550, y=50)

    start_practice.config(state=DISABLED)

    if len(user_wordlist[user]) != 0:
        save_button.config(state=NORMAL)


def save_word_into_wordlist(word, button, definition):
    global user_wordlist, user, user_wordlist_box, topic_choose
    if word not in user_wordlist[user]:
        user_wordlist[user][word] = definition
        user_wordlist_box[user][word] = 0

        topic_choose[word] = definition
    else:
        warning_message(
            "You have added that word already. Please go to user_wordlist.json to verify it.")
    button.config(state=NORMAL)


def practice_option_bunny(Topic):
    bunny.bunny_ask()

    global topic_choose, word_have, flashcard_score_get, bunny_wordlist_box, user, topic, word_have_mcq, MCQ_count
    topic = Topic
    topic_choose = {}
    word_have = []
    word_have_mcq = []
    flashcard_score_get = 0
    topic_choose = load_json('bunny_word_list.json')[topic]

    if topic not in bunny_wordlist_box[user]:
        bunny_wordlist_box[user][topic] = {}
        for word in topic_choose:
            bunny_wordlist_box[user][topic][word] = 0

    for word in bunny_wordlist_box[user][topic]:
        word_have_mcq.append(word)
        if user_checkin_count[user] % times[bunny_wordlist_box[user][topic][word]] == 0:
            word_have.append(word)

    random.shuffle(word_have_mcq)
    random.shuffle(word_have)

    for word in word_have_mcq:
        MCQ_count[word] = 0

    option_ask = Label(win, text='Do you want to practice by multiple \n choice quesions or flashcards?',
                       font=('Klee', 30, 'bold'),
                       bg='#76D7EA')

    multiple_choice = Button(win, text='Multiple Choice',
                             height=3, width=13,
                             font=('Klee', 25, 'bold'),
                             bg='#76D7EA',
                             command=lambda: multiple_display(0, topic_choose, 'bunny'))

    flashcards = Button(win, text='Flashcard',
                        height=3, width=13,
                        font=('Klee', 25, 'bold'),
                        bg='#76D7EA',
                        command=lambda: screen_before_display_flashcard('bunny'))

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

    global user_wordlist

    if len(user_wordlist) == 0:
        bunny.bunny_ask()

        inform = Label(win, text='You do not have any words. \n Do you want to add?',
                       font=('Klee', 40, 'bold'),
                       bg='#76D7EA')

        yes_button = Button(win, text='Yes', font=('Klee', 20, 'bold'),
                            width=10, height=3,
                            command=add_words)

        no_button = Button(win, text='No', font=('Klee', 20, 'bold'),
                           width=10, height=3,
                           command=after_enter_log_in_screen)

        inform.place(x=180, y=100)
        yes_button.place(x=120, y=330)
        no_button.place(x=420, y=330)

    else:
        option_ask = Label(win, text='Do you want to practice by multiple \n choice quesions or flashcards?',
                           font=('Klee', 30, 'bold'),
                           bg='#76D7EA')

        global word_have, user_wordlist_box, user, word_have_mcq, MCQ_count

        word_have_mcq = []
        word_have = []
        for word in user_wordlist_box[user]:
            word_have_mcq.append(word)
            if user_checkin_count[user] % times[user_wordlist_box[user][word]] == 0:
                word_have.append(word)

        for word in word_have_mcq:
            MCQ_count[word] = 0

        random.shuffle(word_have_mcq)
        random.shuffle(word_have)

        multiple_choice = Button(win, text='Multiple Choice',
                                 height=3, width=13,
                                 font=('Klee', 25, 'bold'),
                                 bg='#76D7EA',
                                 command=lambda: multiple_display(0, user_wordlist[user], 'user'))

        flashcards = Button(win, text='Flashcard',
                            height=3, width=13,
                            font=('Klee', 25, 'bold'),
                            bg='#76D7EA',
                            command=lambda: screen_before_display_flashcard('user'))

        option_ask.place(x=180, y=100)
        multiple_choice.place(x=120, y=330)
        flashcards.place(x=420, y=330)

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


def multiple_display(multiple_number, definition, option):
    for widgets in win.winfo_children():
        widgets.destroy()

    global word_have_mcq
    # print(word_have_mcq)
    temp_word_have = copy.deepcopy(word_have_mcq)
    # print(temp_word_have[multiple_number], definition)
    multiple_question(
        temp_word_have[multiple_number], multiple_number, definition, option)


def multiple_question(word, multiple_number, definition, option):
    bunny.bunny_ask()

    ques_ask = Label(win, text=f"Question {multiple_number + 1}: What is the meaning of \n '{word}'?",
                     font=('Klee', 30, 'bold'),
                     bg='#76D7EA')
    ques_ask.place(x=180, y=100)

    random_abcd(word, multiple_number, definition, option)

    if option == 'bunny':
        exit_button(topic_choice_log_in)
    else:
        exit_button(practice_option_mywordlist)


def random_abcd(word, multiple_number, definition, option):

    temp_topic_choose = copy.deepcopy(definition)

    temp_definition = []
    for Word in temp_topic_choose:
        temp_definition.append(temp_topic_choose[Word])

    ans = ['A', 'B', 'C', 'D']
    correct_letter = 0
    correct_answer_definition = temp_topic_choose[word]
    temp_definition.remove(correct_answer_definition)

    random_answer = [correct_answer_definition]

    for i in range(3):
        try:
            ans_def = random.choice(temp_definition)
            temp_definition.remove(ans_def)
            random_answer.append(ans_def)
        except:
            random_answer.append('')

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
            list_button[i].config(command=lambda button=list_button[i], color='green', list=list_button,
                                  num=multiple_number, opt=option: change_color_button(button, color, list, num, definition, opt))
        else:
            list_button[i].config(command=lambda button=list_button[i], color='red', list=list_button,
                                  num=multiple_number, opt=option: change_color_button(button, color, list, num, definition, opt))

    list_button[0].place(x=120, y=310)
    list_button[1].place(x=120, y=390)
    list_button[2].place(x=120, y=470)
    list_button[3].place(x=120, y=550)


def change_color_button(button, color, button_list, multiple_number, definition, option):
    button.config(fg=color)
    for Button in button_list:
        if Button != button:
            Button.config(state=DISABLED)

    global word_have_mcq, bunny_wordlist_box, user, topic
    if MCQ_count[word_have_mcq[multiple_number]] == 0:
        MCQ_count[word_have_mcq[multiple_number]] = 1

        if color == 'green':
            if option == 'bunny':
                box = bunny_wordlist_box[user][topic][word_have_mcq[multiple_number]]
                if box < 4:
                    bunny_wordlist_box[user][topic][word_have_mcq[multiple_number]] += 1
            else:
                box = user_wordlist_box[user][word_have_mcq[multiple_number]]
                if box < 4:
                    user_wordlist_box[user][word_have_mcq[multiple_number]] += 1
        else:
            if option == 'bunny':
                box = bunny_wordlist_box[user][topic][word_have_mcq[multiple_number]]
                if box > 0:
                    bunny_wordlist_box[user][topic][word_have_mcq[multiple_number]] -= 1
            else:
                box = user_wordlist_box[user][word_have_mcq[multiple_number]]
                if box > 0:
                    user_wordlist_box[user][word_have_mcq[multiple_number]] -= 1

    if multiple_number != len(word_have_mcq) - 1:
        next_button(lambda: multiple_display(
            (multiple_number + 1),  definition, option))

#########################################################################


def screen_before_display_flashcard(option):
    for widgets in win.winfo_children():
        widgets.destroy()

    if len(word_have) != 0:
        option_ask = Label(win, text='Today, you have ' + str(len(word_have)) + ' words to review',
                           font=('Klee', 30, 'bold'),
                           bg='#76D7EA')
        option_ask.place(x=180, y=100)
        next_button(lambda: flashcard_display(0, option))

    else:
        option_ask = Label(win, text='Today, you have no word to review. Do you want to review all of the words again?',
                           font=('Klee', 30, 'bold'),
                           bg='#76D7EA')
        option_ask.place(x=180, y=100)
        next_button(lambda: flashcard_display(0, option))


def flashcard_display(flashcard_number, option):
    for widgets in win.winfo_children():
        widgets.destroy()

    global word_have, topic_choose, user_wordlist

    if len(word_have) == 0:
        if option == 'bunny':
            for word in topic_choose:
                word_have.append(word)
        else:
            for word in user_wordlist[user]:
                word_have.append(word)
        random.shuffle(word_have)

    flashcard_frame_word(word_have[flashcard_number], flashcard_number, option)


def flashcard_frame_word(word, flashcard_number, option):
    flashcard_frame = Button(win, text=word,
                             font=('Klee', 20, 'bold'),
                             height=10,
                             width=40,
                             bg='white',
                             command=lambda: flashcard_frame_definition(word, flashcard_number, option))
    flashcard_frame.place(x=135, y=150)

    show_word_number(flashcard_number + 1)

    next_button(lambda: flashcard_score(flashcard_number, option))

    if option == 'bunny':
        exit_button(topic_choice_log_in)
    else:
        exit_button(practice_option_mywordlist)


def flashcard_frame_definition(word, flashcard_number, option):
    for widgets in win.winfo_children():
        widgets.destroy()

    flashcard_frame = Button(win, text=f'Definition: \n {topic_choose[word]}',
                             font=('Klee', 20, 'bold'),
                             height=10,
                             width=40,
                             bg='white',
                             command=lambda: flashcard_frame_word(word, flashcard_number, option))
    flashcard_frame.place(x=135, y=150)

    show_word_number(flashcard_number + 1)

    next_button(lambda: flashcard_score(flashcard_number, option))

    back_flashcard_number = flashcard_number - 1
    if back_flashcard_number <= 0:
        back_flashcard_number = 0

    if option == 'bunny':
        exit_button(topic_choice_log_in)
    else:
        exit_button(practice_option_mywordlist)


def flashcard_score(flashcard_number, option):
    global bunny_wordlist_box, user, topic, word_have, user_wordlist_box
    if (messagebox.askyesno(title='Next?', message='Are you sure you know this word?')):
        if option == 'bunny':
            time = bunny_wordlist_box[user][topic][word_have[flashcard_number]]
            if time < 4:
                bunny_wordlist_box[user][topic][word_have[flashcard_number]] += 1
        else:
            time = user_wordlist_box[user][word_have[flashcard_number]]
            if time < 4:
                user_wordlist_box[user][word_have[flashcard_number]] += 1
    else:
        if option == 'bunny':
            time = bunny_wordlist_box[user][topic][word_have[flashcard_number]]
            if time > 0:
                bunny_wordlist_box[user][topic][word_have[flashcard_number]] -= 1
        else:
            time = user_wordlist_box[user][word_have[flashcard_number]]
            if time > 0:
                user_wordlist_box[user][word_have[flashcard_number]] -= 1
    next_flashcard_number = (flashcard_number + 1) % len(word_have)
    flashcard_display(next_flashcard_number, option)


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

    if bunny_or_user == 'bunny':
        global topic_choose
        i = 1
        for word in topic_choose:
            my_list_box.insert(END, f'{i}. {word}: {topic_choose[word]}')
            i += 1
    else:
        global user_wordlist, user
        i = 1
        for word in user_wordlist[user]:
            my_list_box.insert(
                END, f'{i}. {word}: {user_wordlist[user][word]}')
            i += 1

    if bunny_or_user == 'bunny':
        back_button(lambda: practice_option_bunny(topic))
    else:
        back_button(new_or_old_practice)


class Closing():
    def __init__(self):
        win.protocol('WM_DELETE_WINDOW', self.on_closing)
        win.mainloop()

    def on_closing(self):
        global bunny_wordlist_box, user_wordlist_box, user_checkin_count, bunny_wordlist_box_temp, user_wordlist_box_temp, user_checkin_count_temp, user_wordlist, user_wordlist_temp
        # Message box asks the users if they want to quit
        if messagebox.askyesno(title='Quit?', message='Do you want to save your progress before quitting?'):
            write_json('bunny_wordlist_box.json', bunny_wordlist_box)
            write_json('user_wordlist_box.json', user_wordlist_box)
            write_json('user_checkin_count.json', user_checkin_count)
            write_json('user_wordlist.json', user_wordlist)

        else:
            write_json('bunny_wordlist_box.json', bunny_wordlist_box_temp)
            write_json('user_wordlist_box.json', user_wordlist_box_temp)
            write_json('user_checkin_count.json', user_checkin_count_temp)
            write_json('user_wordlist.json', user_wordlist_temp)
        # Time.sleep(.5)
        win.destroy()

        # mixer.music.stop()
mainScreen()
Closing()
