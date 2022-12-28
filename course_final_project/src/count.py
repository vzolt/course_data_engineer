# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('../data/transform_data.csv', sep=',', index_col=[0]).reset_index(drop=True)

display(df)

# Суррогатный ключ категории
display(df.key_category)

# Название категории
display(df.name_category)

# Общее количество новостей из всех источников по данной категории за все время
display(df.name_category.value_counts().reset_index())

# Общее количество новостей из всех источников по данной категории за последние сутки
day_last = df.day.max()
df.query('day == @day_last').groupby('key_category').agg({'name_category': 'count'}).reset_index()

# Количество новостей данной категории для каждого из источников за последние сутки
df.query('day == @day_last').groupby(['source','key_category']).agg({'name_category': 'count'}).reset_index()

# Среднее количество публикаций по данной категории в сутки
day_key_category = df.groupby(['day','key_category']).agg({'name_category': 'count'}).reset_index()
day_key_category.columns = ['day', 'category', 'count']
day_key_category.groupby('category').agg({'count': 'mean'}).reset_index()

# День, в который было сделано максимальное количество публикаций по данной категории
day_key_category.sort_values(by=['category', 'count'])

# Количество публикаций новостей данной категории по дням недели
df.groupby(['day_of_week', 'key_category']).agg({'name_category': 'count'}).reset_index()
