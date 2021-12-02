#=====================================================================================================================================)
# Подключение библиотек
from selenium import webdriver 
from bs4 import BeautifulSoup
# import re

# Драйвер
driver = webdriver.Chrome() # Подключение Хрома
# Переменные==========================================================================================================================)
data = ""
# Классы==============================================================================================================================)
class vacansia:

    def __init__ (self, link):

        self.link = link
# Кортежи=============================================================================================================================)
vacansii = []
words = []
# Функции=============================================================================================================================)
# Функция записи текста
def cut_inf (long_inf):
    global data
    index_start = long_inf.find("<li>") 
    if index_start != 3:
        index_end = long_inf.find ("<", index_start)
        collect = str(long_inf)[index_start:index_end:]

        data = data + " " + str(collect)

        print (data)

# Функция поиска текста на страницах вакансий
def search_class ():
    long_inf = soup.find(class_= "_2LeqZ _3ceWi _1XzYb Js9sN _3Jn4o WGREZ")
    print ("Запись информации...")
    cut_inf (long_inf)

#-------------------------------------------------------------------------------------)

# Финкция фильтровки строк вакансий
def cut_str (long_str):

    index_start = long_str.find ("/vakansii/") # Начало ссылки с /vacansii/
    if index_start != -1:
        index_end = long_str.find ("\"", index_start) # Конец ссылки "
        fine_str = long_str[index_start:index_end:] # Ссылка из строки с targer = "_blank" и href начинающиеся с /vacansii/

        print ("Ссылка: " + str(fine_str)) 
        v = vacansia (str(fine_str))
        vacansii.append (v)
        cut_str (long_str[index_end-1:])

# Функция поиска строк вакансий
def search_blank ():
    long_str = soup.findAll(target="_blank") # Все тэги с target = "_blank"
    print ("Запись ссылок вакансий...")
    cut_str (str(long_str))


#-------------------------------------------------------------------------------------)
# Функция считывания HTML кода страницы
def get_page_html ():
    global soup
    html_page = driver.page_source # Запись в переменную HTML код 
    soup = BeautifulSoup(html_page, "lxml") # Передача актуального HTML кода в BS4

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
# Основа==============================================================================================================================)

# Переход на страницу 
print ("Сайт открывается...")
driver.get("https://www.superjob.ru/vakansii/programmist.html") # Переход по ссылке на сайт

# Стандартная ссылка на страницу сайта
page_link = "https://www.superjob.ru/vakansii/programmist.html?page="

# Цикл перехода по стринцам
for i in range (1, 2):

    print ("Переход на страницу " + str(i) + "...")
    next_page_link = page_link + str(i) # Изменение ссылки на  ссылку следующей страницы
    driver.get(next_page_link) # Переход на следующую страницу

    print ("Считывание кода страницы...")
    get_page_html () # Функция считывания HTML кода страницы
    search_blank ()

print ("---Все ссылки записаны---")

for j in range (len(vacansii)):
    print ("Переход по ссылке на вакансию: \n" + "https://www.superjob.ru/" + str(vacansii[j].link))
    driver.get(str("https://www.superjob.ru/" + vacansii[j].link))
    get_page_html() # Функция считывания HTML кода страницы
    search_class () 


