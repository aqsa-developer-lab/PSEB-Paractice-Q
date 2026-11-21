# Take one character and print whether it is a Vowel, Consonant, Digit or Special character. Hint: .isdigit(), .isalpha(), and .lower() in "aeiou"

ch = input("Enter one character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Special character")


