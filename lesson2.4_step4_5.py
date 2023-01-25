import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)                                  # говорим WebDriver искать каждый элемент в течение 5 секунд
driver.get("http://suninjuly.github.io/wait1.html")

#time.sleep(1)
button = driver.find_element(By.ID, "verify")
button.click()
message = driver.find_element(By.ID, "verify_message")

assert "successful" in message.text

time.sleep(3)
driver.quit()


