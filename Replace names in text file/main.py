# open the template letter
# replace the [name] with the names in Names Folder
# store in Output

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    invites = names.readlines()

invites_cleaned = []
for name in invites:
    invites_cleaned.append(name.strip())

for name in invites_cleaned:
    new_letter = letter_template.replace("[name]", name)
    with open(f"./Output/letter_for_{name}.txt", mode="w") as letter:
        letter.write(new_letter)