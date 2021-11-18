# Пjдключение библиотек
from selenium import webdriver 
from bs4 import BeautifulSoup

# Драйвер
chormedriver = webdriver.Chrome()

# Переход на страницу 
print ("Сайт открывается...")
chormedriver.get("https://www.superjob.ru/vakansii/programmist.html")

