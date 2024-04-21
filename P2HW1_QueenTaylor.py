#Taylor Queen
#4/19/2024
#P2WH2
#Build onto P1HW2 assignment.

print('This program calculates and displays travel expenses') 
print()
Budget = int(input("Enter Budget:")) 
print()
Desti = input("Enter your travel destination:") 
print()
Gas_Budget = int(input("How much do you think you will spend on gas?")) 
print()
Stay = int(input("Approximately, how much will you need for accomodation/hotel?"))
print()
Food = int(input("Last, how much will you need for food?")) 
print()
print("-------Travel Expenses-------")
print("Location:", Desti) 
print(f"Initial Budget: ${Budget:.2f}")
print(f"Fuel: ${Gas_Budget:.2f}")
print(f"Accomodation: ${Stay:.2f}")
print(f"Food: ${Food:.2f}")
print("-----------------------------")
print(f"Remaining Balance: ${Budget - Gas_Budget - Stay - Food:.2f}")

