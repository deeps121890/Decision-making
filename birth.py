'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
# Function to calculate age
def calculate_age(birth_year_last_two, current_year_last_two):
    # Assuming birth year is in the 1900s or 2000s
    if current_year_last_two >= birth_year_last_two:
        age = current_year_last_two - birth_year_last_two
    else:
        age = (100 + current_year_last_two) - birth_year_last_two  # For cases where the year crosses from 20xx to 21xx
    
    return age

# Input reading
birth_year = int(input())
current_year = int(input())

# Calculate age
age = calculate_age(birth_year, current_year)

# Print the result
print(age)
