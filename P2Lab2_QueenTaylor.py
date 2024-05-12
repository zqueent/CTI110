#Taylor Queen
#4/19/2024
#P2Lab2
#Writing code that uses a dictionary to store user input and displays output to the user

cars = {'Camaro':18.21, 'Prius':52.36, 'Model_S':110, 'Silverado':26}
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

car_name = input("Eneter a vehicle to see its mpg: ")
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

miles_driven = float(input(f"How many miles will you drive the {car_name}?" ))

gallons_needed = miles_driven/car_mpg
print(f"{gallons_needed} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")                   


