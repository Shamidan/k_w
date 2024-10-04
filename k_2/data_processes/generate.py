import numpy as np
import pandas as pd
import random

# Категории строительных ресурсов и их представители
resources = {
    'Металлы': ['Сталь', 'Медь', 'Чугун', 'Алюминий'],
    'Природные каменные материалы': ['Гранит', 'Мрамор', 'Щебень', 'Базальт'],
    'Древесные материалы и изделия': ['Доска обрезная', 'Фанера', 'ОСП', 'МДФ'],
    'Гидроизоляционные материалы': ['Рубероид', 'Полиэтиленовая пленка', 'Битумная мастика',
                                    'Гидроизоляционные мембраны'],
    'Полимерные материалы': ['Пластиковые трубы', 'Пенопласт', 'ПВХ панели', 'Полиуретановая пена'],
    'Стекло': ['Оконное стекло', 'Закаленное стекло', 'Ламинированное стекло', 'Стеклопакеты'],
    'Отделочные материалы': ['Керамическая плитка', 'Ламинат', 'Штукатурка', 'Гипсокартон'],
    'Строительные растворы': ['Бетон', 'Цементный раствор', 'Штукатурный раствор', 'Кладочные смеси'],
    'Керамические материалы и изделия из глины': ['Кирпич красный', 'Кирпич огнеупорный', 'Черепица керамическая',
                                                  'Тротуарная плитка'],
    'Машин-механизмы': ['Экскаватор', 'Бетономешалка', 'Строительный кран', 'Гидромолот']
}


# Функция для генерации данных поквартально
def generate_data(resource, representative, start_import, start_year, end_year, annual_decrease):
    data = []
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    quarter_decrease = annual_decrease / 4  # Уменьшение импортозависимости поквартально

    for year in range(start_year, end_year + 1):
        for quarter in quarters:
            local_prod = 100 - start_import  # Начальный уровень отечественного производства
            import_dep = start_import - quarter_decrease * ((year - start_year) * 4 + quarters.index(quarter))
            local_prod = 100 - import_dep
            data.append([resource, representative, f'{year}-{quarter}', local_prod, import_dep])
    return data


# Генерация данных для каждого представителя каждой категории
data = []
start_year = 2015
end_year = 2023

for resource, representatives in resources.items():
    for representative in representatives:
        start_import = random.randint(50, 90)  # Случайная начальная импортозависимость
        annual_decrease = random.uniform(3, 8)  # Случайный темп импортозамещения в год
        data.extend(generate_data(resource, representative, start_import, start_year, end_year, annual_decrease))

# Преобразуем в DataFrame
df = pd.DataFrame(data,
                  columns=['Category', 'Representative', 'Period', 'Local_Production (%)', 'Import_Dependence (%)'])

# Вывод первых строк
print(df.head())

# Сохранение в CSV файл для анализа
df.to_csv('import_substitution_quarterly_data.csv', index=False)
