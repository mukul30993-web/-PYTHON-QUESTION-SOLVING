import random


def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


def find_smallest(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    return smallest


def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


def count_words(sentence):
    words = sentence.split()
    return len(words)


def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid Operator"


numbers = input("Enter numbers: ").split(",")
numbers = [int(x) for x in numbers]

print("Sum:", sum_numbers(numbers))
print("Smallest:", find_smallest(numbers))

text = input("Enter a word: ")
print("Palindrome:", palindrome(text))

sentence = input("Enter a sentence: ")
print("Words:", count_words(sentence))

num = int(input("Enter a number: "))
multiplication_table(num)

a = int(input("First Number: "))
b = int(input("Second Number: "))
op = input("Operator (+,-,*,/): ")

print("Answer:", calculator(a, b, op))

random_num = random.randint(1, 100)
print("Random Number:", random_num)

if random_num % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(5):
    print(i)

print("Program Finished")