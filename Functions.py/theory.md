
# Python Functions - Theory Notes

## 1. What is a Function?

A function is a reusable block of code that performs a specific task. It helps us avoid repeating the same code multiple times.

Example:
```python
def greet():
    print("Hello, World!")

greet()
```

Output:
```text
Hello, World!
```

## 2. Advantages of Functions

- Code reusability
- Reduces code repetition
- Makes programs easier to understand
- Makes debugging and testing easier
- Divides large programs into smaller parts

## 3. Defining and Calling a Function

The `def` keyword is used to define a function. A function runs when it is called.

Syntax:
```python
def function_name():
    # Code to execute
    pass

function_name()
```

Example:
```python
def welcome():
    print("Welcome to Python")

welcome()
```

## 4. Parameters and Arguments

**Parameters** are variables written inside the function definition.

**Arguments** are the actual values passed when calling the function.

Example:
```python
def greet(name):  # name is a parameter
    print("Hello", name)

greet("Chandan")  # "Chandan" is an argument
```

Output:
```text
Hello Chandan
```

## 5. Functions with Multiple Parameters

A function can accept more than one parameter.

Example:
```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:
```text
30
```

## 6. The return Statement

The `return` statement sends a result back to the caller. It also ends the function's execution.

Example:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Output:
```text
8
```

### Difference Between print() and return

- `print()` displays information on the screen.
- `return` sends a value back so it can be stored or used in another expression.

## 7. Default Arguments

A default argument is a parameter that already has a value. If no argument is provided for it, the default value is used.

Example:
```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Chandan")
```

Output:
```text
Hello Student
Hello Chandan
```

## 8. Keyword Arguments

Keyword arguments pass values using parameter names. The order of arguments does not matter when they are passed by name.

Example:
```python
def student(name, age):
    print(name, age)

student(age=19, name="Rahul")
```

Output:
```text
Rahul 19
```

## 9. Local and Global Variables

### Local Variable
A variable created inside a function is generally local to that function.

Example:
```python
def show():
    x = 10
    print(x)

show()
```

### Global Variable
A variable created outside functions is global and can generally be accessed inside functions.

Example:
```python
x = 100

def show():
    print(x)

show()
```

The `global` keyword can be used when a function needs to reassign a global variable.

## 10. The pass Statement

The `pass` statement does nothing. It can be used as a placeholder when writing a function that will be completed later.

Example:
```python
def calculate():
    pass
```

## 11. Recursion

Recursion occurs when a function calls itself to solve a smaller version of a problem.

A recursive function needs a **base case** to stop the repeated calls.

Example:
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:
```text
120
```

## 12. Lambda Functions

A lambda function is a small anonymous function written using the `lambda` keyword. It can contain only one expression.

Syntax:
```python
lambda arguments: expression
```

Example:
```python
square = lambda x: x * x

print(square(5))
```

Output:
```text
25
```

## 13. Functions with Lists

Functions can accept lists as arguments and process their elements.

Example:
```python
def find_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(find_sum([10, 20, 30]))
```

Output:
```text
60
```

## 14. Function with Multiple Return Values

Python allows a function to return multiple values. They are received as a tuple unless unpacked into separate variables.

Example:
```python
def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)
```

Output:
```text
15
5
```

## 15. Important Points to Remember

- Use `def` to define a function.
- Use parentheses `()` to call a function.
- Indentation is required inside a function.
- Parameters receive values; arguments provide values.
- `return` sends a result back to the caller.
- A function without an explicit return statement returns `None`.
- Default arguments make parameters optional.
- Recursion requires a suitable base case.
- Functions improve code reusability and readability.

## 16. Practice Questions

1. Write a function to find the square of a number.
2. Write a function to check whether a number is even or odd.
3. Write a function to find the largest of three numbers.
4. Write a function to calculate the factorial of a number.
5. Write a function to check whether a number is prime.
6. Write a function to reverse a string.
7. Write a function to find the sum of digits of a number.
8. Write a recursive function to calculate the sum of numbers from 1 to n.
9. Write a function to find the second largest unique number in a list.
10. Write a function that counts the vowels in a string.
