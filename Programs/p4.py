#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."


age = int(input("Enter your Age: "))

if age >= 18:
    print("Your age is valid for vote")

    isPakistani = input("Are you Pakistani? Yes or No: ")

    if isPakistani.lower() == "yes":
        print("You are eligible for vot")
    else:
        print("Only Pakistani allowed for vot")

else:
    print("You are not eligible for vot")

    