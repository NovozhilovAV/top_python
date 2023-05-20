# Первая часть ДЗ на каникулы)
# 1. Спарсить с сайта https://spys.one инфу о прокси-серверах(табличку со скрина)
# сохранить ее в файл, где каждая строчка соответствует строке из таблицы в формате json.

# 2. Выбрать любую страничку в Википедии и сохранить в файл все ссылки с этой страницы построчно.
# Первая строка - ссылка на саму страницу,
# все последующие - ссылки на этой странице

# 3. Первую программу-парсер сделать в стиле ООП с классами,
# реализующими методы получения объекта BeautifulSoup
# и самой инфы о прокси)

# Все это залить на свой гитхаб. Мне прислать ссылки на pull request

import requests
from bs4 import BeautifulSoup
import json

class Request_html:
    def __init__(self, url):
        self.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        self.url = url

    def request_html(self):
        return requests.get(self.url, headers=self.headers).text

class Soup(Request_html):
    def soup(self):
        return BeautifulSoup(self.request_html(), 'html.parser')

class TableOnlineProxy(Soup):
    def table_proxy(self):
        return self.soup().findAll('td', colspan='1')

class Row1(TableOnlineProxy):
    def row_1(self):
        # row_1 = []
        # for row in table_online_proxy1:
        #     row_1.append(row.text)
        # return row_1
        return [row.text for row in self.table_proxy()][6:-2]

class Row2(Row1):
    def row_2(self):
        row_2 = list(zip(self.row_1()[::6], self.row_1()[1::6], self.row_1()[2::6], self.row_1()[3::6], self.row_1()[4::6],
                     self.row_1()[5::6]))
        for validated_rows in row_2:
            print(json.dumps(validated_rows, ensure_ascii=False))

        return row_2


# Row2('https://spys.one/').row_2()
# записываем данные в фаил
with open(file='proxy.txt', mode='w', encoding='utf-8') as file:
        for validated_rows in Row2('https://spys.one/').row_2():
                file.write(str(validated_rows) + '\n')


# headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
# url = 'https://spys.one/'
# response = requests.get(url, headers=headers)
# html = response.text
# получили код страницы
# Создаем объект класса BeautifulSoup. 1-й аргумент - код html-страницы, 2-й аргумент - парсер для html ('html.parser')
# soup = BeautifulSoup(html, 'html.parser')
# получаем все динамические данные таблицы - font
# table_online_proxy = soup.find_all('font')
# table_online_proxy1 = soup.findAll('td', colspan='1')
# print(table_online_proxy?)   # поставить корректный ввод
# или вот таким образом
# table_online_proxy1 = soup.findAll('td', colspan='1')
# print(table_online_proxy1)
# row_1 = []
# for row in table_online_proxy1:
#         row_1.append(row.text)
# print(row_1)
# row_1_2 = row_1[6:-2]
# row_2 = list(zip(row_1_2[::6],row_1_2[1::6],row_1_2[2::6],row_1_2[3::6],row_1_2[4::6],row_1_2[5::6]))
# вывод на экран
# for validated_rows in row_2:
#         print(json.dumps(validated_rows, ensure_ascii=False))
# # записываем данные в фаил
# with open(file='proxy.txt', mode='w', encoding='utf-8') as file:
#         for validated_rows in row_2:
#                 file.write(f'{json.dumps(validated_rows,ensure_ascii=False)}\n')


# вывод
# ["89.249.246.130:8080", "HTTPS !", "NOA", "Россия ", "21% (43) -", "04:05:23 14:45:37"]
# ["178.32.196.197:11211", "HTTP", "ANM", "Франция ", "24% (8) -", "04:05:23 14:45:19"]
# ["152.231.17.229:999", "HTTP !", "NOA", "Аргентина ", "12% (11) -", "04:05:23 14:43:11"]
# .....

