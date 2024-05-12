#Taylor Queen
#4/22/2024
#P3HW1
# This program takes a number grade , determines average and displays letter grade for average.


mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
print()
print("-----------Results-----------")



average = sum(grades)/len(grades)

print(f'Average: {average}')

print("-----------------------------")

if average >= 90:
    print('Your grade is an: A')
elif average >= 80:
    print('Your grade is a: B')
elif average >= 70:
    print('Your grade is a: C')
elif average >= 60:
    print('Your grade is a: D')
elif average < 60:
    print('Your grade is a: F') 





   






