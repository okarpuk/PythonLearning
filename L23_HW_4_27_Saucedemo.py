import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Welcome to our online-store")
print("Choose one of the following products and enter its number:\n1 - Sauce Labs Backpack,\n2 - Sauce Labs Bike Light,\n3 - Sauce Labs Bolt T-Shirt,\n4 - Sauce Labs Fleece Jacket,\n5 - Sauce Labs Onesie,\n6 - Test.allTheThings() T-Shirt (Red)\n")
entered_number = int(input())

if entered_number > 0 and entered_number < 7:
    driver = webdriver.Chrome()
    base_url = 'https://www.saucedemo.com/'
    driver.delete_all_cookies()
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(5)
else:
    print("Incorrect number. Please enter number from 1 to 6")
    sys.exit()

# AUTHORIZATION
login_standard_user = "standard_user"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)

password_standard_user = "secret_sauce"
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_standard_user)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

# PRODUCTS PAGE
# PRODUCT 1
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
price_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
add_to_cart_button_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
product_1_text = product_1.text
price_1_text = price_1.text
# PRODUCT 2
product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
price_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
add_to_cart_button_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
product_2_text = product_2.text
price_2_text = price_2.text
# PRODUCT 3
product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
price_3 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
add_to_cart_button_3 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
product_3_text = product_3.text
price_3_text = price_3.text
# PRODUCT 4
product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
price_4 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
add_to_cart_button_4 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
product_4_text = product_4.text
price_4_text = price_4.text
# PRODUCT 5
product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
price_5 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
add_to_cart_button_5 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
product_5_text = product_5.text
price_5_text = price_5.text
# PRODUCT 6
product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
price_6 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
add_to_cart_button_6 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
product_6_text = product_6.text
price_6_text = price_6.text

# ADD PRODUCT TO CART
def add_to_cart (button_number, product_number, price_number):
    button_number.click()
    print(f"Product: '{product_number}' added to cart.\nPrice - {price_number}")
    return

if entered_number == 1:
    add_to_cart(add_to_cart_button_1, product_1_text, price_1_text)
elif entered_number == 2:
    add_to_cart(add_to_cart_button_2, product_2_text, price_2_text)
elif entered_number == 3:
    add_to_cart(add_to_cart_button_3, product_3_text, price_3_text)
elif entered_number == 4:
    add_to_cart(add_to_cart_button_4, product_4_text, price_4_text)
elif entered_number == 5:
    add_to_cart(add_to_cart_button_5, product_5_text, price_5_text)
elif entered_number == 6:
    add_to_cart(add_to_cart_button_6, product_6_text, price_6_text)

# CART OPENED
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Cart opened")

# CART PAGE AND ASSERTS
if entered_number == 1:
    cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
elif entered_number == 2:
    cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
elif entered_number == 3:
    cart_product_3 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
elif entered_number == 4:
    cart_product_4 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
elif entered_number == 5:
    cart_product_5 = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
elif entered_number == 6:
    cart_product_6 = driver.find_element(By.XPATH, "//*[@id='item_3_title_link']/div")

cart_price = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

def cart_and_assert (product_number, product_cart, price_number):
    assert product_number == product_cart.text
    print(f"Product name ({product_number}) CORRECT with cart name ({product_cart.text})")
    assert price_number == cart_price.text
    print(f"Product price ({price_number}) CORRECT with cart price ({cart_price.text})")
    return

if entered_number == 1:
    cart_and_assert(product_1_text, cart_product_1, price_1_text)
elif entered_number == 2:
    cart_and_assert(product_2_text, cart_product_2, price_2_text)
elif entered_number == 3:
    cart_and_assert(product_3_text, cart_product_3, price_3_text)
elif entered_number == 4:
    cart_and_assert(product_4_text, cart_product_4, price_4_text)
elif entered_number == 5:
    cart_and_assert(product_5_text, cart_product_5, price_5_text)
elif entered_number == 6:
    cart_and_assert(product_6_text, cart_product_6, price_6_text)

# CHECKOUT BUTTON
checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Checkout button clicked")

# USER INFO ENTRY
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

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Continue button clicked")

# CHECKOUT PAGE
if entered_number == 1:
    checkout_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
elif entered_number == 2:
    checkout_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
elif entered_number == 3:
    checkout_product_3 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
elif entered_number == 4:
    checkout_product_4 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
elif entered_number == 5:
    checkout_product_5 = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
elif entered_number == 6:
    checkout_product_6 = driver.find_element(By.XPATH, "//*[@id='item_3_title_link']/div")

checkout_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

def checkout_and_assert (product_number, product_checkout, price_number):
    assert product_number == product_checkout.text
    print(f"Product name ({product_number}) CORRECT with checkout name ({product_checkout.text})")
    assert price_number == checkout_price.text
    print(f"Product price ({price_number}) CORRECT with checkout price ({checkout_price.text})")
    return

if entered_number == 1:
    checkout_and_assert(product_1_text, checkout_product_1, price_1_text)
elif entered_number == 2:
    checkout_and_assert(product_2_text, checkout_product_2, price_2_text)
elif entered_number == 3:
    checkout_and_assert(product_3_text, checkout_product_3, price_3_text)
elif entered_number == 4:
    checkout_and_assert(product_4_text, checkout_product_4, price_4_text)
elif entered_number == 5:
    checkout_and_assert(product_5_text, checkout_product_5, price_5_text)
elif entered_number == 6:
    checkout_and_assert(product_6_text, checkout_product_6, price_6_text)

# ASSERTS ITEM TOTAL
item_total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
item_total_clear = item_total.text.replace("Item total: ", "")
assert checkout_price.text == item_total_clear
print(f"Checkout price ({checkout_price.text}) CORRECT with Item total ({item_total_clear})")

#FINISH
button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()

driver.close()