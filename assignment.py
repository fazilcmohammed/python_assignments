# 1. Accept two inputs from the user and output its sum.

# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter another number: '))
# sum = num1 + num2
# print(f"the sum of your numbers is {sum}")

# 2. Write a program to find the simple interest.
# a. Program should accept 3 inputs from the user and calculate simple interest for the given inputs.
#     Formula: SI=(P*R*n)/100)

# p = int(input('Enter the amount : '))
# r = int(input('Enter the interest percentage per annum: '))
# t = int(input('How long is being invested (by years): '))
# si = int((p*r*t)/100)
# print(f"The Simple Interest for your amount is {si}")

# 3.  Write a program to check whether a student has passed or failed in a subject after he or she enters
#     their mark (pass mark for a subject is 50 out of 100).
#     b. Program should accept an input from the user and output a message as “Passed” or “Failed”

# mark = int(input('Pls enter your score: '))

# if mark >= 50:
#     print("Congrates, you passed!")
# else:
#     print('Sorry, you failed.')

# 4.  Write a program to show the grade obtained by a student after he/she enters their total mark
#     percentage.
#     b. Program should accept an input from the user and display their grade as follows

percentage = int(input('Enter your total mark percentage: '))

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print(f"Your grade is: {grade}")
