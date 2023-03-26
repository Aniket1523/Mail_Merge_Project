# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    for name in names:
        new_file_name = f"letter_for_{name.strip()}.txt"
        with open("./Input/Letters/starting_letter.txt") as start_letter:
            lines = start_letter.readlines()
            with open(f"./Output/ReadyToSend/{new_file_name}", mode='a') as new_letter:
                for i in range(0, len(lines)):
                    if i == 0:
                        first_line = lines[0].replace("[name]", name.strip())
                        new_letter.write(first_line)
                    else:
                        new_letter.write(lines[i])