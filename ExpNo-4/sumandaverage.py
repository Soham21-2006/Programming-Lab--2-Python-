n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    num = int(input("Enter number: "))
    my_list.append(num)

total = sum(my_list)
average = total / n

print("List:", my_list)
print("Sum:", total)
print("Average:", average)