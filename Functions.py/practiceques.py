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
# Q6. Find the First Non-Repeating Character
# in a String Using a Function.
#
# Example:
# Input: "aabbcde"
# Output: c
#
# If no such character exists, return None.
# ==================================================

def first_non_repeating(text):

    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


text = "aabbcde"

print("First non-repeating character:",
      first_non_repeating(text))


# ==================================================
# Q7. Find the Missing Number in a List.
#
# A list contains numbers from 1 to n,
# but one number is missing.
#
# Example:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Do not use sorting.
# ==================================================

def find_missing(numbers):

    n = len(numbers) + 1

    expected_sum = n * (n + 1) // 2

    actual_sum = 0

    for num in numbers:
        actual_sum += num

    return expected_sum - actual_sum


numbers = [1, 2, 3, 5, 6]

print("Missing number:", find_missing(numbers))


# ==================================================
# Q8. Rotate a List to the Right by K Positions.
#
# Example:
# Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
#
# Use a function.
# ==================================================

def rotate_list(numbers, k):

    if not numbers:
        return []

    k = k % len(numbers)

    return numbers[-k:] + numbers[:-k] if k else numbers[:]


numbers = [1, 2, 3, 4, 5]
k = 2

print("Rotated list:", rotate_list(numbers, k))


# ==================================================
# Q9. Find the Longest Word in a Sentence.
#
# Example:
# Input: "Python programming improves problem solving"
# Output: programming
#
# If multiple words have the same maximum length,
# return the first one.
# ==================================================

def longest_word(sentence):

    words = sentence.split()

    if not words:
        return None

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = "Python programming improves problem solving"

print("Longest word:", longest_word(sentence))


# ==================================================
# Q10. Check Whether a List Is a Subset of Another.
#
# Example:
# List 1: [2, 4, 6]
# List 2: [1, 2, 3, 4, 5, 6, 7]
#
# Output: True
#
# Account for duplicate elements.
# ==================================================

def is_subset(list1, list2):

    frequency = {}

    for num in list2:
        frequency[num] = frequency.get(num, 0) + 1

    for num in list1:

        if num not in frequency or frequency[num] == 0:
            return False

        frequency[num] -= 1

    return True


list1 = [2, 4, 6]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("Is subset:", is_subset(list1, list2))
