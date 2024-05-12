#Taylor Queen
#5/4/2024
#P4HW2
#Using Loops

num_employees = 0
total_payOT = 0
total_payRH = 0

employee_name = input('Enter employee name or "Done" to terminate:')
while employee_name != "Done":
    num_employees += 1
    
    hours = int(input(f"How many hours did {employee_name} work?"))
    rate = int(input(f"What is {employee_name}'s pay rate?"))
    print()
    print(f"Employee name: {employee_name}")
    if hours > 40:
        reg_hours = 40
        overtime = hours - reg_hours
    else:
        reg_hours = hours
        overtime = 0
    total_payOT += overtime * rate * 1.5
    total_payRH += reg_hours * rate
    print("Hours worked, Pay Rate, OverTime, OverTime Pay, RegPay, GrossPay")
    print(f"{hours}, {rate}, {overtime}, {overtime * rate * 1.5}, {reg_hours * rate}, {(overtime * rate * 1.5) + (reg_hours * rate)}")
    employee_name = input('Enter employee name or "Done" to terminate:')    

print(f"Total number of employees entered: {num_employees}")  
print(f"Total amount paid for OT: {total_payOT}")
print(f"Total amount paid for regular hours: {total_payRH} ")
print(f"Total amount paid in gross: {total_payOT + total_payRH}")  
                
