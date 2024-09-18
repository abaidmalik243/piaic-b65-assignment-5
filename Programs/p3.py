#  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.


num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Number is divisible by both 2 and 3")
elif num % 2 != 0 and num % 3 != 0:
    print("Number is no divisible by both 2 and 3")
else:
    print("Number is divisible with one of these numbers 2 o 3")
    