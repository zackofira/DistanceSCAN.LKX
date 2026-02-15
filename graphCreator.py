import matplotlib.pyplot as plt

# Sample data
x = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35]

# First data set
y1 = [203, 4, 1, 0, 0, 0, 0]

# Second data set
y2 = [200, 174, 134, 84, 13, 9, 6]

# Plot both lines
plt.plot(x, y1, label='Dataset 1', color='blue', marker='o')
plt.plot(x, y2, label='Dataset 2', color='red', linestyle='--', marker='s')

# Add labels and title
plt.title('Line Graph with Two Data Sets')
plt.xlabel('μ')
plt.ylabel('Average Cluster Size')

# Add a legend
plt.legend()

# Optional grid
plt.grid(True)

# Show the plot
plt.show()