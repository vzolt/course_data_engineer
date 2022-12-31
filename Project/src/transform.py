# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# загрузка файла
df = pd.read_csv('../data/raw_data.csv', sep=',', index_col=[0]).reset_index(drop=True)

# функция для систематизации категория
def is_key(value):
    """
    Возвращает ключ категории
    """
    if value == 'Россия' or value == 'Среда обитания' or value == '69-я параллель' or value == 'Моя страна':
        key_category = 'russia'
    elif  value == 'Бывший СССР' or value == 'Путешествия' or value == 'Мир' or value == 'Международная панорама' or value == 'Политика':
        key_category = 'world'
    elif value == 'Экономика' or value == 'Бизнес' or value == 'Недвижимость' or value == 'Экономика и бизнес' or value == 'Финансы':
        key_category = 'business'
    elif value == 'Авто' or value == 'Технологии':
        key_category = 'technology'
    elif value == 'Ценности' or value == 'Интернет и СМИ' or value == 'Общество' or value == 'Происшествия' or value == 'Силовые структуры':
        key_category = 'society'
    elif value == 'Из жизни' or value == 'Культура' in value:
        key_category = 'entertainment'
    elif value == 'Спорт':
        key_category = 'sport'
    elif value == 'Наука и техника' or value == 'Космос':
        key_category = 'science' 
    elif value == 'Забота о себе':
        key_category = 'health'    
    else:
        key_category = 'unknown'       
    return key_category
    
    
df['key_category'] = df['category'].apply(is_key)

# присвоим имена категориям
key_name = {'russia' : 'Россия', 'world': 'Мир', 'business': 'Экономика и бизнес',
            'technology' : 'Технологии',  'society' : 'Общество', 'entertainment': 'Культура',
            'sport' : 'Спорт', 'science' : 'Наука и техника', 'health' : 'Здоровье', 'unknown': 'Неизвестно'}

df_key_names = pd.DataFrame.from_dict(key_name, orient='index').reset_index()
df_key_names.columns = ['key_category', 'name_category']
df = df.merge(df_key_names, on = 'key_category')

# формируем готовый датаврейм
df_transform = df[['key_category', 'name_category', 'source', 'day', 'day_of_week']]

# выгрузка в файл
df.to_csv('../data/transform_data.csv', encoding='utf-8')

# импорт в Postgres
exec(open("postgres_intro.py").read())

df.to_sql('transform_data', con=conn, if_exists='replace',
		index=False)

conn = psycopg2.connect(connection_string						)
conn.autocommit = True
cursor = conn.cursor()
conn.close()