# Python Basics - Theory

## 1. Taking Input

The `input()` function is used to take input from the user.

Example:

name = input("Enter your name: ")
print(name)

By default, `input()` returns the value as a STRING.

---

## 2. Taking Integer Input

If we want to take a number as an integer, we use `int()`.

Example:

age = int(input("Enter your age: "))

Here:

input() → takes input from the user
int() → converts the input into an integer

---

## 3. Taking Decimal Input

For decimal numbers, we use `float()`.

Example:

marks = float(input("Enter your marks: "))

---

## 4. Data Type Conversion

Changing one data type into another is called type conversion.

Examples:

int("10")       → 10
float("10.5")   → 10.5
str(100)        → "100"

---

## 5. If Statement

`if` is used to execute a block of code when a condition is true.

Example:

age = 20

if age >= 18:
    print("Adult")

---

## 6. If-Else Statement

`else` is executed when the `if` condition is false.

Example:

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

---

## 7. If-Elif-Else

`elif` means "else if".

It is used when we have multiple conditions.

Example:

marks = 80

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

---

## 8. Comparison Operators

Comparison operators are used to compare values.

>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to
!=  Not equal to

Example:

age >= 18

---

## 9. Logical Operators

### AND

Both conditions must be true.

Example:

age >= 18 and age <= 60

### OR

At least one condition must be true.

Example:

marks >= 90 or marks == 100

### NOT

Reverses the condition.

Example:

not(age >= 18)

---

## 10. Modulus Operator %

`%` gives the remainder after division.

Example:

10 % 2 = 0
11 % 2 = 1

It is commonly used to check whether a number is even or odd.

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

---

## 11. Indentation

Python uses indentation (spaces) to define a block of code.

Correct:

if age >= 18:
    print("Adult")

Incorrect:

if age >= 18:
print("Adult")

Usually, 4 spaces are used for indentation.
