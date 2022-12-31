# -*- coding: utf-8 -*-

import psycopg2
from sqlalchemy import create_engine

# импорт в Postgres
# устанавливаем параметры
db_config = {'user': 'postgres', # имя пользователя
'pwd': 'password', # пароль
'host': 'localhost',
'port': 5432, # порт подключения
'db': 'database'} # название базы данных
connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
 db_config['pwd'],
 db_config['host'],
 db_config['port'],
 db_config['db'])
# сохраняем коннектор
engine = create_engine(connection_string, connect_args={'sslmode':'require'})
db = create_engine(connection_string)
conn = db.connect()

