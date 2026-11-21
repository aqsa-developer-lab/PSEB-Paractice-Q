# Take the balance and the package price. If the balance is enough, print “Package activated” and the remaining balance. Otherwise, print how much more is needed. Test: balance 300, price 450 → Insufficient balance, need Rs 150 more



balance = int(input("Enter your balance: "))
price = int(input("Enter package price: "))
if balance >= price:
    remaining = balance - price
    print("Package activated")
    print("Remaining balance: Rs", remaining)
else:
    needed = price - balance
    print("Insufficient balance, need Rs", needed, "more")
