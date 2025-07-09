import pandas as pd 
import matplotlib.pyplot as plt 
data = {
    'Имя' : ['Анна', 'Петр', 'Мария'],
    'Возраст' : [25, 30, 35],
    'Средний чек' : [4500, 3200, 7200]}

df = pd.DataFrame(data)
plt.plot(df['Имя'], df['Возраст'])
plt.xlabel('Имя') # Ось X
plt.ylabel('Возраст') # Ось Y
plt.title('Распределение возраста покупателя') # Оглавление таблицы
plt.grid(True) #Сетка на графике 
plt.show()

plt.bar(df['Имя'], df['Средний чек'])
plt.xlabel('Имя')
plt.ylabel('Средний чек')
plt.title('Сравнение среднего чека покупателей')
plt.show()

colors = ['blue', 'green', 'red']
plt.bar(df['Имя'], df['Средний чек'])
plt.xlabel('Имя')
plt.ylabel('Средний чек')
plt.title('Средний чек покупателей')
plt.show()