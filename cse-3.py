'''
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
# Function to find the most suitable lab for 'n' students
def find_suitable_lab(capacities, num_students):
    suitable_labs = { 'L1': capacities[0], 'L2': capacities[1], 'L3': capacities[2] }
    
    # Filter labs that can accommodate 'n' students
    possible_labs = {lab: capacity for lab, capacity in suitable_labs.items() if capacity >= num_students}
    
    # Find the lab with the maximum capacity among the possible labs
    if possible_labs:
        suitable_lab = max(possible_labs, key=possible_labs.get)
        return suitable_lab
    else:
        return None  # In case no lab can accommodate 'n' students

# Input reading
x = int(input())  # Seating capacity of L1
y = int(input())  # Seating capacity of L2
z = int(input())  # Seating capacity of L3
n = int(input())  # Number of students

# List of lab capacities
capacities = [x, y, z]

# Find and print the suitable lab
suitable_lab = find_suitable_lab(capacities, n)
if suitable_lab:
    print(suitable_lab)
else:
    print("No suitable lab available")
