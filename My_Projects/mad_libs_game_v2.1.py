# function: this is really a helpful way to reduce code 😎

# function1
def validation_check(hint):
   while True:
        value = input(f"Input {hint}: ")      

        if value:
            print("Processing the funny story...")
            return value

        else:
            print("Input valid thing: ")

# function2
def validation_check_for_decision(decision):
    while True:
        if decision == "y":
            print("Let's make you understand the rules and regulations of this game:\n >This game is very easy to play.\n >You just need to input 10 words (Noun, Verb, Adjective, and etc.) to fill some gaps of a hidden story.\n >That means you should fill the gaps of the story to complete without knowing the real story.")
            decision_1 = input("To go the next step, type 'next': ").lower().strip()

            return decision_1

        elif decision == "n":
            print("It's okay. :-( Thanks for visiting our site!")
            exit() # no more chance

        else:
            print("Sorry, invalid input.")
            print("Provide valid input, please!")
            decision = input("If 'yes', please type 'y', otherwise type 'n':").lower().strip()


# intro
print("Hey, Hello!")
print("You are welcome to Mad Libs Game!")
print("Do you want to play this Game?") 

decision = input("If 'yes', please type 'y', otherwise type 'n':").lower().strip()
decision_1 = validation_check_for_decision(decision)

while True:
    if decision_1 == "next":
        print(" >After you input all words, you will see the completed story filled with your words and then...you will discover a funny story you completed with.")
        print("Ok, hope you understood. So let's start to play...")
        print("At first—")


        # input
        a_name = validation_check("a name")
        a_color = validation_check("a color")
        a_bad_smell = validation_check("a bad smell")
        a_food = validation_check("a food")
        an_animal = validation_check("an animal")
        a_verb = validation_check("a verb")
        a_body_part = validation_check("a body part")
        a_happy_word = validation_check("a happy word")


        # output
        print("Okay, you are almost done!")
        print("Processing the final funny story...")
        print("The final completed story is ready here: ")
        print("Name of the Story is: The Person Who Hated Flowers.")
        print(f"Once upon a time, there was a person named {a_name} who didn't love flowers.\n Whenever {a_name} saw a rose, their face would turn {a_color}. 'Flowers are boring!' they said. 'They smell like {a_bad_smell}!'\n Instead of flowers, {a_name} wanted to grow {a_food} in the garden.\n One day, a big {an_animal} ran into the yard and started to {a_verb} all over the grass.\n Suddenly, a tiny flower grew and touched their {a_body_part}. It felt so soft! {a_name} smiled and felt very {a_happy_word}.\n Maybe flowers were okay after all!")
        break

    else:
        print("Invalid Input.")
        decision_1 = input("To go the next step, type 'next': ").lower().strip()