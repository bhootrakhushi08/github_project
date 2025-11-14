import random
import datetime
import time
import winsound

# -------------------------------
#  JUMBLE WORD GAME FUNCTIONS
# -------------------------------

words = ["python", "jumble", "keyboard", "function", "variable", "loop", "string", "integer"]

def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

def play_jumble_game():
    score = 0
    print("\n Welcome to the Jumble Word Game!\n")

    for i in range(5):  # Play 5 rounds
        word = random.choice(words)
        jumbled = jumble_word(word)
        print(f"Round {i+1}: Unscramble this word → {jumbled}")
        guess = input("Your guess: ").lower()

        if guess == word:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct word was: {word}\n")

    print(f" Game Over! Your score: {score}/5\n")


# -------------------------------
#  TO-DO LIST APP FUNCTIONS
# -------------------------------

my_dictionary = {}

def addTask(value):
    key = len(my_dictionary) + 1
    my_dictionary[key] = value
    print(f"  Task '{value}' added successfully!")

def viewTask():
    if not my_dictionary:
        print("Your to-do list is empty!")
    else:
        print("\n  Your To-Do List:")
        for task, details in my_dictionary.items():
            print(f"{task}. {details}")

def updateTask(key):
    if key in my_dictionary:
        new_task = input("Enter the updated task: ")
        my_dictionary[key] = new_task
        print("  Task updated successfully!")
    else:
        print("  Task not found!")

def doneTask(key):
    if key in my_dictionary:
        if "(DONE)" not in my_dictionary[key]:
            my_dictionary[key] += " (DONE)"
            print("  Task marked as done!")
        else:
            print("  Task is already marked as done.")
    else:
        print("  Task not found!")

def deleteTask(key):
    if key in my_dictionary:
        removed = my_dictionary.pop(key)
        my_dictionary.update({i + 1: v for i, v in enumerate(my_dictionary.values())})
        print(f"  Task '{removed}' deleted successfully!")
    else:
        print("  No such task number exists!")

def to_do_list_menu():
    while True:
        print("\n----   TO-DO LIST MENU ----")
        print("1 - Add Task")
        print("2 - View All Tasks")
        print("3 - Update Task")
        print("4 - Mark Task as Done")
        print("5 - Delete Task")
        print("6 - Return to Main Menu")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("  Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            value = input("Enter your task: ")
            addTask(value)
        elif choice == 2:
            viewTask()
        elif choice == 3:
            try:
                key = int(input("Enter the task number to update: "))
                updateTask(key)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 4:
            try:
                key = int(input("Enter the task number to mark as done: "))
                doneTask(key)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 5:
            try:
                key = int(input("Enter the task number to delete: "))
                deleteTask(key)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 6:
            print("Returning to Main Menu...\n")
            break
        else:
            print(" Invalid choice! Please try again.")          

# -------------------------------
#  ALARM CLOCK
# -------------------------------           
            
def set_alarm(alarm_time_str):
    print(f"Alarm set for: {alarm_time_str}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_str:
            print("Time to wake up!")
            winsound.PlaySound("morning_new_alarm.wav",
                               winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(5)  # keep alive so sound can play
            break
        time.sleep(1)
        
# -------------------------------
#  ROCK PAPER SCISSOR GAME
# -------------------------------             
    
def play_game():
    choices = ["rock", "paper", "scissor"]
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissor): ").lower()
        if player_choice in choices:
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissor") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
        
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            play_game() 
        elif play_again == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
# -------------------------------
#  HANGMAN GAME
# -------------------------------

def hangman():
    words = ["python", "programming", "developer", "computer", "algorithm", "challenge"]
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    lives = 6
    
    print("Welcome to Hangman!")
    print("_ " * len(chosen_word))

    while lives > 0:
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", chosen_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Correct guess!")
        else:
            lives -= 1
            print(f"Wrong guess! You have {lives} lives left.")
            if lives == 0:
                print("Game Over! The word was:", chosen_word)
 

 
# -------------------------------
#   MAIN MENU
# -------------------------------

def main():
    while True:
        print("\n========  MAIN MENU  ========")
        print("1 - Play Jumble Word Game")
        print("2 - Open To-Do List App")
        print("3 - Hangman Game")
        print("4 - Alarm Clock")
        print("5 - Rock Paper Scissor Game")
        print("6 - Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("  Invalid input! Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            play_jumble_game()
        elif choice == 2:
            to_do_list_menu()
        elif choice == 3:
            hangman()
        elif choice == 4:
            alarm_hour = input("Enter alarm hour (24-hour format): ")
            alarm_minute = input("Enter alarm minute: ")
            alarm_second = input("Enter alarm second: ")
            alarm_time = f"{alarm_hour}:{alarm_minute}:{alarm_second}"
            set_alarm(alarm_time)
        elif choice == 5:
            play_game()
        elif choice == 6:
            print("  Exiting program. Goodbye!")
            break
        else:
            print("  Invalid choice! Try again.")
 
# Run the program
main()
