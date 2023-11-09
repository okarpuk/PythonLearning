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
time.sleep(3)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

url_inventory_page = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert get_url == url_inventory_page

print("Test passed")

time.sleep(3)
driver.close()


