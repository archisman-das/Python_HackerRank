if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)  # Create a tuple from the list
    print(hash(t))  # Compute and print the hash of the tuple
