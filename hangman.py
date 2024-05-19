import random

HANGMAN_STAGES = [
    """
     +---+
     |   |
     O   |



    """,
    """
     +---+
     |   |
     O   |
     |   |


    """,
    """
     +---+
     |   |
     O   |
     |   |
    /    |
           
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
           
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
    """
]


def random_word():
    word_list = ["mango", "tryngo", "rama", "ant", "joker"]
    p_guess = random.choice(word_list)
    return p_guess


def display_word_login(comp_guess_word, display_word):
    word_display = ""
    for letter in comp_guess_word:
        if letter in display_word:
            word_display = word_display + letter
        else:
            word_display = word_display + "_"
    return word_display


def game_logic():
    com_guess = random_word()
    life_points = 5
    hangman_death = 0
    display_word = []
    result = ""
    while True:
        if life_points == 0:
            print("you lost the game.")
            print("AND YOU HAVE KILLED A MAN!")
            break
        if len(result) == len(com_guess):
            print("you have guessed all the letter's correctly!")
            print(f"the correct word was {com_guess}")
            print("YOU HAVE SAVED A LIFE!")
            break
        user_guess = input("enter the letter-:")
        if user_guess in com_guess:
            print(f"great guess! The word has {user_guess} in it.")
            display_word.append(user_guess)
            word = display_word_login(com_guess, display_word)
            if "_" not in word:
                result = word
            print(f"SECRET WORD -: {word}")
        else:
            life_points = life_points - 1
            print(f"Wrong! you are left with {life_points} life points")
            print(HANGMAN_STAGES[hangman_death])
            hangman_death = hangman_death + 1


def play():
    game_logic()
    while True:
        print("Do you want to play again")
        response = input("response(yes or no)-:")
        if response in ("yes", "Yes"):
            game_logic()
        else:
            print("SEE YOU SOON!")
            break


print("Welcome To the Death game")
print("Here you can become a savior by saving a life or you can be a murderer looser for failing to do so.")
print("Play Well my Friend!")
play()
