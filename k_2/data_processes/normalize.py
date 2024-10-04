import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Загрузка данных (пример с CSV-файлом)
df = pd.read_csv('data_processes/import_substitution_quarterly_data.csv')

# Выбираем столбцы для нормализации (например, числовые столбцы)
columns_to_normalize = ['column1', 'column2', 'column3']

# Создаем объект MinMaxScaler для нормализации данных
scaler = MinMaxScaler()

# Применяем нормализацию к выбранным столбцам
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# Выводим первые строки нормализованных данных
print(df.head())

# Сохраняем нормализованные данные обратно в файл
df.to_csv('normalized_data.csv', index=False)
