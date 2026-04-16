# Open source file and read data
with open("ExpNo9/example.txt", "r") as source:
    data = source.read()

# Write data into target file
with open("target.txt", "w") as target:
    target.write(data)

print("File copied successfully.")