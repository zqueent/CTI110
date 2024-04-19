#Taylor Queen
#4/19/2024
#P1WH2
#User Budget Input/Output.

print('This program calculates and displays travel expenses')
Budget = int(input("Enter Budget:"))
Desti = input("Enter your travel destination:")
Gas_Budget = int(input("How much do you think you will spend on gas?"))
Stay = int(input("How much will you need for a hotel?"))
Food = int(input("How much will you need for food?"))

print("-------Travel_Expenses-------")
print("Location:", Desti)
print("Initial Budget:", Budget)
print()
print("Fuel:", Gas_Budget)
print("Accomodation:", Stay)
print("Food", Food)
print()
print("Remaining Balance:", Budget-Gas_Budget-Stay-Food)



