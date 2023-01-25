import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
driver.get(link)

input1 = driver.find_element(By.NAME, "firstname")         # вводим данные в поля для ввода
input1.send_keys("Ivan") 
input2 = driver.find_element(By.NAME, "lastname")
input2.send_keys("Petrov") 
input3 = driver.find_element(By.NAME, "email")
input3.send_keys("test@test.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

input4 = driver.find_element(By.ID, "file")                 # прикрепляем файл
input4.send_keys(file_path)

button = driver.find_element(By.CSS_SELECTOR, "button.btn") # жмём на кнопку
button.click()

time.sleep(10)
driver.quit()


