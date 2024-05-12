#Taylor Queen
#5/5/2024
#P4WH1
#Using Loops

valid_grades = []
scores = int(input('How many grades do you want to enter?'))
for item in range(scores):
    grade = int(input('Enter a score:'))
    while grade < 0 or grade > 100:
        print('Invalid score entered!!!!')
        print('Score should be between 0 and 100')
        grade = int(input('Try again:'))
    valid_grades.append(grade)
print(valid_grades)
lowest = min(valid_grades)
valid_grades.remove(lowest)
print(valid_grades)
average = sum(valid_grades)/len(valid_grades)
print(average)

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')    
elif average >= 60:
    print('Your grade is: D')
elif average < 60:
    print('Your grade is: F')    
