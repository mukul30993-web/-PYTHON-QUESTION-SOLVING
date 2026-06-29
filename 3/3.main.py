largest = None

for i in range(5):
    num = int(input("Enter a number: "))

    if largest is None or num > largest:
        largest = num

print("Largest number is:", largest)