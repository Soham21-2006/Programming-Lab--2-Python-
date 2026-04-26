import matplotlib.pyplot as plt

# Data
data = [12, 15, 18, 22, 25, 28, 30, 35, 40, 45, 50]

# Create box plot
plt.boxplot(data)

# Labels and title
plt.title("Box-and-Whisker Plot")
plt.ylabel("Values")

# Show plot
plt.show()