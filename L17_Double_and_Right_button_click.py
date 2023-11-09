import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

elements_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")
elements_button.click()
time.sleep(2)

buttons_button = driver.find_element(By.XPATH, "//li[@id='item-4']")
buttons_button.click()
time.sleep(2)

#  Create object of ActionChains class
action = ActionChains(driver)

# Double click
doubleclick_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(doubleclick_button).perform()

# Right button click
rightlick_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(rightlick_button).perform()

time.sleep(2)
driver.close()
