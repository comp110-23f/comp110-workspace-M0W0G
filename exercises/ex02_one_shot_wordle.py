"""EX02 - One Shot World - A bigger step toward Wordle."""

__author__ = "730564009"


# Defining emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Secret Guess
secret_word = "python"

# Asks user what their guess is
input_string = input(f"What is your {len(secret_word)} letter guess?")

# Makes sure users guess is same length as secret
while (len(input_string) != len(secret_word)):
    input_string = input(f"That was not {len(secret_word)} letters! Try again:")


string_index = 0

# Variable to see if string contains guess at another index
string_contains = False

string_output = ""

# Looping through the secret
while (string_index < len(secret_word)):
    # If input index and secret index are equal add a green box
    if (input_string[string_index] == secret_word[string_index]):
        string_output += GREEN_BOX

    # If not check to see if we need to add a yellow box
    else:
        nested_string_index = 0
        string_contains = False
        # Looping through the word again to check for specific input index
        while (not string_contains and nested_string_index < len(secret_word)):
            # If input index is found somewhere in the word
            if (input_string[string_index] == secret_word[nested_string_index]):
                string_output += YELLOW_BOX
                # This variable will escape the while loop
                string_contains = True
            nested_string_index += 1
        # If the letter was not foupnd anywhere in the secret we add a white box
        if (string_contains == False):
            string_output += WHITE_BOX

    string_index += 1

#print output
print(string_output)

if (input_string == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
