from cProfile import label
import matplotlib.pyplot as plt
import numpy as np 
# Создание данных для графика
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Создание сложного графика с несколькими подграфиками
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)


ax1.plot(x, y1, 'r-', label='sin(x)')
ax1.set_ylabel('Значение')
ax1.legend()

#
ax2.plot(x, y2, 'r-', label='cos(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('Значение')
ax2.legend()

plt.show()


categories = ['Category 1', 'Category 2', 'Category 3']
month = ['January', 'February', 'March', 'April']
sales = [[100, 150, 200, 250], [50, 100, 150, 200], [200, 250, 300, 350]]

#
plt.figure(figsize=(10, 6))
for i in range(len(categories)):
    plt.plot(month, sales[i], label=categories[i])

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales by month and category')
plt.legend()
plt.show()