import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/huge_form.html")
elements = driver.find_elements(By.CSS_SELECTOR, "[type='text']")
for element in elements:
    element.send_keys("Жопа")
    
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30) 
driver.quit()


