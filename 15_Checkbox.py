import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
elements = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")
elements.click()
time.sleep(2)

checkbox_button = driver.find_element(By.XPATH, "//li[@id='item-1']")
checkbox_button.click()
time.sleep(2)



# elements.send_keys(login_standard_user)





time.sleep(2)

driver.close()
