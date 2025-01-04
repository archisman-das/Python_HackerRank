def average(array):
    # Convert the list to a set to remove duplicates
    distinct_heights = set(array)
    
    # Calculate the sum and length of the distinct heights
    avg = sum(distinct_heights) / len(distinct_heights)
    
    # Return the average rounded to 3 decimal places
    return round(avg, 3)
# your code goes here

