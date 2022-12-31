# -*- coding: utf-8 -*-

import feedparser
import pandas as pd
import time

# функции для извлечения латы и дня недели
def strftime(date):
    return time.strftime('%d.%m.%Y', date)

def tm_wday(date):
    return date.tm_wday

# получаем последние данные из новостынх лент
newsfeed_lenta = feedparser.parse("https://lenta.ru/rss/")
newsfeed_tass = feedparser.parse("https://tass.ru/rss/v2.xml")
newsfeed_vedomosti = feedparser.parse("https://www.vedomosti.ru/rss/news")
res = [*newsfeed_lenta.entries, *newsfeed_tass.entries, *newsfeed_vedomosti.entries]

# формируем датафрейм
categories, dates, sources = [], [], []

for i in range(0, len(res)): 
    try:
       category = res[i].tags[0]['term']
    except:
       category = 'unknown'
    categories.append(category)
    dates.append(res[i].published_parsed)
    sources.append(res[i].title_detail.base)
    
df_add = pd.DataFrame({'category': categories, 'date': dates, 'source': sources}).reset_index(drop=True)
    
df_add['day'] = df_add.date.apply(strftime)

df_add['day_of_week'] = df_add.date.apply(tm_wday)

df_add.date = df_add.date.astype('string')

# выгружаем данные из raw_data.csv
df = pd.read_csv('../data/raw_data.csv', index_col=[0]).reset_index(drop=True)

# объединяем данные и удаляем дубликаты
df_union = pd.concat([df, df_add], axis=0).reset_index(drop=True)

df_union.drop_duplicates(subset=['date', 'source'], inplace= True, ignore_index = True, keep = 'last')

# загружаем в файл
df_union.to_csv('../data/raw_data.csv', encoding='utf-8')

# импорт в Postgres
exec(open("postgres_intro.py").read())
df_union.to_sql('raw_data', con=conn, if_exists='replace',
		index=False)
conn = psycopg2.connect(connection_string						)
conn.autocommit = True
cursor = conn.cursor()
conn.close()
