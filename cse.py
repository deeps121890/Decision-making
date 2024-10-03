'''
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
'''
# Function to find the lab with minimal seating capacity
def find_min_capacity_lab(capacities):
    # Find the index of the minimum capacity
    min_index = capacities.index(min(capacities))
    
    # Lab names corresponding to the indices
    lab_names = ['L1', 'L2', 'L3']
    
    return lab_names[min_index]

# Input reading
a = int(input())  # Seating capacity of L1
b = int(input())  # Seating capacity of L2
c = int(input())  # Seating capacity of L3

# List of lab capacities
capacities = [a, b, c]

# Find and print the lab with minimal seating capacity
min_lab = find_min_capacity_lab(capacities)
print(min_lab)
