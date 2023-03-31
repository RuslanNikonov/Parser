from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://www.omgtu.ru/l/?SHOWALL_1=1' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', class_='news__item') # находим  контейнер с нужным классом
    description = []
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('h3', class_='news-card__title'): # находим тег <p>
            description.append(" ".join(data.text.split()) )# записываем в переменную содержание тега
    print(description)
    with open("news_OmGTU.txt", "w") as f:
        for el in description:
            f.write(str(el))
            f.write('\n')