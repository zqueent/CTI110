#Taylor Queen
#5/2/2024
#P4LAB2
#Range and looping for multiplication table.

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")

    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")

print("Exiting program...")
                                
