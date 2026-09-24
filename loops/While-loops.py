# ==========================================
# WHILE LOOP - INTERMEDIATE PRACTICE
# ==========================================


# Q1. Write a program to reverse a number using a while loop.
#
# Example:
# Input: 12345
# Output: 54321

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)


# ==========================================
# Q2. Write a program to count the number of digits
# in a given number using a while loop.
#
# Example:
# Input: 45892
# Output: 5
# ==========================================

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits:", count)


# ==========================================
# Q3. Write a program to find the sum of digits
# of a number using a while loop.
#
# Example:
# Input: 12345
# Output: 15
# ==========================================

num = int(input("Enter a number: "))

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print("Sum of digits:", total)


# ==========================================
# Q4. Write a program to check whether a number
# is a palindrome using a while loop.
#
# Example:
# Input: 121
# Output: Palindrome
#
# Input: 123
# Output: Not Palindrome
# ==========================================

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# ==========================================
# Q5. Write a program to find the factorial of
# a given number using a while loop.
#
# Example:
# Input: 5
# Output: 120
# ==========================================

num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial:", factorial)


# ==========================================
# Q6. Write a program to count the number of
# even and odd digits in a given number.
#
# Example:
# Input: 123456
# Even digits: 3
# Odd digits: 3
# ==========================================

num = int(input("Enter a number: "))

even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    num = num // 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)


# ==========================================
# Q7. Write a program to find the largest digit
# in a given number using a while loop.
#
# Example:
# Input: 58329
# Output: 9
# ==========================================

num = int(input("Enter a number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)


# ==========================================
# Q8. Write a program that repeatedly asks the
# user to enter numbers and stops when the user
# enters 0.
#
# Print the sum of all numbers entered.
# ==========================================

total = 0

num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))

print("Total:", total)


# ==========================================
# Q9. Write a program that keeps asking the user
# for a password until the correct password is entered.
#
# Correct password: 1234
# ==========================================

password = int(input("Enter password: "))

while password != 1234:
    print("Wrong password!")
    password = int(input("Enter password: "))

print("Access granted!")


# ==========================================
# Q10. Write a program to print the multiplication
# table of a number using a while loop.
#
# Example:
# Input: 7
#
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
# ==========================================

num = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
