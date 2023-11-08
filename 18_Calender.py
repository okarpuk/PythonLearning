import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker/'
driver.get(base_url)
driver.maximize_window()






datepicker_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")
datepicker_button.click()
time.sleep(2)








time.sleep(2)
driver.close()
