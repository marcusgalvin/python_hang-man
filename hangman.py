import random

possible_answers = ["cat", "dog", "pig", "car",
                    "run", "grab", "pub", "man", "women"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

guess = ""


def main():
    # the cimputer will select a random word to have user guess
    computer_pick = random.choice(possible_answers)
    print("computer chose word: ", computer_pick)

    first_pick = raw_input("Hello, Please select your first letter: ")

    # for marble in computer_pick:
    #     print(marble)


def findLetters(first_pick, computer_pick):
    return all(letter in computer_pick for letter in first_pick)


if __name__ == '__main__':
    main()
