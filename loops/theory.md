# Python Loops: for and while


'''

Beginner Notes and Common Mistakes

1. What is a Loop?
A loop is used when we want to repeat a task multiple times. Instead of writing the same code again and
again, we use a loop.

Example without a loop:
print("Hello")
print("Hello")
print("Hello")'''
# Example with a loop:
for i in range(3):
    print("Hello")

'''
2. The for Loop
A for loop is generally used when we know how many times we want to repeat something.
Basic syntax:
for variable in range(...):
# code to repeat'''
# Example:
for i in range(5):
    print("Hello")


# This prints Hello 5 times. The variable i changes during each iteration.
'''
3. Understanding range()
range() is commonly used with a for loop to control how many times the loop runs.
range(5)'''

for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4. Python starts from 0 by default and stops before 5.
# range(1, 6)


for i in range(1, 6):
    print(i)
'''
Output: 1, 2, 3, 4, 5. The first number is the starting value. The second number is not included.'''


# 5. Using if Statements Inside a for Loop
# We can combine loops and conditions.
# Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
''
# The % operator gives the remainder. If the remainder after division by 2 is 0, the number is even.


'''   
6. The while Loop
A while loop repeats code as long as its condition is True. It is useful when the number of repetitions
depends on a condition.
Basic syntax:
while condition:
# code to repeat
# update the condition
Example: Print 1 to 5'''

i = 1
while i <= 5:
    print(i)
i += 1
'''
The loop starts with i = 1. After every iteration, i += 1 increases i by 1. When i becomes 6, the condition i
<= 5 becomes False and the loop stops.'''

'''   
7. Important: Updating the Variable
In a while loop, we usually need to update the variable used in the condition. Otherwise, the condition may
remain True forever and create an infinite loop.'''

# Correct:
i = 1
while i <= 5:
        print(i)
i += 1

# Incorrect idea:
i = 1
while i <= 5:
     print (i)

# Here i never changes, so the loop keeps running.

'''   
8. Common Mistake: Putting i += 1 Inside the Wrong Block
A mistake I made while printing even numbers was:'''

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
        i +=1
'''   
Why is this wrong? When i = 1, the if condition is False. Therefore i += 1 does not run. The value of i
remains 1 forever, so the while loop never progresses.
Correct version:'''
i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)
    
    i += 1
'''   
The indentation is important. i += 1 is outside the if block but inside the while block, so it runs during every
iteration.'''
# 9. A Simpler Way to Print Even Numbers

i = 2
while i <= 20:
    print(i)
i += 2
'''   
This starts from 2 and increases by 2 each time, so only even numbers are printed.

11. Indentation in Python
Python uses indentation (spaces at the beginning of a line) to show which code belongs to a loop or
condition.'''


