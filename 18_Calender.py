import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker/'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)

date_field = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
#date_field.clear() # Should be this Method, but it doesn't work. So, we create "kostyl"- using BACKSPACE * 10
date_field.send_keys(Keys.BACKSPACE) #1
date_field.send_keys(Keys.BACKSPACE) #2
date_field.send_keys(Keys.BACKSPACE) #3
date_field.send_keys(Keys.BACKSPACE) #4
date_field.send_keys(Keys.BACKSPACE) #5
date_field.send_keys(Keys.BACKSPACE) #6
date_field.send_keys(Keys.BACKSPACE) #7
date_field.send_keys(Keys.BACKSPACE) #8
date_field.send_keys(Keys.BACKSPACE) #9
date_field.send_keys(Keys.BACKSPACE) #10
time.sleep(2)

date_field.send_keys("10/10/2023")
time.sleep(2)
date_field.send_keys(Keys.RETURN)



time.sleep(2)
driver.close()
