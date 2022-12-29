# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# загрузка файла
df = pd.read_csv('../data/transform_data.csv', sep=',', index_col=[0]).reset_index(drop=True)

# Суррогатный ключ категории
task1 = df.key_category

# Название категории
task2 = df.name_category

# Общее количество новостей из всех источников по данной категории за все время
task3 = df.name_category.value_counts().reset_index()

# Количество новостей данной категории для каждого из источников за все время
task4 = df.groupby(['source', 'key_category']).agg({'name_category': 'count'}).reset_index()

# Общее количество новостей из всех источников по данной категории за последние сутки
day_last = df.day.max()
task5 = df.query('day == @day_last').groupby('key_category').agg({'name_category': 'count'}).reset_index()

# Количество новостей данной категории для каждого из источников за последние сутки
task6 = df.query('day == @day_last').groupby(['source','key_category']).agg({'name_category': 'count'}).reset_index()

# Среднее количество публикаций по данной категории в сутки
day_key_category = df.groupby(['day','key_category']).agg({'name_category': 'count'}).reset_index()
day_key_category.columns = ['day', 'category', 'count']
task7 = day_key_category.groupby('category').agg({'count': 'mean'}).reset_index()

# День, в который было сделано максимальное количество публикаций по данной категории
task8 = day_key_category.sort_values(by=['category', 'count'])

# Количество публикаций новостей данной категории по дням недели
task9 = df.groupby(['day_of_week', 'key_category']).agg({'name_category': 'count'}).reset_index()

# выгрузка в файл Excel
with pd.ExcelWriter('../data/data.xlsx') as writer:  
    task1.to_excel(writer, sheet_name='key_category')
    task2.to_excel(writer, sheet_name='name_category')
    task3.to_excel(writer, sheet_name='key_category-count')
    task4.to_excel(writer, sheet_name='source-category_count')
    task5.to_excel(writer, sheet_name='key_category-count_day')
    task6.to_excel(writer, sheet_name='source-key_category-count_day')
    task7.to_excel(writer, sheet_name='key_category-avg')
    task8.to_excel(writer, sheet_name='key_category-max')
    task9.to_excel(writer, sheet_name='key_category-count-week_day')
    
    
    