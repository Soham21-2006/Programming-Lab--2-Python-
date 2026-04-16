# Recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input
num = int(input("Enter number of terms: "))

# Generate series
print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")