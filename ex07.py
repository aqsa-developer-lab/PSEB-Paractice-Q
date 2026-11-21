# Take the bill amount and print the discount and the final amount.
billAmount = int(input("Enter your Amount"))
discount = 0
if billAmount >= 5000:
    discount = billAmount * 0.10
elif billAmount >=2000 and billAmount <=4999:
    discount = billAmount * 0.05
else:
    discount = 0
    print(f"Your billing ammpount is {billAmount},Your discount is {discount} , Net pay able ammount is {billAmount - discount}")