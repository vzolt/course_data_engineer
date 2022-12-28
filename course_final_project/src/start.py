# -*- coding: utf-8 -*-
!pip install feedparser
import feedparser
import pandas as pd
import time

def strftime(date):
    return time.strftime('%d.%m.%Y', date)

def tm_wday(date):
    return date.tm_wday

newsfeed_lenta = feedparser.parse("https://lenta.ru/rss/")
newsfeed_tass = feedparser.parse("https://tass.ru/rss/v2.xml")
newsfeed_vedomosti = feedparser.parse("https://www.vedomosti.ru/rss/news")

res = [*newsfeed_lenta.entries, *newsfeed_tass.entries, *newsfeed_vedomosti.entries]
print(len(newsfeed_lenta.entries))
print(len(newsfeed_tass.entries))
print(len(newsfeed_vedomosti.entries))

print(len(res))

categories, dates, sources = [], [], []

for i in range(0, len(res)): 
    try:
       category = res[i].tags[0]['term']
    except:
       category = 'unknown'
    categories.append(category)
    dates.append(res[i].published_parsed)
    sources.append(res[i].title_detail.base)
    
df = pd.DataFrame({'category': categories, 'data': dates, 'source': sources}).reset_index(drop=True)

df['day'] = df.data.apply(strftime)

df['day_of_week'] = df.data.apply(tm_wday)

df.to_csv('../data/raw_data.csv', encoding='utf-8')