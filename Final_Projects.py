import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
base_url = 'https://www.7745.by/'
driver.get(base_url)
driver.maximize_window()

######### MAIN PAGE ###########

enter_button = driver.find_element(By.XPATH,"//div[@id='logon-link']/div[2]")
enter_button.click()

selector_registration = driver.find_element(By.XPATH,"//div[@class='open-logon open-login']//div//select[@name='prefix']")
selector_registration.click()

se = Select(selector_registration)
for item in se.options:
    if item.text == 'e-mail':
        item.click()
        break

login_standard_user = "final_project_test@mail.ru"
user_name = driver.find_element(By.XPATH, "//div[@class='open-logon open-login']//div//input[@id='login-modal-input-login']")
user_name.send_keys(login_standard_user)

password_standard_user = "1A.2b.3c.4d"
user_password = driver.find_element(By.XPATH, "//div[@class='open-logon open-login']//div//input[@id='password']")
user_password.send_keys(password_standard_user)

enter_2_button = driver.find_element(By.CSS_SELECTOR,"div[class='open-logon open-login'] div input[value='Войти']")
enter_2_button.click()
print("Enter 2 button clicked")
time.sleep(10)

TV_button = driver.find_element(By.XPATH,"//a[@class='header-categories__item'][contains(text(),'Телевизоры')]")
TV_button.click()
time.sleep(5)

######### TV PAGE ###########

