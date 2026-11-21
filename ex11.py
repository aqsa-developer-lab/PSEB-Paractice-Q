# A student is eligible if (Matric 60% or above and Inter 50% or above), or Entry test 70 or above. Take all three and print Eligible or Not eligible.



matric = int(input("Enter Matric percentage: "))
inter = int(input("Enter Inter percentage: "))
entry = int(input("Enter Entry test marks: "))
if (matric >= 60 and inter >= 50) or entry >= 70:
    print("Eligible")
else:
    print("Not eligible")
