# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

# Function to determine the day of the week
def find_day(month, day, year):
    # Get the day of the week as an integer (0 = Monday, 6 = Sunday)
    day_of_week = calendar.weekday(year, month, day)
    
    # Map the integer to the corresponding day name
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    
    # Return the day in uppercase
    return days[day_of_week]

# Input reading
month, day, year = map(int, input().split())

# Call the function and print the result
print(find_day(month, day, year))