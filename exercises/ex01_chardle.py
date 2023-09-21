"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730564009"

# Getting input string
input_string = input("Enter a 5-character word:")

if len(input_string) != 5:
    print("Error: Word must contain 5 characters")
    exit()

# Getting input character
input_character = input("Enter a single character:")

if len(input_character) != 1:
    print("Error: Character must be a single character.")
    exit()

# Initializing counter to 0
instances_found = 0


print("Searching for " + input_character + " in " + input_string)

# Checking through various positions looking for specified character
if input_string[0] == input_character:
    print(input_character + " found at index 0")
    # if character is found up the instances by 1
    instances_found += 1

if input_string[1] == input_character:
    print(input_character + " found at index 1")
    instances_found += 1

if input_string[2] == input_character:
    print(input_character + " found at index 2")
    instances_found += 1

if input_string[3] == input_character:
    print(input_character + " found at index 3")
    instances_found += 1

if input_string[4] == input_character:
    print(input_character + " found at index 4")
    instances_found += 1

# Printing various responses depending on how many characters found
if (instances_found == 0):
    print("No instances of " + input_character + " found in " + input_string)
elif (instances_found == 1):
    print(str(instances_found) + " instance of " + input_character + " found in " + input_string)
elif (instances_found > 1):
    print(str(instances_found) + " instances of " + input_character + " found in " + input_string)
