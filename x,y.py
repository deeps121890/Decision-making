'''
Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8
'''
# Function to compare two integers
def compare_numbers(x, y):
    if x == y:
        return f"{x} and {y} are equal"
    elif x > y:
        return f"{x} greater than {y}"
    else:
        return f"{x} less than {y}"

# Input reading
a = int(input())  # First integer
b = int(input())  # Second integer

# Compare and print the result
result = compare_numbers(a, b)
print(result)
