# Take a student’s marks out of 100. 40 or above is Pass; below 40 is Fail.

numbers = int(input("Enter your marks:"))
if numbers < 0 or numbers > 100:
    print("Incorrect Marks")
elif numbers >= 40:
    print("You are passed")
else:
    print("Failed")