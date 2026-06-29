import random
import math


numbers = [12, 5, 9, 18, 21, 30, 44, 51]


def square_list(data):
    results = []
    for i in data:
        results.append(i ** 2)
    return results


def even_numbers(data):
    even = []
    for n in data:
        if n % 2 == 0:
            even.append(n)
    return even


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def reverse_string(text):
    return text[::-1]


def largest(data):
    biggest = data[0]
    for i in data:
        if i > biggest:
            biggest = i
    return biggest


def average(data):
    total = 0
    for i in data:
        total += i
    return total / len(data)


def count_vowels(text):
    count = 0
    vowels = "aeiou"

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count


def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def remove_duplicates(data):
    return list(set(data))


def greeting(name):
    print("Hello", name)


# ---------------- MAIN PROGRAM ----------------

text = input("Enter text: ")

nums = input("Enter numbers (comma separated): ").split(",")
nums = [int(i) for i in nums]

print("\nSquare List:", square_list(nums))
print("Even Numbers:", even_numbers(nums))
print("Factorial of 5:", factorial(5))
print("Is 17 Prime?:", is_prime(17))
print("Reverse String:", reverse_string(text))
print("Largest Number:", largest(nums))
print("Average:", average(nums))
print("Vowel Count:", count_vowels(text))

print("Fibonacci Series:")
fibonacci(10)

print("Remove Duplicates:", remove_duplicates(nums))

greeting("Mukul")

print("\nLoop Output:")
for i in range(5):
    print(i)

x = random.randint(1, 10)
print("\nRandom Number:", x)

print("Square Root of 81:", math.sqrt(81))

if len(nums) > 5:
    print("Large List")
else:
    print("Small List")

print("\nProgram Finished Successfully!")