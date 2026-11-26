
import matplotlib.pyplot as plt

# Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Box Plot
marks = [40, 50, 60, 70, 80, 90]
plt.boxplot(marks)
plt.title("Box Plot")
plt.show()

# Bar Chart
items = ["Apple", "Mango", "Banana", "Orange"]
prices = [50, 60, 30, 40]

plt.bar(items, prices)
plt.title("Bar Chart")
plt.xlabel("Items")
plt.ylabel("Prices")
plt.show()

# Pie Chart
labels = ["Apple", "Mango", "Banana", "Orange"]
values = [25, 30, 20, 25]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
