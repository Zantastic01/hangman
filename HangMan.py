def show_start():
    print("  _    _                   __  __")             
    print(" | |  | |                 |  \/  |")            
    print(" | |__| | __ _ _ __   __ _| \  / | __ _ _ __ ")
    print(" |  __  |/ _` | '_ \ / _` | |\/| |/ _` | '_ \ ")
    print(" | |  | | (_| | | | | (_| | |  | | (_| | | | |")
    print(" |_|  |_|\__,_|_| |_|\__, |_|  |_|\__,_|_| |_|")
    print("                      __/ |                  ") 
    print("                     |___/       ")

def get_name():
    name = input("What is your name?")
    print("Lets get started :)" + str(name))
    return name 

def show_credits():
 print:("Made by Zan")

    
def get_puzzle():
   return "Welcome hangman"

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


def display_board(solved, strikes, true_guess, wrong_guess):
    print(solved)
    print("Strikes: " + str(strikes))
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
    limit = 7
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
        display_board(solved, strikes, true_guess, wrong_guess)

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

