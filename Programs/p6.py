#  - Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.

def days_in_month(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return "31 days"
    elif month in [4, 6, 9, 11]:
        return "30 days"
    elif month == 2:
        return "28 days"
    else:
        return "Invalid month number. Please enter a number between 1 and 12."

# Example usage
month = int(input("Enter a month number (1-12): "))
result = days_in_month(month)
print(result)

