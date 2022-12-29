# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# загрузка файла
df = pd.read_csv('../data/transform_data.csv', sep=',', index_col=[0]).reset_index(drop=True)

# Расчеты.
# Суррогатный ключ категории
task1 = pd.DataFrame(df.key_category.unique())
task1.columns = ['key_category']

# Название категории
task2 = pd.DataFrame(df.name_category.unique())
task2.columns = ['name_category']

# Общее количество новостей из всех источников по данной категории за все время
task3 = df.name_category.value_counts().reset_index()
task3.columns = ['name_category', 'count']

# Количество новостей данной категории для каждого из источников за все время
task4 = df.groupby(['source', 'key_category']).agg({'name_category': 'count'}).sort_values(by=['source', 'key_category']).reset_index()
task4.columns = ['source', 'key_category', 'count']

# Общее количество новостей из всех источников по данной категории за последние сутки
day_last = df.day.max()
task5 = df.query('day == @day_last').groupby('key_category').agg({'name_category': 'count'}).sort_values(by='name_category', ascending = False).reset_index()

# Количество новостей данной категории для каждого из источников за последние сутки
task6 = df.query('day == @day_last').groupby(['source','key_category']).agg({'name_category': 'count'}).sort_values(by=['source', 'key_category']).reset_index()
task6.columns = ['source', 'key_category', 'count_day']

# Среднее количество публикаций по данной категории в сутки
day_key_category = df.groupby(['day','key_category']).agg({'name_category': 'count'}).reset_index()
day_key_category.columns = ['day', 'category', 'count']
task7 = day_key_category.groupby('category').agg({'count': 'mean'}).reset_index()
task7['count'] = round(task7['count']).astype('int')
task7.columns = ['key_category', 'avg']

# День, в который было сделано максимальное количество публикаций по данной категории
task8 = day_key_category.sort_values(by=['category', 'count'])
task = task8.groupby(['category']).agg({'count': 'max', 'day': 'first'}).reset_index()
task.columns = [['key_category', 'count', 'max']]
task8 = task[['key_category', 'max']]

# Количество публикаций новостей данной категории по дням недели
task9 = df.groupby(['day_of_week', 'key_category']).agg({'name_category': 'count'}).reset_index()
task9.columns = ['day_of_week', 'key_category', 'count']

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
    
    
    