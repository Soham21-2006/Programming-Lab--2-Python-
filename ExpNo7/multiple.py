# Function returning multiple values
def calc(a, b):
    return a + b, a - b
# Call function
sum_val, diff_val = calc(10, 5)
# Display results
print("Sum:", sum_val)
print("Difference:", diff_val)