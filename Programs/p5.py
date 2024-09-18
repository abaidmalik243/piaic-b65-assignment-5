#  - Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)

age = int(input("Enter your Age: "))

match age:

    case _ if age > 0 and age <= 12:
        print("You are Child!")
    case _ if age >= 13 and age <= 19:
        print("You are teenager!")
    case _ if age >= 20 and age <= 59:
        print("You are adult!")
    case _ if age >= 60:
        print("You are senior citizen!")
    case _:
        print("Invalid Age")

        