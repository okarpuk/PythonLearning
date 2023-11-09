import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker/'
driver.get(base_url)
driver.maximize_window()

date_field = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
#date_field.clear() # Оптимально использовать этот  метод. Но если он не работает, используем костыли

for i in range(len(date_field.get_attribute(name="value"))): # с помощью цилка получаем длину текста в поле
    date_field.send_keys(Keys.BACKSPACE)                     # и вводим BACKSPACE по количеству символов

# date_field.send_keys(Keys.BACKSPACE * 10) # либо просто вводим BACKSPACE по количеству символов
time.sleep(2)

date_field.send_keys("10/10/2023")
time.sleep(2)
date_field.send_keys(Keys.RETURN)

driver.refresh() # refresh page







time.sleep(2)
driver.close()
