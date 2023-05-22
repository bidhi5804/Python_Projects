# import random module
import random

choices = {1:'Rock', 2:'Paper', 3:'Scissors'}

"""The following function will take user choice and 
computer choice as arguments and returns True if the 
user wins"""
def FindWinner(user_choice,comp_choice):
    if user_choice == comp_choice:
        print("Its a draw !!")
        return False
    elif (user_choice == 1 and comp_choice == 2) or \
            (user_choice == 2 and comp_choice == 1) or \
            (user_choice == 3 and comp_choice == 2):
        return True
    else:
        return False
        
"""This Function allows to Play the Game again if the user wants"""
def NextChance():
    while True:
        try:
            next_chance = input("Do you want to play again? ([Y/N] ")
            next_chance.lower()
            if next_chance in ['y','n']:
                if next_chance == 'n':
                    print("Thank you for playing!!")
                    return False
                elif next_chance == 'y':
                    PlayGame()
            else:
                print("Enter a Valid Choice")
        except ValueError:
            print("Invalid Choice. Please Enter Y/N")
            
"""This function will get the user choice"""
def UserChoice():
    while True:
        try:
            print("Coices :\n"
                    +"1: Rock\n"
                    +"2: Paper\n"
                    +"3: Scissors")
            choice = int(input("Enter your choice: "))
            if choice in choices:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid choice. Please enter a number.")
            
#Function to get Computer Choice            
def ComputerChoice():
    return random.choice(list(choices.keys()))
    
#Function to play the game    
def PlayGame():    
    user_choice = UserChoice()
    comp_choice = ComputerChoice()
    print("You chose:", choices[user_choice])
    print("Computer chose:", choices[comp_choice])
    if FindWinner(user_choice,comp_choice):
        print("Congrats You Won!")
    else:
        print("Better Luck Next Time!")
    NextChance()
    
#Game Rules
print('Game Rules :\n'
	+ "Rock vs Paper        ==> Paper Wins \n"
	+ "Rock vs Scissors     ==> Rock Wins \n"
	+ "Paper vs Scissors    ==> Scissor Wins \n")
PlayGame()
