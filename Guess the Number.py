
# Guess the number game
# It automatically selects a number from 1 to 100 and the user has to guess it.
# The user recieves hints based on if the random number is higher or lower than the one input.


import random                                                                       # we include the library random

while True:                                                                         # start a loop
    random_number = random.randint(1, 100)                                          # generate a random number and saves it to "random_number"
    print("Guess the number between 1-100!")                                        # Prints this

    while True:                                                                     # start another loop inside the main one so we can come back here later
        guess_input = input("Guess the number: ")                                   # makes the user input a number
        if not guess_input.isdigit():                                               # if the content of the input is not a digit...
            print("You can only submit numbers!")                                   # prints that you can only submit numbers and...
            continue                                                                # continues...
        guess = int(guess_input)                                                    # asking again the number

        if guess == random_number:                                                  # if the guessed number is the same as the randomly-selected one...
            print("You guessed it!")                                                # prints that you won
            break                                                                   # and breaks ONLY THIS LOOP so the one below starts
        elif guess < random_number:                                                 # If the guessed number is lower than the randomly-selected one...
            print("Higher!")                                                        # tells you to guess higher
        else:                                                                       # in the opposite case
            print("Lower!")                                                         # it tells you to guess lower

    repeat = input("Do you want to start again? (Y/N) (Default: N): ")              # Asks if you want to repeat (asking for a Y if yes and a N if not)
    if repeat.upper() != "Y":                                                       # if the answer is not Y... (if it is it will go back to the loop from before)
        print("Bye!")                                                               #prints bye and...
        break                                                                       #breaks and stops de code
