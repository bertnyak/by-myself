import matplotlib.pyplot as plt


prices = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
sales = [5, 10, 15, 20, 25, 20, 15, 10, 5, 2, 1]

#Построение гистограммы
plt.figure(figsize=(10, 6))
plt.bar(prices, sales)

plt.xlabel('Price')
plt.ylabel('Number of Sales')
plt.title('Sales distibution by Price')
plt.show()