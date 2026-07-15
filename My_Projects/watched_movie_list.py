# learned 'for loop'' and list
# func. 1
def entry_no_validation(watched_movie):
	print("Which number of entry do you want to change, let's confirm, please!")
	while True:
		try:
			entry_no = int(input("The entry no.: "))
			if entry_no in [1, 2, 3, 4, 5]:
				watched_movie.pop(entry_no-1)
				return entry_no, watched_movie
			else:
				print("Invalid entry no. Try again with valid entry no.")
				
		except ValueError:
			print("Invalid input. Try again with valid thing.")
	
# func. 2
def making_list():
	while True:
		watched_movie =[ ]
		print("Write five of your best watched movie: ")
		for i in range (5):
			while True:
				movie = input(f"Movie-{i+1}: ")
				if movie in watched_movie:
					print("You already entered this name. Write a different one.")
					
				else:
					watched_movie.append(movie)
					break
		break
			
						
	return watched_movie
	
	
# func. 3
def change_whole_list():
	print("\nDo you want to change this list?\n")
	is_wish_to_change = input("My decision is [y/n]: ").lower().strip()
	return is_wish_to_change


# main code		
watched_movie = making_list()
print(" \n\nHere is your list:")
print(watched_movie)
	
while True:	
	is_wish_to_change = change_whole_list()
	if is_wish_to_change == "y":
		while True:
			print("""1. I want to change the whole list
2. I want to remove just one entry""")
			change_option = input("Select one option: ")
			if change_option == "1":
				watched_movie = making_list()
				print(" \n\nHere is your list:")
				print(watched_movie)
				break
			elif change_option == "2":
				entry_no, watched_movie = entry_no_validation(watched_movie)
				
				while True:
					movie = input(f"Movie-{entry_no}: ")
					if movie in watched_movie:
						print("You already entered this name. Write a different one.")
						continue
						
					else:
						watched_movie.insert(entry_no-1, movie)
						print("\n\nHere is your list:")
						print(watched_movie)
						break
			else:
				print("Wrong choice. Retry with valid option.")
			break
											
	elif is_wish_to_change == "n":
		break
		
	else:
		print("Wrong input. Please try again with valid thing.")
		
print(f"\n\n\nOkay, your final list is:— {watched_movie}")
