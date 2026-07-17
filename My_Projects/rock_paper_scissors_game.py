import random
total_match = 3
user_won_match = 0
computer_won_match = 0
tie_match = 0
options = ["Rock", "Paper", "Scissors"]

# function
def who_win(user_won_match, computer_won_match):
	if user_won_match > computer_won_match:
		return "You win the game. 🥳🎉"
	elif user_won_match < computer_won_match:
		return "Computer win the game.💪🖥️"
	else:
		return "The game is Tie. 🤝"


print("Options:— \n\n1. Rock (🪨) \n2. Paper (📰) \n3. Scissors (✂️)") 


for i in range(3):
	while True:
		computer_input = random.choice(options)
		print(f"\nRound-{i+1}:")
		user_input = input("Choose one of them: ").capitalize().strip()
		if user_input in ["Rock", "Paper", "Scissors"]:
			if user_input == computer_input:
				print(f"The game is TIE. :।\nYou: {user_input}\nComputer: {computer_input}")
				tie_match = tie_match + 1
				break
			elif user_input == options[0] and computer_input == "Paper":
			    print(f"You LOSE. :(\nYou: {user_input}\nComputer: {computer_input}")
			    computer_won_match = computer_won_match + 1
			    break
			elif user_input == options[1] and computer_input == "Scissors":
			    print(f"You LOSE. :(\nYou: {user_input}\nComputer: {computer_input}")
			    computer_won_match = computer_won_match + 1
			    break
			elif user_input == options[2] and computer_input == "Rock":
			    print(f"You LOSE. :(\nYou: {user_input}\nComputer: {computer_input}")
			    computer_won_match = computer_won_match + 1
			    break
			elif user_input == options[0] and computer_input == "Scissors":
			    print(f"You WIN. :)\nYou: {user_input}\nComputer: {computer_input}")
			    
			    user_won_match = user_won_match + 1
			    break
			elif user_input == options[1] and computer_input == "Rock":
			    print(f"You WIN. :)\nYou: {user_input}\nComputer: {computer_input}")
			    user_won_match = user_won_match + 1
			    break
			elif user_input == options[2] and computer_input == "Paper":
			    print(f"You WIN. :)\nYou: {user_input}\nComputer: {computer_input}")
			    user_won_match = user_won_match + 1
			    break
		else:
			   print("Wrong input. Please try again with 'Rock'/'Paper'/'Scissors' only.")
	    

# result
print(f"\n\nResult Card: \n✔ You won: {user_won_match}/{total_match} match\n✔ Computer won: {computer_won_match}/{total_match} match\n✔ Tie: {tie_match}/{total_match} match")


winner_message = who_win(user_won_match, computer_won_match)

print(f"\n☞ Final Result: {winner_message}")