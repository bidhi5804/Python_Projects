import random
import math
# Taking lower bound and upper bound from user
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
num_to_guess = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1, 2))
print("\n\tYou've only ",chances,
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while chances > 0:
	count += 1
	chances += -1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Checking Conditions
	if num_to_guess == guess:
		print("Congratulations you did it in ",
			count, " try")
		# If user guess correctly, loop will break
		break
	elif num_to_guess > guess:
		print("The number guessed is small!")
		print("You have ",chances, " Chances left")
	elif num_to_guess < guess:
		print("The number guessed is Large!")
		print("You have ",chances, " Chances left")

# output If the chances are over .
if chances == 0:
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
