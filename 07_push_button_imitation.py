import time
from selenium import webdriver
from selenium.webdriver import Keys
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
password.send_keys(Keys.RETURN) # имитация нажатия Enter
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()

dropdown_list = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
dropdown_list.click()
dropdown_list.send_keys(Keys.ARROW_DOWN) # имитация нажатия стрелки Вниз
dropdown_list.send_keys(Keys.RETURN)

time.sleep(3)
driver.close()
