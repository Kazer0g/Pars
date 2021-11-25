#----------------------------------------------------------------------------------------------------------------------------------------------)
# Подключение библиотек
from selenium import webdriver 
from bs4 import BeautifulSoup
# import re

# Драйвер
driver = webdriver.Chrome() # Подключение Хрома

# Классы---------------------------------------------------------------------------------------------------------------------------------------)
class vacansia:

    def __init__ (self, link):

        self.link = link
# Кортежи--------------------------------------------------------------------------------------------------------------------------------------)
vacansii = []
words = []
# Функции--------------------------------------------------------------------------------------------------------------------------------------)
# Финкция фильтровки строк вакансий
def cut_str (long_str):
    index_start = long_str.find ("/vakansii/")
    index_end = long_str.find ("\"", index_start)
    fine_str = long_str[index_start:index_end:] # Ссылка из строки с targer = "_blank" и href начинающиеся с /vacansii/
    print (fine_str)
    v = vacansia (str(fine_str))
    vacansii.append (v)
    print (str(vacansii[0].link))
# Функция считывания HTML кода страницы
def get_page_html ():
    global soup
    html_page = driver.page_source # Запись в переменную HTML код 
    soup = BeautifulSoup(html_page, "lxml") # Передача актуального HTML кода в BS4
    long_str = soup.find_all(target="_blank") # Все тэги с target = "_blank"
    cut_str (str(long_str))

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
