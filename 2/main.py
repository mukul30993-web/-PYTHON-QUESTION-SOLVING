num = int(input("Enter number:"))
reverse = 0;

while num >0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = 10 // 10

print (reverse)