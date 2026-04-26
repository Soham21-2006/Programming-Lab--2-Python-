# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input
num = int(input("Enter a number: "))

# Output
print("Factorial:", factorial(num))