import random


opened_file = open("words")
words = opened_file.read().splitlines()
random_word = random.choice(words).lower()
word_length = (len(random_word))
random_word_letters = list(random_word)
turns = 8
# level = input("Sir or Madame, which difficulty do you prefer? Novice, Intermediate, Heroic: ")


print("The word contains: " + str(len(random_word)) + " letters")
user_guess = input("Please guess a letter: ").lower()


def game_control():
    blanks = 0
    for letter in random_word_letters:
        if turns == turns - 1:
            blanks += 1
        if letter not in good_guess:
            print('_ ', end='')
            blanks += 1
        else:
            print(letter, end='')
    if blanks == 0:
        print("\nYou win!!!")
        exit()


def guess_status():
    print("\nGood guesses: " + str(good_guess))
    print("\nBad guesses: " + str(bad_guess))

good_guess = []
bad_guess = []

new_game = "y"


while turns != 0:
    if len(user_guess) != 1:
        user_guess = input("Only one letter please: ")
    elif user_guess in good_guess:
        print("You already guessed that one!")
    elif user_guess in bad_guess:
        print("You already guessed that one!")
    for letter in random_word_letters:
        if user_guess in random_word_letters:
            if user_guess not in good_guess:
                good_guess.append(user_guess)
        else:
            if user_guess not in bad_guess:
                turns -= 1
                print("You lost a turn!")
                print("You have " + str(turns) + " guesses left.")
                bad_guess.append(user_guess)
            if turns == 0:
                print(random_word)
                print("\nYou lose!")
                exit()
    game_control()
    guess_status()
    user_guess = input("Please guess again: ").lower()
