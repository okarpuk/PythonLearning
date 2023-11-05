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
time.sleep(2)

driver.execute_script("window.scrollTo(0, 300)")

current_date_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
screenshot_name = 'screenshot' + current_date_time + '.png'
driver.save_screenshot('D:\PycharmProjects\AutomationLearning\Screenshots\\' + screenshot_name)

driver.close()
