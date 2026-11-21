# Take the temperature in °C and print the advice.

temperature = int(input("Enter temperature:"))
if temperature < 10:
    print("Cold,Wear a jacket")
elif temperature < 25:
    print("Pleasent")
elif temperature < 35:
    print("Warm")
elif temperature > 35:
    print("Very hot, stay hydrated")