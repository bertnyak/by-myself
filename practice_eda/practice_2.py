import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Вам предоставлен набор данных о зарплатах сотрудников в компании.
# Ваша цель — визуально оценить центральное положение данных, определить среднюю и медианную зарплату в компании.
data = pd.read_csv('salary_data.csv')
df = pd.DataFrame(data)
# a = data.describe()
# Рассчитаем среднюю и медиану зарплаты
mean_salary = data['salary'].mean()
median_salary = data['salary'].median()

plt.figure(figsize=(8, 6))
plt.hist(data['salary'], bins= 10, edgecolor='black')
plt.xlabel('Зарплата')
plt.ylabel('Частота')
plt.title('Распределение зарплаты')
plt.show()

print("Средняя зарплата", mean_salary)
print("Медиана зарплаты", median_salary)