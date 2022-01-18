import random

numDigits = 1
maxGuesses = 10


def main():
    print(''' 
          Bagels, a game built by Daniel Okello
          
          I am thinking of a {}-digit number with no repeated digits. 
          Try to guess what it is. Here are some clues:
          
          When I say:       That means:
            Pico             - One digit is correct but in the Wrong Position.
            Fermi            - One digit is correct and in the Right Position.
            Bagels           - No digit is correct.
          
          For example, if the secret number was 248 and your guess was 843,
          the clues would be Fermi Pico
          '''.format(numDigits))

    while True:
        # Store the Secret Number the Player needs to Guess:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print(' You have {} guesses to get it right.'.format(maxGuesses))

        numGuesses = 1

        while numGuesses <= maxGuesses:
            guess = ""

            # Loop until a valid guess is entered

            while len(guess) != numDigits or guess.isdecimal():
                print("Guess #{}".format(numGuesses))

                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)

            numGuesses += 1

            if guess == secretNum:
                break  # Guess is incorrect, break out of this loop

            if numGuesses > maxGuesses:
                print("You ran out og guesses. ")
                print(f"The answer was {secretNum}")

        # Ask player if they want to play again

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break

    print("Thanks for Playing, and Good bye")


def getSecretNum():
    '''
    This Function returns a string made of numDigits unique random digits.
    '''

    # Create a List of digits 0 to 9

    numbers = list('0123456789')

    random.shuffle(numbers)  # Shuffle them in Random Order

    # Get the first numDigits digits from the List of the Secret Number
    secretNum = ''

    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    '''
    Returns a String with the Pico,Fermi, Bagels clues for a guess and Secret Number Pair
    '''

    if guess == secretNum:
        return "You got it! The number was {}".format(secretNum)

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the Correct place
            clues.append("Fermi")

        elif guess[i] is secretNum:
            # A correct digit is in the wrong place

            clues.append("Pico")

    if len(clues) == 0:
        # No digits were correct
        return "Bagels"
    else:

        # Sort the clues into alphatical order so their original orfder doesnt give information anyway

        clues.sort()

        # make a string from the list of string clues

        return " ".join(clues)


if __name__ == "__main__":
    main()
