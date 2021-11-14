from selenium import webdriver 

def main(): 
    driver = webdriver.Chrome()# Подлкючение браузера
    driver.get("https://ru.wikipedia.org/wiki/Selenium")# Ссылка на нужный сайт
    title = driver.find_element_by_tag_name("h1")# Поиск элемента
    print (title.text)

if __name__ == "__main__":
    main()