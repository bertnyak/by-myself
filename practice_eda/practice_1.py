import pandas as pd

data_1 = pd.read_csv('data1.csv')
data_2 = pd.read_csv('data2.csv')
data_3 = pd.read_csv('data3.csv')

taxonomy = {
    'data_1' : data_1.dtypes,
    'data_2' : data_2.dtypes,
    'data_3' : data_3.dtypes
}

for dataset, dtypes in taxonomy.items():
    print("Таксономия данных", dataset)
    print(dtypes)
    print()