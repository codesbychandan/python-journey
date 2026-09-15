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
