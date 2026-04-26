# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Input
num = int(input("Enter a number: "))

# Check and display result
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")