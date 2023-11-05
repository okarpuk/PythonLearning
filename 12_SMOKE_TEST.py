import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# AUTHORIZATION
login_standard_user = "standard_user"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)

password_standard_user = "secret_sauce"
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_standard_user)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
time.sleep(5)

# PRODUCT INFO - PRODUCTS PAGE
product_backpack = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
product_backpack_text = product_backpack.text
print(product_backpack_text)

price_backpack = driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[1]//div[2]//div[2]//div[1]")
price_backpack_text = price_backpack.text
print(price_backpack_text)

# ADD PRODUCT TO CART
add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart_button.click()
print("Product added to cart")
time.sleep(5)

cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Cart opened")
time.sleep(5)



