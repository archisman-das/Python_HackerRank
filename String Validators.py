def string_validation(s):
    # Check for each condition and print the result
    print(any(char.isalnum() for char in s))  # Alphanumeric check
    print(any(char.isalpha() for char in s))  # Alphabetical check
    print(any(char.isdigit() for char in s))  # Digits check
    print(any(char.islower() for char in s))  # Lowercase check
    print(any(char.isupper() for char in s))  # Uppercase check
if __name__ == '__main__':
    s = input()
    string_validation(s)  # Call the validation function
