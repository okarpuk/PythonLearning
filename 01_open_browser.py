import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(3)
driver.close()

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(3)
driver.close()