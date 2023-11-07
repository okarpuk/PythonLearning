import datetime
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

password_standard_user = "secret_sauce"
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_standard_user)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu_button.click()
time.sleep(2)

about_menu_button = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
about_menu_button.click()
time.sleep(5)

driver.back() # ВОЗВРАТ НАЗАД
time.sleep(5)

driver.forward() # ПЕРЕМЕЩЕНИЕ ВПЕРЕД
time.sleep(5)


driver.close()
