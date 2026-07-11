# so much irritating. I must need to learn how to make function and how to avoid this irritating loop
# 😫😫 only I know how difficult is this to code in mobile without learning function
# I'll try this project later with using function, promise ✊
# intro
print("Hey, Hello!")
print("You are welcome to Mad Libs Game!")
print("Do you want to play this Game?")

decision = input("If 'yes', please type 'y', otherwise type 'n':").lower().strip()

while True: # giving users a chance/pressure to input valid thing
        if decision == "y":
                print("Let's make you understand the rules and regulations of this game:\n >This game is very easy to play.\n >You just need to input 10 words (Noun, Verb, Adjective, and etc.) to fill some gaps of a hidden story.\n >That means you should fill the gaps of the story to complete without knowing the real story.")

                decision_1 = input("To go the next step, type 'next': ").lower().strip()

                while True:
                            if decision_1 == "next":
                                    print(" >After you input all words, you will see the completed story filled with your words and then...you will discover a funny story you completed with.")
                                    print("Ok, hope you understood. So let's start to play...")
                                    print("At first—")

                                    # should need to make a function to make easy to understand the code from here...will try later.
                                    a_name = input("Input a name: ")


                                    while True:
                                        if a_name:
                                            print("Processing the funny story...")
                                            a_color = input("Input a color: ")


                                            while True:
                                                if a_color:
                                                    print("Processing the funny story...")
                                                    a_bad_smell = input("Input a bad smell: ")


                                                    while True:
                                                        if a_bad_smell:
                                                            print("Processing the funny story...")
                                                            a_food = input("Input a food: ")

                                                            while True:
                                                                if a_food:
                                                                    print("Processing the funny story...")
                                                                    an_animal = input("Input an animal: ")
                                                                    while True:
                                                                        if an_animal:
                                                                            print("Processing the funny story...")
                                                                            verb = input("Input a verb: ")

                                                                            while True:
                                                                                if verb:
                                                                                    print("Processing the funny story...")
                                                                                    a_body_part = input("Input a body part: ")

                                                                                    while True:
                                                                                        if a_body_part:
                                                                                            print("Processing the funny story...")
                                                                                            a_happy_word = input("Input a happy word: ")

                                                                                            while True:
                                                                                                if a_happy_word:
                                                                                                    print("Okay, you are almost done!")
                                                                                                    print("Processing the final funny story...")
                                                                                                    print("The final completed story is ready here: ")
                                                                                                    print("Name of the Story is: The Person Who Hated Flowers.")
                                                                                                    print(f"Once upon a time, there was a person named {a_name} who didn't love flowers.\n Whenever {a_name} saw a rose, their face would turn {a_color}. 'Flowers are boring!' they said. 'They smell like {a_bad_smell}!'\n Instead of flowers, {a_name} wanted to grow {a_food} in the garden.\n One day, a big {an_animal} ran into the yard and started to {verb} all over the grass.\n Suddenly, a tiny flower grew and touched their {a_body_part}. It felt so soft! {a_name} smiled and felt very {a_happy_word}.\n Maybe flowers were okay after all!")
                                                                                                    break

                                                                                                else:
                                                                                                    print("Input something.")
                                                                                                    a_happy_word = input("Input a happy word: ")


                                                                                        else:
                                                                                            print("Input something ")
                                                                                            a_body_part = input("Input a body part: ")

                                                                                else:
                                                                                    print("Input something ")
                                                                                    verb = input("Input a verb: ")
                                                                        else:
                                                                            print("Input something ")
                                                                            an_animal = input("Input an animal: ")
                                                                else:
                                                                        print("Input something ")
                                                                        a_food = input("Input a food: ")
                                                        else:
                                                            print("Input something ")
                                                            a_bad_smell = input("Input a bad smell: ")


                                                else:
                                                    print("Input something ")
                                                    a_color = input("Input a color: ")


                                        else:
                                            print("Input Something ")
                                            a_name = input("Input a name: ")

                            else:
                                    print("Invalid Input.")
                                    decision_1 = input("To go the next step, type 'next': ").lower().strip()
                                    continue
                break



        elif decision == "n":
            print("It's okay. :-( Thanks for visiting our site!")
            #exit() # no more chance
            break # another option to exit the loop


        else:
                print("Sorry, invalid input.")
                print("Provide valid input, please!")
                decision = input("If 'yes', please type 'y', otherwise type 'n':").lower().strip()
