# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_mat(n, m):
    # Calculate the number of rows above and below the center row
    top_bottom_rows = (n - 1) // 2
    
    # Generate the top rows
    for i in range(1, top_bottom_rows + 1):
        # Create the pattern (.|.) repeated (2*i - 1) times
        pattern = ('.|.' * (2 * i - 1)).center(m, '-')
        print(pattern)
    
    # Print the middle "WELCOME" row
    print('WELCOME'.center(m, '-'))
    
    # Generate the bottom rows (mirror of the top rows)
    for i in range(top_bottom_rows, 0, -1):
        # Create the pattern (.|.) repeated (2*i - 1) times
        pattern = ('.|.' * (2 * i - 1)).center(m, '-')
        print(pattern)

# Input Reading
n, m = map(int, input().split())
print_mat(n, m)