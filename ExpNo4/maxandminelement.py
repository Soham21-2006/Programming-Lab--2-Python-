n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    num = int(input("Enter number: "))
    my_list.append(num)

print("List:", my_list)
print("Maximum element:", max(my_list))
print("Minimum element:", min(my_list))