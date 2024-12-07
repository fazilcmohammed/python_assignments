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

# percentage = int(input('Enter your total mark percentage: '))

# if percentage >= 90:
#     grade = "A"
# elif percentage >= 80:
#     grade = "B"
# elif percentage >= 70:
#     grade = "C"
# elif percentage >= 60:
#     grade = "D"
# else:
#     grade = "F"

# # Display the grade
# print(f"Your grade is: {grade}")


# 5.	Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 

# day = int(input('Enter a number: '))

# match day:
#     case 1:
#         print('Sunday') 
#     case 2:
#         print('Monday') 
#     case 3:
#         print('Tuesday')
#     case 4:
#         print('Wednesday')
#     case 5:
#         print('Thursday')
#     case 6:
#         print('Friday')
#     case 7:
#         print('Saturday')
#     case _:
#         print('Invalid Entry') 

# 6.	Write a program to print the multiplication table of given numbers.
# a.	Accept an input from the user and display its multiplication table

# num = int(input('Enter a number: '))

# table = range(1, 11)

# for n in table:
#     product = n * num
#     print(f"{n}*{num} = {product} ")


# 7.	Write a program to find the sum of all the odd numbers for a given limit
# a.	Program should accept an input as limit from the user and display the sum of all the odd numbers within that limit

limit = int(input('Enter a limit: '))

num = range(1, limit+1)
odd_num = []
sum = 0

for n in num:
    if n%2 !=0:
        odd_num.append(n)
        sum += n

print(odd_num)
print(sum)
    