try:
    # Try to open file
    file = open("example.txt", "r")
    
    data = file.read()
    print(data)

except FileNotFoundError:
    print("Error: File not found.")

except IOError:
    print("Error: Problem reading the file.")

finally:
    print("File handling operation completed.")