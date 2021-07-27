# NATO alphabet for user input

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# ask for user input + error handeling if wrong input
def generate():
    user_input = list(input("Your name: ").upper())
    try:
        print([dictionary[letter] for letter in user_input])
    except KeyError:
        print("Not a valid entry")
        generate()


generate()