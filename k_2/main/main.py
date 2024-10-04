import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Загрузка сгенерированных данных
df = pd.read_csv(r'C:\Users\Шамед\py\Kursach\iad_sistem_my\data_processes\import_substitution_quarterly_data.csv')

# Преобразуем кварталы в числовое значение (Q1 = 1, Q2 = 2, и так далее)
df['Quarter'] = df['Period'].apply(lambda x: (int(x.split('-')[0]) - 2015) * 4 + int(x.split('-')[1][1]))

# Выбираем данные для модели
X = df[['Quarter']]  # Время в кварталах (независимая переменная)
y = df['Import_Dependence (%)']  # Процент импортозависимости (зависимая переменная)

# Разделение данных на обучающую и тестовую выборки (80% - обучение, 20% - тестирование)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на тестовой выборке
y_pred = model.predict(X_test)

# Оценка модели (среднеквадратичная ошибка)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Quarter (from 2015-Q1)')
plt.ylabel('Import Dependence (%)')
plt.title('Linear Regression of Import Dependence Over Time')
plt.legend()
plt.show()

# Коэффициенты модели (угол наклона и пересечение с осью Y)
print(f'Intercept: {model.intercept_}')
print(f'Coefficient: {model.coef_[0]}')
