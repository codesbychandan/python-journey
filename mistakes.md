# 🧠 Mistakes & Lessons

This file contains mistakes I made while learning Python and what I learned from them.

---

## 1. `=` vs `==`

### Mistake

```python
if age = 18:
    print("18")
Correct
if age == 18:
    print("18")
Lesson
= is used for assignment.
== is used for comparison.
2. input() returns a string
Mistake
age = input("Enter your age: ")

if age >= 18:
    print("Adult")
Correct
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
Lesson
input() returns a string by default.
Use int() when an integer is required.
3. Checking even and odd
Correct
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
Lesson
The modulus operator % gives the remainder.
If the remainder after division by 2 is 0, the number is even.
4. Indentation
Incorrect
if age >= 18:
print("Adult")
Correct
if age >= 18:
    print("Adult")
Lesson
Python uses indentation to define blocks of code.
5. if vs elif
Multiple independent if statements can all be checked.
if num > 0:
    print("Positive")

if num < 0:
    print("Negative")
With if-elif-else, Python follows one matching branch.
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
Lesson
Use if-elif-else when the conditions are alternatives.
6. Starting counters from 0
Example:
even_count = 0
odd_count = 0
Lesson
Counters usually start from 0 because initially we have counted nothing.
