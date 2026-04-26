n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    num = int(input("Enter number: "))
    my_list.append(num)

my_list.sort()
print("Sorted list (ascending):", my_list)