import random

possible_answers = ["cat", "dog", "pig", "car",
                    "run", "grab", "pub", "man", "women"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

guess = ""


def main():
    # the cimputer will select a random word to have user guess
    computer_pick = random.choice(possible_answers)
    print(computer_pick)

    first_pick = raw_input("Hello, Please select your first letter: ")

    for i in possible_answers:
        print(possible_answers)

        if first_pick == char in possible_answers:
            print(char)

    # for char in computer_pick:
    #     print("letter", char)

    #     if char in first_pick == char in computer_pick:
    #         print("pick", char)


if __name__ == '__main__':
    main()
