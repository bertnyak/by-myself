from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

categories = ['Category 1', 'Category 2', 'Category 3']
month = ['January', 'February', 'March', 'April']
sales = np.array([[100, 150, 200, 250], [50, 100, 150, 200], [200, 250, 300, 350]])

plt.figure(figsize=(10, 6))
bar_width = 0.2
for i in range(len(categories)):
    plt.bar(np.arange(len(month))+ i * bar_width,sales[i], width=bar_width, label=categories[i])

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Comparison by Month and Category')
plt.xticks(np.arange(len(month)) + bar_width * len(categories) - 1 / 2, month)
plt.legend()
plt.show()

# Тепловая карта продаж по категориям и месяцам
categories = ['Category 1', 'Category 2', 'Category 3']
month = ['January', 'February', 'March', 'April']
sales = np.array([[100, 150, 200, 250], [50, 100, 150, 200], [200, 250, 300, 350]])

plt.figure(figsize=(10, 6))
plt.imshow(sales, cmap='hot')

plt.xlabel('Month')
plt.ylabel('Category')
plt.title('Sales Heatmap by Month and Category')
plt.xticks(np.arange(len(month)), month)
plt.yticks(np.arange(len(categories)), categories)
plt.colorbar(label='Sales')
plt.show()