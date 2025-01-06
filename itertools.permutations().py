# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

# Read input
S, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
sorted_S = sorted(S)

# Generate and print permutations of size k
for perm in permutations(sorted_S, k):
    print(''.join(perm))
