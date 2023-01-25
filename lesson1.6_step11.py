﻿import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()
driver.get(link)

labels = driver.find_elements(By.CSS_SELECTOR, "required")
inputs = driver.find_elements(By.TAG_NAME, "input")

inputs.send_keys('Обязалово!')

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(10) 
driver.quit()



