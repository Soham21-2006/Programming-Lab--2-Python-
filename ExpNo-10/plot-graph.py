import matplotlib.pyplot as plt

x = []
y = []

# Open and read file
with open("ExpNo10/data.txt", "r") as file:
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

# Plot graph
plt.plot(x, y, marker='o')

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph from File Data")

# Show grid
plt.grid(True)

# Show plot
plt.show()