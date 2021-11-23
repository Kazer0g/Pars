#----------------------------------------------------------------------------------------------------------------------------------------------)
# Подключение библиотек
from selenium import webdriver 
from bs4 import BeautifulSoup
import re

# Драйвер
driver = webdriver.Chrome() # Подключение Хрома

# Классы---------------------------------------------------------------------------------------------------------------------------------------)
class vacancia:

    def __init__ (self, link):

        self.link = link
# Кортежи--------------------------------------------------------------------------------------------------------------------------------------)
vacansii = []
words = []
# Функции--------------------------------------------------------------------------------------------------------------------------------------)
# Функция считывания HTML кода страницы
def get_page_html ():
    global soup
    html_page = driver.page_source # Запись в переменную HTML код 
    soup = BeautifulSoup(html_page, "html.parser") # Передача актуального HTML кода в BS4

    
    print (re.findall(r'<a.*>.*</a>', str(soup)))

    # v = vacansia (link) # Создание объекта вакансии
    # vacansii.appened (v) # Запись вакансии в список
# Функция добавления слова в кортеж
def new_word_up (mb_new_word):
    for word in words:
        if mb_new_word != word:
            new_word = mb_new_word
        else:
            new_word = " "
    if new_word != " ":
        print ("Запись " + new_word)
        words.append(new_word)
# Основа---------------------------------------------------------------------------------------------------------------------------------------)

# Переход на страницу 
print ("Сайт открывается...")
driver.get("https://www.superjob.ru/vakansii/programmist.html") # Переход по ссылке на сайт

# Стандартная ссылка на страницу сайта
page_link = "https://www.superjob.ru/vakansii/programmist.html?page="

# Цикл перехода по стринцам
for i in range (1, 20):

    print ("Переход на страницу " + str(i) + "...")
    next_page_link = page_link + str(i) # Изменение ссылки на  ссылку следующей страницы
    driver.get(next_page_link) # Переход на следующую страницу

    print ("Считывание кода страницы...")
    get_page_html () # Функция считывания HTML кода страницы
