import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")
time.sleep(3)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login = driver.find_element(By.XPATH, "//*[@id='login-button']").click()
button_login.click()
time.sleep(3)

driver.close()




