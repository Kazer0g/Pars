#=====================================================================================================================================)
# Подключение библиотек
from selenium import webdriver 
from bs4 import BeautifulSoup
import re

# Драйвер
driver = webdriver.Chrome() # Подключение Хрома
# Переменные==========================================================================================================================)
data = ""
new_word = ""
# Классы==============================================================================================================================)
class vacansia:

    def __init__ (self, link, data):

        self.link = link
        self.data = data
# Кортежи=============================================================================================================================)

vacansii = []
words = []
abb = []
pLib = ["!", "#", "$", "%", "&", "'", "*", "+", ",", ".", "/", ":", ";", "<", "=", ">", "?", "[", "\\", "]",  "^", "_",  "`",  "{", "|", "}", "~", "-", "(", ")", "—"]
counts = []
num = []
di = dict()

# Функции=============================================================================================================================)

# Функция очистки текста
def clean (long_text):
    global cleaned
    for i in pLib:
        long_text = long_text.replace (i, " ")
    cleaned = long_text

#-------------------------------------------------------------------------------------)

# Функция отлова по критериям
def catch (long_text):
    catch_skobka (long_text)

def catch_skobka (long_text):
    index_start = long_text.find ("(")
    if index_start != -1:
        index_end = long_text.find (")")


#-------------------------------------------------------------------------------------)

# Функция записи текста
def cut_inf (long_inf):
    global data
    index_start = long_inf.find("<") 
    index_end = long_inf.find(">")
    if index_start != -1:
        long_inf = long_inf[:index_start:] + long_inf[index_end+1::]
        cut_inf (long_inf)
    else:
        data = long_inf

# Функция поиска текста на страницах вакансий
def search_class ():
    long_inf = soup.find(class_= "_2LeqZ _2ZUiD _3DjcL _1tCB5 _3fXVo _2iyjv")
    print ("Запись информации...")
    cut_inf (str(long_inf))

#-------------------------------------------------------------------------------------)

# Финкция фильтровки строк вакансий
def cut_str (long_str):

    index_start = long_str.find ("/vakansii/") # Начало ссылки с /vacansii/
    if index_start != -1:
        index_end = long_str.find ("\"", index_start) # Конец ссылки "
        fine_str = long_str[index_start:index_end:] # Ссылка из строки с targer = "_blank" и href начинающиеся с /vacansii/

        print ("Ссылка: " + str(fine_str)) 
        v = vacansia (str(fine_str), "")
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
    print ("Считывание кода страницы...")
    html_page = driver.page_source # Запись в переменную HTML код 
    soup = BeautifulSoup(html_page, "lxml") # Передача актуального HTML кода в BS4


#-------------------------------------------------------------------------------------)
# Функция распределения
def distribution (word):
    if len(word) > 0:
        if word[0].isupper() == True:
            if len(word) > 1:
                ABB_chek (word)

# Функция проверки на аббривиатуру
def ABB_chek (word):
    bool = True
    for index in range (len(word)):
        if word[index].isupper() == False:
            bool = False
    if bool == True:
        new_word_up (word, abb)


#-------------------------------------------------------------------------------------)

# Функция расложения текста на слова
def inwords (long_text):
    index = long_text.find(" ")
    if index != -1:
        distribution (long_text[:index:])
        inwords (long_text[index+1::])

# Функция добавления слова в кортеж (возможно ненужная функция)
def new_word_up (mb_new_word, place):
    global new_word
    bool = True
    if re.search (r'[^а-яА-Я]', mb_new_word):
        for word in place:
            if word == mb_new_word:
                bool = False
                counts.append(mb_new_word)

        if bool == True:
            place.append(mb_new_word)
            counts.append(mb_new_word)
# Основа==============================================================================================================================)

# Переход на страницу 
print ("Сайт открывается...")
driver.get("https://www.superjob.ru/vakansii/programmist.html") # Переход по ссылке на сайт

# Стандартная ссылка на страницу сайта
page_link = "https://www.superjob.ru/vakansii/programmist.html?page="

# Цикл перехода по стринцам
for i in range (1, 14):

    print ("Переход на страницу " + str(i) + "...")
    next_page_link = page_link + str(i) # Изменение ссылки на  ссылку следующей страницы
    driver.get(next_page_link) # Переход на следующую страницу

    get_page_html () # Функция считывания HTML кода страницы
    search_blank ()

print ("---Все ссылки записаны---")

#len(vacansii)

for j in range (len(vacansii)):
    print ("Переход по ссылке на вакансию: \n" + "https://www.superjob.ru/" + str(vacansii[j].link))
    driver.get(str("https://www.superjob.ru/" + vacansii[j].link))
    get_page_html() # Функция считывания HTML кода страницы
    search_class () 
    vacansii[j].data = data

for l in range (len(vacansii)):
    print ("Обработка текста вакансии: \n" + "https://www.superjob.ru/" + str(vacansii[l].link))
    print ("Очистка текста...")
    clean (vacansii[l].data)
    vacansii [l].data = cleaned
    print ("Поиск...")
    # catch (vacansii[l].data)
    inwords (vacansii[l].data)

print ("Подсчет повторений...")
with open ("counts.txt", "w") as c:
    for n in abb:
        num.append(counts.count(n))
        di[n] = counts.count(n)
        num = list(set(num))
    num = sorted(num, reverse=True)
    for g in num:
        for p in di:
            if di[p] == g:
                c.write(p + " " + str(g) + "\n")

print ("Запись аббревиатур...")

with open ("abbreviations.txt", "w") as f:
    for p in abb:
        f.write(p + "\n")

print ("Завершение работы.")
print ("Вакансий обработано: " + str(len(vacansii)))
print ("Аббревиатур найденно: " + str(len(abb)))

