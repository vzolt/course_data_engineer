# -*- coding: utf-8 -*-
from tabulate import tabulate
# установка и загрузка бибиотек
# !pip install feedparser
import feedparser
import pandas as pd
import time

# функции для извлечения латы и дня недели
def strftime(date):
    return time.strftime('%d.%m.%Y', date)

def tm_wday(date):
    return date.tm_wday

# получаем данные из новостынх лент
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
    
df = pd.DataFrame({'category': categories, 'date': dates, 'source': sources}).reset_index(drop=True)

df['day'] = df.date.apply(strftime)

df['day_of_week'] = df.date.apply(tm_wday)

print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

# выгружаем в файл
df.to_csv('../data/raw_data.csv', encoding='utf-8')

# импорт в Postgres
exec(open("postgres_intro.py").read())

df.to_sql('raw_data', con=conn, if_exists='replace',
		index=False)

conn = psycopg2.connect(connection_string						)
conn.autocommit = True
cursor = conn.cursor()
conn.close()
