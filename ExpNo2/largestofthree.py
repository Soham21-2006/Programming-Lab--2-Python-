a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
for num in (b, c):
    if num > largest:
        largest = num

print("Largest number is:", largest)