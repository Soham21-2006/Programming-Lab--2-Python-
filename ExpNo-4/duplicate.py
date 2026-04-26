n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    num = int(input("Enter number: "))
    my_list.append(num)

new_list = []

for num in my_list:
    if num not in new_list:
        new_list.append(num)

print("Original list:", my_list)
print("After removing duplicates:", new_list)