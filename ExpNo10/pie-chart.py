import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 25, 25]
colors = ['gold', 'lightblue', 'lightgreen', 'pink']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Title
plt.title("Simple Pie Chart")

# Show chart
plt.show()