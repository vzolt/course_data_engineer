# -*- coding: utf-8 -*-
#!pip install feedparser
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
    
df_add['day'] = df_add.data.apply(strftime)

df_add['day_of_week'] = df_add.data.apply(tm_wday)

df = pd.read_csv('../data/raw_data.csv', index_col=[0]).reset_index(drop=True)

df_union = pd.concat([df, df_add], axis=0).reset_index(drop=True)

df_union.drop_duplicates(subset=['date'], inplace= True, ignore_index = True, keep = 'last')

df_union.to_csv('../data/raw_data.csv', encoding='utf-8')

display(df_union)


