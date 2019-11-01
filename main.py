import random
import hangman_animation

random_list = ['letter', 'galgje', 'woord', 'computer', 'toetsenbord', 'programma', 'camera', 'scherm', 'galg', 'goed',
               'stoel', 'spel', 'ananas', 'pizza', 'onderbroek', 'python', 'docent', 'waarom', 'alfabet', 'rapper',
               'auto', 'kippenpot']


# Selecteer een random woord van een lijst
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def game_setup():
    try:
        total_players = int(input("Speel jij de game zelf of met meerdere personen? Voer een getal in.\n"))
    except ValueError:
        print("Er is geen getal ingevoerd. De game stopt...")
        exit(0)

    start_game(total_players)


def start_game(total_players):
    # Checken met hoeveel spelers je het spel speelt
    if total_players == 1:
        random_word = getRandomWord(random_list)
    else:
        while True:
            random_word = input("Vul een woord in: \n")

            # Checken of het een woord is
            if not random_word.isalpha():
                print("Je moet een woord invoeren!")
            else:
                break

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

    characters_said = []

    print("\nHet woord is ", len(random_word), "letters lang.")

    fill = "_" * len(random_word)
    geraden = list(fill)
    guesses_over = 10
    correct_input = 0

    while guesses_over > 0:

        # Checken of alleen alfabet karakters zijn ingevoerd bijvoorbeeld 'abc' 'ABC'
        while True:
            user_input1 = input("\nTyp een woord of een letter.\n")
            user_input = user_input1[0].lower()

            if user_input.isalpha():
                break

        characters_said.append(user_input)

        # Als de speler het in 1 keer goed raden
        if user_input == random_word:
            print("\nJij wint! Je hebt het woord in 1 keer goed geraden! Het woord was namelijk:", random_word)
            break

        for char in random_word:

            if user_input == char:

                for index, character in enumerate(random_word):
                    if character in user_input:
                        geraden[index] = user_input

                correct_input += 1

        print(geraden)

        if user_input not in random_word:
            guesses_over -= 1

            print("Je hebt nog '", guesses_over, "' kansen over.")
            print("Deze letter zit niet in het woord! Deze letter(s) heb je gehad:\n", characters_said)

            hangman_animation.display(characters_said)

        if correct_input == len(random_word):
            print("Gefeliciteerd! Jij wint. Het woord was", random_word)
            break

        if guesses_over == 0:
            print("Game over! Het woord was:", random_word)
            break


# Game loop
while True:
    game_setup()
    stop_game = input(
        "\nWil je stoppen of doorgaan? Typ 'exit' om te stoppen. Wil je doorgaan druk dan een random toets in. \n")
    if stop_game in "exit":
        break

print("Bedankt voor het spelen!")
