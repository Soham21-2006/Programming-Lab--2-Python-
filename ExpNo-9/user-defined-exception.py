# Create user-defined exception
class MyException(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise MyException("Negative number is not allowed")

    print("You entered:", num)

except MyException as e:
    print("Error:", e)

except ValueError:
    print("Invalid input.")