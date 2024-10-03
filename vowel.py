'''
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
'''
# Function to check if the character is a vowel, consonant, or not an alphabet
def check_character(char):
    if char.isalpha():  # Check if the character is an alphabet
        if char.lower() in 'aeiou':  # Check for vowels
            return "Vowel"
        else:  # If it's not a vowel, it's a consonant
            return "Consonant"
    else:
        return "Not an alphabet"  # If it's not an alphabet

# Input reading
character = input().strip()  # Read the input character

# Check and print the result
result = check_character(character)
print(result)
