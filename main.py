import matplotlib.pyplot as plt

# List of fruits
fruits = ['Applee', 'Guava', 'Orange', 'Grapes', 'Watermelon']

# Corresponding quantities or counts
quantities = [25, 18, 30, 15, 10]

# Create a bar chart
plt.bar(fruits, quantities, color='skyblue')

# Add labels and title
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')

# Display the bar chart
plt.show()

# Save the graph as an image file (e.g., PNG)
plt.savefig('fruits.png')
