import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.get(link)

button = driver.find_element(By.CSS_SELECTOR, "button.btn") # жмём на кнопку
button.click()

new_window = driver.window_handles[1]                       # находим вторую вкладку
driver.switch_to.window(driver.window_handles[1])           # переходим на вторую вкладку

def calc(x):                                                # считать математическую функцию от x.
  return str(math.log(abs(12*math.sin(int(x)))))

num1 = driver.find_element(By.ID, "input_value").text        # находим нужный элемент на странице и приобразуем в текст


input1 = driver.find_element(By.CSS_SELECTOR, "input")      # вводим данные в поля для ввода
input1.send_keys(calc(num1))

button = driver.find_element(By.CSS_SELECTOR, "button.btn") # жмём на кнопку
button.click()

time.sleep(10)
driver.quit()


