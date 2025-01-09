def print_formatted(number):
    # Calculate the width for alignment
    width = len(bin(number)) - 2  # Remove the '0b' prefix from binary representation

    # Print each number in the required formats
    for i in range(1, number + 1):
        # Print decimal, octal, hexadecimal and binary in aligned format
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")
# your code goes here
