import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

#time.sleep(1)
price = WebDriverWait(driver, 12).until(                           # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

def calc(x):                                                # считать математическую функцию от x.
  return str(math.log(abs(12*math.sin(int(x)))))

num1 = driver.find_element(By.ID, "input_value").text        # находим нужный элемент на странице и приобразуем в текст


input1 = driver.find_element(By.CSS_SELECTOR, "input")      # вводим данные в поля для ввода
input1.send_keys(calc(num1))

button = driver.find_element(By.ID, "solve")
button.click()

time.sleep(10)
driver.quit()


