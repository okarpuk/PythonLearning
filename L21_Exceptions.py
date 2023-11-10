import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/dynamic-properties/'
driver.get(base_url)
driver.maximize_window()

try:
    visible_after = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_after.click()
except NoSuchElementException as exception:
    time.sleep(10)
    visible_after = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_after.click()
    print("[Visible after] button clicked")

time.sleep(5)
driver.close()
