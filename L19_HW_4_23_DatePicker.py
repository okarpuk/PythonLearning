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

# Get text lenght in date field and use Backspace for each symbol
for i in range(len(date_field.get_attribute(name="value"))):
    date_field.send_keys(Keys.BACKSPACE)

# Automatic date generation
test_day = int(datetime.datetime.utcnow().strftime("%d")) + 10
print(f"Test day - {test_day}")
test_month = int(datetime.datetime.utcnow().strftime("%m"))
print(f"Test month - {test_month}")
test_year = int(datetime.datetime.utcnow().strftime("%Y"))
print(f"Test year - {test_year}")

# Send generated date into field
date_field.send_keys(f"{test_month}/{test_day}/{test_year}")
date_field.send_keys(Keys.RETURN)
time.sleep(2)

driver.close()