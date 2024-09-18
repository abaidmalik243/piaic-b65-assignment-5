#  - Even or Odd.

def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

# Example usage
number = int(input("Enter a number: "))
result = check_even_or_odd(number)
print(result)
