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
onesie_products = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
onesie_products_text = onesie_products.text
print("Product #2 - " + onesie_products_text)

onesie_price_products = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
onesie_price_products_text = onesie_price_products.text
print("Product #2 price - " + onesie_price_products_text)

# ADD PRODUCTS TO CART
# PRODUCT 1
add_light_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
add_light_to_cart_button.click()
print("Product #1 added to cart")

# PRODUCT 2
add_onesie_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
add_onesie_to_cart_button.click()
print("Product #2 added to cart")
time.sleep(3)

# CART OPENED
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Cart opened")
time.sleep(3)

# CART PAGE
# PRODUCT 1
light_cart = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
light_cart_text = light_cart.text
print("Cart product #1 - " + light_cart_text)

light_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
light_price_cart_text = light_price_cart.text
print("Cart product #1 price - " + light_price_cart_text)

# PRODUCT 2
onesie_cart = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']/div")
onesie_cart_text = onesie_cart.text
print("Cart product #2 - " + onesie_cart_text)

onesie_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
onesie_price_cart_text = onesie_price_cart.text
print("Cart product #2 price - " + onesie_price_cart_text)

# ASSERTS PRODUCTS TEXT & PRODUCTS PRICE
# PRODUCT 1
assert light_products_text == light_cart_text
print("PRODUCT #1 TEXT CORRECT")
assert light_price_products_text == light_price_cart_text
print("PRODUCT #1 PRICE CORRECT")

# PRODUCT 2
assert onesie_products_text == onesie_cart_text
print("PRODUCT #2 TEXT CORRECT")
assert onesie_price_products_text == onesie_price_cart_text
print("PRODUCT #2 PRICE CORRECT")

# CHECKOUT BUTTON
checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Checkout button clicked")
time.sleep(3)

# USER INFO ENTRY ON CHECKOUT PAGE
first_name = "Jack"
first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_field.send_keys(first_name)
print("First name entered")

last_name = "Daniels"
last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_field.send_keys(last_name)
print("Last name entered")

zip_code = "12345"
zip_code_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code_field.send_keys(zip_code)
print("Zip code entered")
time.sleep(3)

# CONTINUE BUTTON
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Continue button clicked")
time.sleep(3)









time.sleep(3)
driver.close()
