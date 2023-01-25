import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(link)

#Считать математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#Находим нужный элемент на странице
num1 = driver.find_element(By.ID, "input_value")
x = int(num1.text)
y = calc(x)
#Скрол вниз и ввод значения в поле для ввода
input1 = driver.find_element(By.CSS_SELECTOR, "input")
driver.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)
#Выбор чекбокса
option1 = driver.find_element(By.ID, "robotCheckbox")
option1.click()
#Переключить radiobutton
option2 = driver.find_element(By.ID, "robotsRule")
option2.click()
#Нажатие на кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
driver.quit()



