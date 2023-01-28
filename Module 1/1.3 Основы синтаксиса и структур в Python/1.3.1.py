# спарсить данные о вакансиях python разработчиков с сайта hh.ru, введя в поиск “python разработчик”

import requests  # импорт библиотеки для запросов к серверу
import json

# функция для получения url
def urls(todos):
    todos_urls = []
    n = len(todos['items'])
    for i in range(0, n):
        todos_urls.append(todos['items'][i]['url'])
    return todos_urls


# запрос к api
url = 'https://api.hh.ru/vacancies?text="python разработчик"&per_page=100&page=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
req = requests.get(url, headers=headers)

todos = json.loads(req.text)
number_pages = todos['pages']
all_urls = urls(todos)

# url-адреса всех страниц
for i in range(1, number_pages):
    url = 'https://api.hh.ru/vacancies?text="python разработчик"&per_page=100&page=' + \
        str(i)
    req = requests.get(url, headers=headers)
    todos = json.loads(req.text)
    all_urls.extend(urls(todos))

# парсим каждую страницу
data = {}
for i in range(0, len(all_urls)):
    req = requests.get(all_urls[i], headers=headers)
    todos = json.loads(req.text)
    data[i] = {'title': todos['name'], 'work experience': todos['experience']['name'],
               'salary': todos['salary'], 'region': todos['area']['name']}

# вывод
print(json.dumps(data, ensure_ascii=False))
