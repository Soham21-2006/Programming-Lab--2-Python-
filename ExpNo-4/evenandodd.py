n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    num = int(input("Enter element: "))
    my_list.append(num)

even_count = 0
odd_count = 0

for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", my_list)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)