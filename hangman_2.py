import os
import random
def show_start():
    file_names = os.listdir("art")
    for i, f in enumerate(file_names):

        file = "art/start.txt"

        with open(file, 'r') as f:
            start = f.read()

    print(start)

def get_name():
    name = input("What is your name?")
    print("Lets get started :)" + str(name))
    return name 

def show_credits():
 print:("Made by Zan")

    
def get_puzzle():

    file_names = os.listdir("data")
    for i, f in enumerate(file_names):
        print(str(i + 1) + ")" + f)

    choice = input("Which one?")
    choice = int(choice)

    file = "data/" + file_names[choice]

    with open(file, 'r') as f:
            lines = f.read().splitlines()

    print(lines)

    category = lines[0]
    puzzle = random.choice(lines[1:])

    print(category)
    return puzzle

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        elif letter == " ":
            solved += " "
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a Letter " + str(name))

        if len(letter) == 1:
            return letter
    
        else:
            print("Sorry, I dont understand " + str(name) + "." + " Enter a letter for your guess. ")


def display_board(solved, true_guess, wrong_guess, strikes):
    print(solved)
    print("")
    
    file_names = os.listdir("art")
    for i, f in enumerate(file_names):
        if strikes == 0:
            file = "art/nothing.txt"
            with open(file, 'r') as f:
                pic = f.read()
        elif strikes == 1:
            file = "art/1.txt"
            with open(file, 'r') as f:
                pic = f.read()
        elif strikes == 2:
            file = "art/2.txt"
            with open(file, 'r') as f:
                pic = f.read()
        elif strikes == 3:
            file = "art/3.txt"
            with open(file, 'r') as f:
                pic = f.read()
        elif strikes == 4:
            file = "art/4.txt"
            with open(file, 'r') as f:
                pic = f.read()
        elif strikes == 5:
            file = "art/5.txt"
            with open(file, 'r') as f:
                pic = f.read()
        elif strikes == 6:
            file = "art/6.txt"
            with open(file, 'r') as f:
                pic = f.read()

    print(pic)
    print("True guesses: " + str(true_guess))
    print("False guesses: " + str(wrong_guess))

def show_result(strikes,limit, name):
    if strikes < limit:
        print("You Got It! " + str(name))
    else:
        print("Do better :( " + str(name) + ".")


def play(name):

    puzzle = get_puzzle()
    guesses = ""
    true_guess = ""
    wrong_guess = ""
    solved = get_solved (puzzle, guesses)
    limit = 5
    strikes = 0
    
    print("You have " + str(limit) + " tries.")
    print(solved)

    while solved != puzzle and strikes < limit :
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1
            wrong_guess += letter
        else:
            true_guess += letter
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, true_guess, wrong_guess, strikes)

    show_result(strikes, limit, name)

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

# Game starts running here

show_start()
name = get_name()

playing = True

while playing:
    play(name)
    playing = play_again()


show_credits()
