from selenium import webdriver 
from bs4 import BeautifulSoup

# Драйвер
driver = webdriver.Chrome() # Подключение Хрома

words = []
errors = []

#-------------------------------------------------------------------------------------)

# Функция считывания HTML кода страницы
def get_page_html ():
    global soup
    print ("Считывание кода страницы...")
    html_page = driver.page_source # Запись в переменную HTML код 
    soup = BeautifulSoup(html_page, "lxml") # Передача актуального HTML кода в BS4

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

def search_class ():
	long_str = soup.find (class_ = "hgKElc")
	cut_inf (str(long_str))

print ("Считывание файла...")

with open ("abbreviations.txt", "r") as f:
	
	while True:

		abb = f.readline ()

		if not abb:
			break

		words.append (abb)

print ("Поиск и запись определений...")

t = open ("Error.txt", "w")
n = open ("None.txt", "w")

with open ("discriptions.txt", "w") as d:
	for i in range (len(words)):
		
		try:
			driver.get ("https://www.google.com/search?q=" + words[i] + " определение")
			get_page_html ()
			search_class ()
			if data == "None":
				n.write(words[i])
			else:
				d.write (words[i] + data + "\n\n")
		except UnicodeEncodeError:
			t.write (words [i])
