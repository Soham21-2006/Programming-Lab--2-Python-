import matplotlib.pyplot as plt

# Data
data = [10, 12, 15, 20, 22, 25, 30, 35, 40, 45, 50]

# Create histogram
plt.hist(data, bins=5)

# Labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram Example")

# Show plot
plt.show()