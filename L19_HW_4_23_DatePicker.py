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

# Catch incorrect month / date
if test_month < 1 or test_month > 12:
    print(f"Incorrect month number - {test_month}. Should be from 1 to 12")
elif test_month == 2 and (test_day < 1 or test_day > 28):
    print(f"Incorrect date for month - {test_month}. Should be from 1 to 28")
elif (test_month == 4 or test_month == 6 or test_month == 9 or test_month == 11) and (test_day < 1 or test_day > 30):
    print(f"Incorrect date for month - {test_month}. Should be from 1 to 30")
elif (test_month == 1 or test_month == 3 or test_month == 5 or test_month == 7 or test_month == 8 or test_month == 10 or test_month == 12) and (test_day < 1 or test_day > 31):
    print(f"Incorrect date for month - {test_month}. Should be from 1 to 31")

# Send correct date into field
else:
    date_field.send_keys(f"{test_month}/{test_day}/{test_year}")
    date_field.send_keys(Keys.RETURN)

time.sleep(2)
driver.close()