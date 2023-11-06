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
time.sleep(3)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
time.sleep(3)

# PRODUCTS PAGE
# PRODUCT 1 INFO
light_products = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
light_products_text = light_products.text
print("Product #1 - " + light_products_text)

light_price_products = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
light_price_products_text = light_price_products.text
print("Product #1 price - " + light_price_products_text)

# PRODUCT 2 INFO
jacket_products = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
jacket_products_text = jacket_products.text
print("Product #2 - " + jacket_products_text)

jacket_price_products = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
jacket_price_products_text = jacket_price_products.text
print("Product #2 price - " + jacket_price_products_text)

# ADD PRODUCTS TO CART
# PRODUCT 1
add_light_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
add_light_to_cart_button.click()
print("Product #1 added to cart")

# PRODUCT 2
add_jacket_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
add_jacket_to_cart_button.click()
print("Product #2 added to cart")
time.sleep(3)

# CART OPENED
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Cart opened")

# CART PAGE
# PRODUCT 1
light_cart = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
light_cart_text = light_cart.text
print("Cart product #1 - " + light_cart_text)

light_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
light_price_cart_text = light_price_cart.text
print("Cart product #1 price - " + light_price_cart_text)

# PRODUCT 2
jacket_cart = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']/div")
jacket_cart_text = jacket_cart.text
print("Cart product #2 - " + jacket_cart_text)

jacket_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
jacket_price_cart_text = jacket_price_cart.text
print("Cart product #2 price - " + jacket_price_cart_text)













time.sleep(3)
driver.close()
