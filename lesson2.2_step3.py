import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()
driver.get(link)

#Расчёт суммы двух чисел
def calc_sum(a, b):
    return str(int(a)+int(b))

#Найти элемент и записать его как целое число
num1 = driver.find_element(By.ID, "num1")
a = int(num1.text)
num2 = driver.find_element(By.ID, "num2")
b = int(num2.text)
num3 = calc_sum(a, b)

#Открытие выподающего списка и выбор нужного значения
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(num3)

#Нажатие на кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
driver.quit()



