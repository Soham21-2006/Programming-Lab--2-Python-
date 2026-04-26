n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    num = int(input("Enter element: "))
    my_list.append(num)

my_list.sort()

print("Second largest element:", my_list[-2])