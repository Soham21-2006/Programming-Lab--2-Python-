num = int(input("Enter a number: "))

reverse = 0

sign = -1 if num < 0 else 1
num = abs(num)

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

reverse = reverse * sign

print("Reversed number =", reverse)