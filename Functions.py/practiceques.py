# ==================================================
# Q1. Find the Second Largest Unique Element
# in a List Using a Function.
#
# Example:
# Input: [10, 20, 4, 45, 99, 99]
# Output: 45
#
# Note: Do not use sort() or sorted().
# ==================================================

def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num

        elif largest > num > second:
            second = num

    if second == float('-inf'):
        return None

    return second


numbers = [10, 20, 4, 45, 99, 99]

print("Second largest:", second_largest(numbers))


# ==================================================
# Q2. Find All Pairs Whose Sum Equals Target.
#
# Example:
# Input: [2, 7, 11, 15, 3, 6], Target = 9
#
# Output:
# (2, 7)
# (3, 6)
#
# Use a function.
# ==================================================

def find_pairs(numbers, target):
    pairs = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


numbers = [2, 7, 11
