with open("example.txt", "r") as file:
    data = file.read()

lines = data.split('\n')
words = data.split()
chars = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)