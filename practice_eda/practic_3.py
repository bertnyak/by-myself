import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tabulate
import numpy as np

# Price and Value


data = pd.read_csv('data_pr3.csv')
df = pd.DataFrame(data)

def column_values(df):
    row = [df.nunique(), (df == 0).sum(axis=0), df.isna().sum(), round(df.isna().sum() / len(df) * 100, 1), df.dtypes]
    return row


sex = []
for column in df:
    sex.append([column] + column_values(df[column]))

print(
    tabulate.tabulate(sex, headers=['название', 'к-во уник знач', 'к-во 0-ых знач', 'пустые', '% пустых', 'тип данн'],
                      tablefmt='orgtbl'))

statistic = df.describe()
print("Средние значения")
print(statistic)

# Визуализация данных
plt.figure(figsize=(10, 6))
plt.hist(data['Price'], bins=10, edgecolor='black')
plt.xlabel('Продажи')
plt.ylabel('Частота')
plt.title('Распределение продаж')
plt.show()