      # Basics to moderate level ques## ( FOR AND WHILE ) ##

        ## FOR LOOPS##

#  print no. from 1 to 10

for i in  range (1 , 11):  # range (1, 11) means start from 1 and stops before 11
    print( i ) 

#=============================================================

# Print your name 5 times using loop

for i in range (5):
    print("chandan ")

#=============================================================
# Print squares of numbers from 1 to 5

for i in range (1,6):  
    print(i ** 2 )   # ** means power 

# #=============================================================
# Print only even numbers from 1 to 10

for i in range (1, 11):
    if i % 2 == 0:
        print(i)


# #=============================================================
#  Q. Sum of numbers from 1 to N

n = int(input("enter a num :"))

sum = 0

for i in range(1,n+1):
    sum = sum + i 

print ("sum of numbers from 1 to n is", sum)

# Q.Find the Factorial of a Number

n = int(input("enter a num : "))
total = 1
for i in range (1,n+1):
    total = total*i
print(" factorial of ", n,"is", total) 

#  Q. Multiplication Table
# Take a number from the user and print its multiplication table from 1 to 10.

n = int(input("enter a num : "))
for i in range ( 1, 11):
    print(n*i)  

# Count Even and Odd Numbers
n = int(input("enter a num : "))

even_count = 0
odd_count = 0

for i in range (1, n+1):
    if i % 2 ==0:
        even_count +=1
    else:
        odd_count += 1
print("even nums :",even_count)
print("odd nums ", odd_count)


# ==========================================
# Q1. Find the second largest number
# in a list using a for loop.
#
# Example:
# Input: [10, 25, 8, 40, 30]
# Output: 30
# ==========================================

numbers = [10, 25, 8, 40, 30]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)


# ==========================================
# Q2. Find all pairs of numbers in a list
# whose sum is equal to a given target.
#
# Example:
# List: [2, 4, 3, 7, 5, 8]
# Target: 10
#
# Output:
# 2 + 8 = 10
# 3 + 7 = 10
# ==========================================

numbers = [2, 4, 3, 7, 5, 8]
target = 10

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "+", numbers[j], "=", target)


# ==========================================
# Q3. Find all duplicate elements in a list
# using for loops.
#
# Example:
# Input: [2, 5, 3, 2, 7, 5, 8]
#
# Output:
# 2
# 5
# ==========================================

numbers = [2, 5, 3, 2, 7, 5, 8]
duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicate elements:")

for num in duplicates:
    print(num)


# ==========================================
# Q4. Find the frequency of each character
# in a string using a for loop.
#
# Example:
# Input: "programming"
#
# Output:
# p -> 1
# r -> 2
# o -> 1
# g -> 2
# a -> 1
# m -> 2
# i -> 1
# n -> 1
# ==========================================

text = "programming"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char in frequency:
    print(char, "->", frequency[char])


# ==========================================
# Q5. Check whether a number is a perfect number
# using a for loop.
#
# A perfect number is equal to the sum of its
# proper divisors.
#
# Example:
# Input: 28
# Output: Perfect number
#
# Because:
# 1 + 2 + 4 + 7 + 14 = 28
# ==========================================

num = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")


        ## BASIC QUES ON WHILE LOOPS##

    #   Print numbers 1 to 10 using while
i = 1 
while i <=10:
    print(i)
    i += 1

   # Print even numbers from 1 to 20 using while
i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)
    
    i += 1
    
'''i += 1

is outside the if block but still inside the while loop.

This means i increases every time.'''
#  better version
i = 2
while i <=20:
    print(i)
    i += 2




    #Print your name 5 times using while
i = 1
while i <=5:
    print("chandan ")
    i += 1





# ==========================================
# Q6. Find the largest difference between
# any two elements in a list.
#
# Example:
# Input: [10, 3, 25, 7, 18]
# Output: 22
# ==========================================

numbers = [10, 3, 25, 7, 18]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

difference = largest - smallest

print("Largest difference:", difference)


# ==========================================
# Q7. Count the number of prime numbers
# between two given numbers.
#
# Example:
# Input: 1 to 20
# Output: 8
# ==========================================

start = 1
end = 20
count = 0

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print("Number of prime numbers:", count)


# ==========================================
# Q8. Find the common elements between
# two lists using for loops.
#
# Example:
# List 1: [1, 2, 3, 4, 5]
# List 2: [3, 5, 7, 9]
#
# Output:
# 3
# 5
# ==========================================

list1 = [1, 2, 3, 4, 5]
list2 = [3
    
