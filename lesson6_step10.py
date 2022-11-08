import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
driver = webdriver.Chrome()
driver.get(link)

input1 = driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
input1.send_keys("Ivan") 
input2 = driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
input2.send_keys("Petrov") 
input3 = driver.find_element(By.XPATH, "//input[@placeholder='Input your email']")
input3.send_keys("Smolensk") 

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(10) 
driver.quit()



