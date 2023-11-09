import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
time.sleep(3)
user_name.clear()
time.sleep(3)


password_standard_user = "secret_sauce"
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_standard_user)
time.sleep(3)
password.clear()
time.sleep(3)

driver.close()
