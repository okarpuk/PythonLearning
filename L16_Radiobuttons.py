import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

elements_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")
elements_button.click()
time.sleep(2)

radiobutton_button = driver.find_element(By.XPATH, "//li[@id='item-2']")
radiobutton_button.click()
time.sleep(2)

#  Click on radiobutton
radiobutton = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
radiobutton.click()

time.sleep(2)
driver.close()
