import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
time.sleep(10)

tv_button = driver.find_element(By.XPATH,"//a[@class='header-categories__item'][contains(text(),'Телевизоры')]")
tv_button.click()


######### TV PAGE ###########

action = ActionChains(driver)
price_slider_1 = driver.find_element(By.XPATH, "//*[@id='filter-range-price']/span[1]")
action.click_and_hold(price_slider_1).move_by_offset(20, 0).release().perform()

price_slider_2 = driver.find_element(By.XPATH, "//*[@id='filter-range-price']/span[2]")
action.click_and_hold(price_slider_2).move_by_offset(-50, 0).release().perform()

brands_dropdown = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[3]/div[2]/div[8]/label")
brands_dropdown.click()

checkbox_lg = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[3]/div[2]/div[10]/div/div/div/div[10]/label/span[1]/span")
checkbox_lg.click()

checkbox_diagonal = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[5]/div[3]/div[6]/label/span[1]")
driver.execute_script("arguments[0].click();", checkbox_diagonal)

checkbox_screen_technology = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[6]/div[3]/div[2]/label/span[1]/span")
driver.execute_script("arguments[0].click();", checkbox_screen_technology)

checkbox_screen_resolution = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[7]/div[3]/div[3]/label/span[1]/span")
driver.execute_script("arguments[0].click();", checkbox_screen_resolution)

confirm_filter_button = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[33]/button[1]")
driver.execute_script("arguments[0].click();", confirm_filter_button)

# работает только так. При использовании ожиданий выдает ошибку - Stale element
time.sleep(3)
add_to_cart_button = driver.execute_script("return document.querySelector('.action-btn--btn-buy');")
add_to_cart_button.click()

cart_button = driver.find_element(By.XPATH,"//a[@id='cart-link']")
cart_button.click()


########## CART PAGE #############





time.sleep(10)

















driver.close()



