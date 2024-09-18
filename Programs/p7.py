#  - Check if a year is a leap year or not.

yearValue = int(input("Enter year: "))

if (yearValue % 4 == 0 and yearValue % 100 != 0) or (yearValue % 400 == 0):
    print(f"{yearValue} is a leap year .")
else:
    print(f"{yearValue} is not a leap year.")
