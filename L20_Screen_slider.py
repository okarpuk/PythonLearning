import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://5element.by/catalog/377-smartfony/brest/'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
my_slider = driver.find_element(By.XPATH, "//div[@aria-label='lower']")
action.click_and_hold(my_slider).move_by_offset(100, 0).release().perform()

time.sleep(5)
driver.close()
