# ==========================================
# IF-ELSE PRACTICE QUESTIONS
# ==========================================


# Q1. Write a program to check whether a person is an adult or a minor.
# A person is considered an adult if their age is 18 or above.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# ==========================================
# Q2. Write a program to check whether a given number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==========================================
# Q3. Write a program to check whether a given number is positive,
# negative, or zero using separate if statements.

num = int(input("Enter number: "))

if num > 0:
    print("Positive")

if num < 0:
    print("Negative")

if num == 0:
    print("Zero")


# ==========================================
# Q4. Write a program to check whether a given number is positive,
# negative, or zero using if-elif-else statements.

num = int(input("Enter number: "))

if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")


# ==========================================
# Q5. Write a program to check whether a number is:
# - Even Positive
# - Odd Positive
# - Even Negative
# - Odd Negative
# - Zero
# Use nested if-else statements.

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Even Positive")
    else:
        print("Odd Positive")

elif num < 0:
    if num % 2 == 0:
        print("Even Negative")
    else:
        print("Odd Negative")

else:
    print("Zero")


# ==========================================
# Q6. Write a program to check whether a number is:
# - Even Positive
# - Odd Positive
# - Even Negative
# - Odd Negative
# - Zero
# Use if-elif-else and logical operators.

num = int(input("Enter a number: "))

if num == 0:
    print("Zero")

elif num % 2 == 0 and num > 0:
    print("Even Positive")

elif num % 2 == 0 and num < 0:
    print("Even Negative")

elif num % 2 != 0 and num > 0:
    print("Odd Positive")

else:
    print("Odd Negative")


# ==========================================
# Q7. Write a program to find and print the greater of two numbers.

a = 55
b = 65

if a >= b:
    print(a)
else:
    print(b)


# ==========================================
# Q8. Write a program to assign a grade based on marks:
#
# 90 or above  -> Grade A
# 75 to 89     -> Grade B
# 50 to 74     -> Grade C
# Below 50     -> Grade D

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Grade D")
