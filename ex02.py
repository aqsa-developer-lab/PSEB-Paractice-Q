# Take a person’s age. At 18 or above, print “Eligible to vote”. Otherwise, print how many years are left

age = int (input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    yearLeft = 18 - age
    print(f"You're not eligible to vote, {yearLeft} years left to vote")
    