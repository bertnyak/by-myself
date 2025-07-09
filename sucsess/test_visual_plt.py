import pandas as pd 
import matplotlib.pyplot as plt
data = {
    'Месяц' : ['January', 'February', 'March', 'April', 'May'],
    'Продажи' : [10000, 15000, 12000, 18000, 20000]}

df = pd.DataFrame(data)

#График продаж по месяцам
plt.plot(df['Месяц'], df['Продажи'])
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.title('Динамика продаж')
plt.show()

plt.pie(df['Продажи'], labels=df['Месяц'], autopct='%1.1f%%')
plt.title('Доля продаж по месяцам')
plt.show()