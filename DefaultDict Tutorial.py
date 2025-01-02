# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def find_positions_in_group_a(n, m, group_a, group_b):
    # Create a defaultdict to store the positions of each word in group A
    positions_map = defaultdict(list)
    
    # Populate the defaultdict with words and their positions
    for i, word in enumerate(group_a, 1):
        positions_map[word].append(i)
    
    # Check each word in group B and print the positions
    for word in group_b:
        if word in positions_map:
            print(" ".join(map(str, positions_map[word])))
        else:
            print(-1)

# Reading input
n, m = map(int, input().split())  # n is size of group A, m is size of group B
group_a = [input().strip() for _ in range(n)]  # Group A words
group_b = [input().strip() for _ in range(m)]  # Group B words

# Call the function with the parsed inputs
find_positions_in_group_a(n, m, group_a, group_b)
