from random import *

def pick_a_number():
    number = randint(1, 100)
    return number


picked_number = pick_a_number()

attempts = 0
game_run = True

print("GUESS THE CHOSEN NUMBER!")

while game_run:
    try:
        user_input = int(input('guess: '))
    
        if user_input < picked_number:
            attempts += 1
            print(f"The chosen number is greater than {user_input}")
        
        elif user_input > picked_number:
            attempts += 1
            print(f"The chosen number is less than {user_input}")
        
        elif user_input == picked_number:
            print(f"YOU WIN! The chosen number was {picked_number}\nYou tried to guess {attempts} times!")
            break
        
    except ValueError:
        print("An error occured: you must use only integer numbers to play!")
        continue