import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker/'
driver.get(base_url)
driver.maximize_window()

date_field = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# date_field.clear() # Оптимально использовать этот  метод. Но если он не работает, используем костыли
# КОСТЫЛЬ 1
for i in range(len(date_field.get_attribute(name="value"))):  # с помощью цилка получаем длину текста в поле
    date_field.send_keys(Keys.BACKSPACE)                      # и вводим BACKSPACE по количеству символов

# КОСТЫЛЬ 2
# date_field.send_keys(Keys.BACKSPACE * 10) # либо просто вводим BACKSPACE по количеству символов

time.sleep(2)
date_field.send_keys("10/10/2023")
time.sleep(2)
date_field.send_keys(Keys.RETURN)
time.sleep(2)

# Автоматическая генерация даты
date_field.click()
date_field.send_keys(Keys.BACKSPACE * 10)  # КОСТЫЛЬ!!!!!!!!!
todays_day = datetime.datetime.utcnow().strftime("%d")
todays_month = datetime.datetime.utcnow().strftime("%m")
todays_year = datetime.datetime.utcnow().strftime("%Y")

test_day = int(todays_day) + 7
test_month = int(todays_month) - 2
test_year = int(todays_year) - 2

date_field.send_keys(f"{test_month}/{test_day}/{test_year}")
date_field.send_keys(Keys.RETURN)
time.sleep(2)

# Ввод даты через пикер
driver.refresh()
date_field.click()
new_date_field = driver.find_element(By.XPATH, "//div[@aria-label='Choose Tuesday, October 31st, 2023']")
new_date_field.click()
time.sleep(2)

# Ввод даты через пикер + автогенерация даты
driver.refresh()
date_field.click()
new_date_field = driver.find_element(By.XPATH, f"//div[contains(@aria-label, ' October {test_day}st, {test_year}']")
new_date_field.click()
time.sleep(2)


# Ввод даты через функционал XPATH Contains
date_field.click()
today_date_field = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
today_date_field.click()
time.sleep(2)

time.sleep(2)
driver.close()
