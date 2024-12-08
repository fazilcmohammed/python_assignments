# 1. Accept two inputs from the user and output its sum.

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
sum = num1 + num2
print(f"the sum of your numbers is {sum}")

# 2. Write a program to find the simple interest.
# a. Program should accept 3 inputs from the user and calculate simple interest for the given inputs.
#     Formula: SI=(P*R*n)/100)

p = int(input('Enter the amount : '))
r = int(input('Enter the interest percentage per annum: '))
t = int(input('How long is being invested (by years): '))
si = int((p*r*t)/100)
print(f"The Simple Interest for your amount is {si}")

# 3.  Write a program to check whether a student has passed or failed in a subject after he or she enters
#     their mark (pass mark for a subject is 50 out of 100).
#     b. Program should accept an input from the user and output a message as “Passed” or “Failed”

mark = int(input('Pls enter your score: '))

if mark >= 50:
    print("Congrates, you passed!")
else:
    print('Sorry, you failed.')

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


# 5.	Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 

day = int(input('Enter a number: '))

match day:
    case 1:
        print('Sunday') 
    case 2:
        print('Monday') 
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Invalid Entry') 

# 6.	Write a program to print the multiplication table of given numbers.
# a.	Accept an input from the user and display its multiplication table

num = int(input('Enter a number: '))

table = range(1, 11)

for n in table:
    product = n * num
    print(f"{n}*{num} = {product} ")


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
print(f"Sum of odd numbers: {sum}")
    

# 8.	Write a program to print the following pattern (hint: use nested loop)

row = 5

for r in range(1, row+1):
    for c in range(1, r+1):
        print(c, end=' ')
    print()


# 9.	Write a program to interchange the values of two arrays.
# a.	Program should accept an array from the user, swap the values of two arrays and display it on the console

size = int(input('Enter the size of array: '))
arr1 = []
arr2 = []

for num in range(size):
    if num <= size:
        number = int(input('Enter a number to array 1 : '))
        arr1.append(number)

for num in range(size):
    if num <= size:
        numberr = int(input('Enter a number to array 2 : '))
        arr2.append(numberr)

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
# arr1 = [5, 10, 15, 20, 25]
# arr2 = [3,6,9,12,15]

arr1, arr2 = arr2, arr1
print('INTERCHANGED:')
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")


# 10. Write a program to find the number of even numbers in an array
# a.	Program should accept an array and display the number of even numbers contained in that array


size = int(input('Enter the size of array: '))
arr = []

for i in range(size):
    num = int(input('Enter a number: '))
    arr.append(num)
print(arr)

count = 0

for n in arr:
    if n%2==0:
        count += 1
print(f"Number of even numbers in the given array is {count}")


# 11.	 Write a program to sort an array in descending order
# a.	Program should accept and array, sort the array values in descending order and display it

size = int(input('Enter the size of array: '))
arr = []

for i in range(size):
    num = int(input('Enter a number: '))
    arr.append(num)
print(arr)

arr.sort(reverse=True)
print(f"Sorted array: {arr}")


# 12.	Write a program to identify whether a string is a palindrome or not
# a.	A string is a palindrome if it reads the same backward or forward eg: MALAYALAM
# Program should accept a string and display whether the string is a palindrome or not

word = input('Enter a word: ')
forward = word.upper()
reverse = word[::-1]
backward = reverse.upper()


if forward == backward:
    print(f"{forward} is a palindrome")
else:
    print(f"{forward} is not a palindrome")


# 13. Write a program to accept an array and display it on the console using functions
# a.	Program should contain 3 functions including main() function

arr1 = []

def getArray():
    limit = int(input('Enter the array limit: '))
    for i in range(limit):
        num = int(input('Enter number: '))
        arr1.append(num)

def displayArray():
    print(arr1)


def main():
    getArray()
    displayArray()

displayArray()



# 14.	Write a java program to check whether a given number is prime or not
# a.	Program should accept an input from the user and display whether the number is prime or not

num = int(input('Enter a number: '))

if num>1:
    for i in range(2, (num//2)+1):
        if num%2 == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number")


# 15. Write a menu driven java program to do the basic mathematical operations such as addition, subtraction, multiplication and division (hint: use if else ladder or switch)
# a.	Program should have 4 functions named addition(), subtraction(), multiplication() and division()
# b.	Should create a class object and call the appropriate function as user prefers in the main function


def multiplication(num1, num2):
    print( num1 * num2)

def addition(num1, num2):
    print( num1 + num2)

def substraction(num1, num2):
    print( num1 - num2)

def division(num1, num2):
    print( num2/num1)

usr = int(input('choose an operation: \n 1 - Multiplication \n 2 - Addition \n 3 - Substraction \n 4 - Division \n'))
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

match usr:
    case 1:
        multiplication(num1, num2)
    case 2:
        addition(num1, num2)
    case 3:
        substraction(num1, num2)
    case 4:
        division(num1, num2)

# 16.	Write a program to print the following pattern using for loop


row = 4
num = 1

for r in range(1,row+1):
    for i in range(1, r+1):
        print(num, end=' ')
        num += 1
    print()