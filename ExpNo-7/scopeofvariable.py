# Global variable
x = 10

def func():
    # Local variable
    x = 5
    print("Inside function (local x):", x)

func()

# Access global variable
print("Outside function (global x):", x)