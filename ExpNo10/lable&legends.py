import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 20, 25, 30]
y2 = [5, 10, 15, 20, 25]

# Plot first line
plt.plot(x, y1, label="Series 1", marker='o')

# Plot second line
plt.plot(x, y2, label="Series 2", marker='s')

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Plot with Labels and Legends")

# Show legend
plt.legend()

# Add grid
plt.grid(True)

# Show plot
plt.show()