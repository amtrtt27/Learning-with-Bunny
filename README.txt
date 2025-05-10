			#### LEARNING WITH BUNNY - 15112 Project ####

################################################################################
	
	## Introduction ##

Learning with Bunny is a digital tool that helps users learn and memorize 
vocabulary through the use of various forms of practice. This app allows users 
to create their own set of vocabulary. Learning with Bunny provides users with 
various options to practice including virtual flashcards and multiple-choice 
questions, in which the multiple choices are randomized with only 1 correct 
answer. So the users can easily choose the proper learning approach, which 
enables them to absorb new words better. Learning with Bunny applies the Leitner 
system algorithm to help the user revise words with the goal that after a certain 
amount of time, he can memorize the whole set of words.

################################################################################
	## How to run the project ##

The user run the appRun.py to run the app

Learning with Bunny allows user to sign up or log in his exist account. After 
that, you can choose to practice Bunny's given wordlist or create your new own. 

If you choose Bunny's wordlist, there are 4 given topics provided: Job, Tourism, 
Environment, and Education. 

If you choose your own wordlist, you can add new words or practice the previous 
version of your wordlist. 

Then you can choose to practice with multiple-choice questions or flashcards. 
You can also see your current wordlist with the 'Wordlist' button.

1) In the multiple-choice options: there is only 1 correct answer, and the 
others are randomized. If you choose the incorrect answer, you cannot see the 
correct one. You should go back to the wordlist to check what it is or practice 
the flashcards before playing multiple-choice questions.

2) In the flashcards: you flip the card to see the word and its definition. In 
order to make sure you know the word, Bunny will ask you a question. If you 
choose yes, you can move to the next word.

Before quitting the app, Bunny will ask you whether you want to save your 
progress. If you choose yes, the system will save the latest version of your 
progress. If you choose no, nothing will be stored.

Space repetition practice system:
There are 5 boxes to save the user's progress:
- Box 0: review every time the you logs in 
- Box 1: review after 2 times log in
- Box 2: review after 5 times log in 
- Box 3: review after 10 times log in 
- Box 4: review after 20 times log in

At the beginning, all words are stored in box 0. When the you make a correct 
answer in multiple-choice question or know a word in the flashcard option, that 
word will be moved to box 1. The log in time is calculated after the account is  
created. If the user finish all the word before the time log in required in the 
next box, Bunny will ask if he wants to reset again.

################################################################################

	## How to install libraries needed ##

## Install Tkinter ##

Step 1 − Make sure Python and pip is preinstalled on your system
Type the following commands in command propmt to check is python and pip is 
installed on your system.
- To check Python: python --version
If python is successfully installed, the version of python installed on your 
system will be displayed.

- To check pip: pip -V
The version of pip will be displayed, if it is successfully installed on your system.

Step 2 − Install Tkinter
Tkinter can be installed using pip. The following command is run in the command 
prompt to install Tkinter: pip install tk

## Install PIL ##

Run pip install Pillow in the terminal to install Pillow in a virtual environment.

## Install PyGame ##

To install Pygame, open the command prompt and give the command: pip install pygame
