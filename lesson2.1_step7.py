import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()
driver.get(link)

#Считать математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#Находим нужный элемент на странице
images1 = driver.find_element(By.ID, "treasure")
#Определяем значение атрибута
x = images1.get_attribute("valuex")
y = calc(x)

input1 = driver.find_element(By.ID, "answer")
input1.send_keys(y)
option1 = driver.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = driver.find_element(By.CSS_SELECTOR, "[value='robots']")
option2.click()
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)
driver.quit()



