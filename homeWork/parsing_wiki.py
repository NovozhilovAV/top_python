# 2. Выбрать любую страничку в Википедии и сохранить в файл все ссылки с этой страницы построчно.

import requests
from bs4 import BeautifulSoup
# import useragent
import json


url = 'https://ru.m.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%BA%D1%81%D0%B8-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80'

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.status_code)
wiki_html = response.text
# print(html)
# получили код страницы и из него теперь необходимо получить все ссылки

# with open('wiki.html', 'w', encoding='utf-8') as file:
#         file.write(wiki_html)
# сохраним код страницы в фаил.  обязательно encoding='utf-8'!!! - иначе не работает

# Чтобы не "долбить" страницу запросами откроем фаил и будем работать с ним
# with open('wiki.html', encoding='utf-8') as file:
#         src = file.read()

# Создаем объект класса BeautifulSoup. 1-й аргумент - код html-страницы, 2-й аргумент - парсер для html ('html.parser')
soup = BeautifulSoup(wiki_html, 'html.parser')
# soup = BeautifulSoup(src, 'html.parser')    # если будем работать с файлом а не с сайтом
# получаем все теги <a> содержащие ссылки href
all_a = soup.find_all('a')
# print(all_a)
# переберем все полученные ссылки и выведем их в каждой строке
# for hr in all_a:
#         hr_text = hr.text
#         # hr_url = hr.get('href')    # выведет все ссылки содержащиеся в href
#         hr_url = 'https://ru.m.wikipedia.org' +  hr.get('href')    # добавили доменное имя - так отображается корректнее
#         # hr_url = hr['href']    # так тоже можно указать
#         # print(hr_text)
#         print(f'{hr.text}: {hr_url}')

# заносим данные в словарь
all_link = {}
for hr in all_a:
        hr_text = hr.text.strip('\n')
        hr_url = 'https://ru.m.wikipedia.org' +  hr.get('href')    # добавили доменное имя - так отображается корректнее
        all_link[hr_text] = hr_url
        print(all_link)

# # сохраним словарь в фаил в формате json, обязательно encoding='utf-8'!!! - иначе не работает
with open('all_link.json', 'w', encoding='utf-8') as file:
        json.dump(all_link, file, indent=4, ensure_ascii=False)


