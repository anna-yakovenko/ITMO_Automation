# 1.	Создайте функцию которая
# a.	переходит на страницу https://www.saucedemo.com/
# b.	находит элементы:
# i.	текстовое поле username
# ii.	текстовое поле password
# iii.	кнопку submit
# c.	Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.saucedemo.com/")

# поиск элемента
text = driver.find_element(By.CSS_SELECTOR, 'username')
if text is None:
    print('Элемент не найден')
else:
    print('Элемент найден')