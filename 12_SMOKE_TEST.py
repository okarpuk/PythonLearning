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

# PRODUCT INFO - PRODUCTS PAGE
item_products = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
item_products_text = item_products.text
print("Products page item - " + item_products_text)

price_products = driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[1]//div[2]//div[2]//div[1]")
price_products_text = price_products.text
print("Products page price - " + price_products_text)

# ADD PRODUCT TO CART
add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart_button.click()
print("Product added to cart")
time.sleep(3)

# CART OPENED
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Cart opened")
time.sleep(3)

# PRODUCT INFO - CART PAGE
item_cart = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
item_cart_text = item_cart.text
print("Cart page item - " + item_cart_text)

price_cart = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
price_cart_text = price_cart.text
print("Cart page price - " + price_cart_text)

# ASSERTS ITEM TEXT & ITEM PRICE
assert item_products_text == item_cart_text
print("ITEM TEXT CORRECT")
assert price_products_text == price_cart_text
print("PRICE CORRECT")

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

# PRODUCT INFO - CHECKOUT PAGE
item_checkout = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
item_checkout_text = (item_checkout.text)
print("Checkout page item - " + item_checkout_text)

price_checkout = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
price_checkout_text = price_checkout.text
print("Checkout page price - " + price_checkout_text)

price_total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
price_total_text = price_total.text
print("Total item price - " + price_total_text)

# ASSERTS ITEM TEXT & ITEM PRICE
assert item_products_text == item_checkout_text
print("ITEM TEXT CORRECT")
assert price_products_text == price_checkout_text
print("ITEM PRICE CORRECT")
assert ("Item total: " + price_products_text) == price_total_text
print("TOTAL PRICE CORRECT")

driver.close()
