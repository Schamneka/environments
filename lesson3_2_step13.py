import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
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

return welcome_text


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = check_page(link)
        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = check_page(link)
        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

if __name__ == "__main__":
    unittest.main()