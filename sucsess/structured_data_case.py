import pandas as pd 
# Создание DataFrame с помощью библотеки pandas(Таблица)
data = {'Имя' : ['Анна', 'Петр', 'Григорий'],
        'Возраст' : [25, 30, 35],
        'Город' : ['Москва', 'Питер', 'Тагил']}

df = pd.DataFrame(data)
print(df)
# Использование функций из библиотеки pandas
mean_age = df['Возраст'].mean()
print('Средний возраст:', int(mean_age))
