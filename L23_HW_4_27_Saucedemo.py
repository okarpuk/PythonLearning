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
time.sleep(3)

# PRODUCTS PAGE
# DICTIONARY WITH ALL PRODUCTS AND PRICES
products_page = {
    "product_1": driver.find_element(By.XPATH, "//a[@id='item_4_title_link']"),
    "price_1": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"),
    "add_to_cart_button_1": driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"),
    "product_2": driver.find_element(By.XPATH, "//a[@id='item_0_title_link']"),
    "price_2": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"),
    "add_to_cart_button_2": driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"),
    "product_3": driver.find_element(By.XPATH, "//a[@id='item_1_title_link']"),
    "price_3": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div"),
    "add_to_cart_button_3": driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"),
    "product_4": driver.find_element(By.XPATH, "//a[@id='item_5_title_link']"),
    "price_4": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div"),
    "add_to_cart_button_4": driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"),
    "product_5": driver.find_element(By.XPATH, "//a[@id='item_2_title_link']"),
    "price_5": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div"),
    "add_to_cart_button_5": driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']"),
    "product_6": driver.find_element(By.XPATH, "//a[@id='item_3_title_link']"),
    "price_6": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"),
    "add_to_cart_button_6": driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
}

# ADD PRODUCT TO CART
if entered_number == 1:
    products_page["add_to_cart_button_1"].click()
    print(f"Product: '{products_page['product_1'].text}' added to cart.\nPrice - {products_page['price_1'].text}")
elif entered_number == 2:
    products_page["add_to_cart_button_2"].click()
    print(f"Product: '{products_page['product_2'].text}' added to cart.\nPrice - {products_page['price_2'].text}")
elif entered_number == 3:
    products_page["add_to_cart_button_3"].click()
    print(f"Product: '{products_page['product_3'].text}' added to cart.\nPrice - {products_page['price_3'].text}")
elif entered_number == 4:
    products_page["add_to_cart_button_4"].click()
    print(f"Product: '{products_page['product_4'].text}' added to cart.\nPrice - {products_page['price_4'].text}")
elif entered_number == 5:
    products_page["add_to_cart_button_5"].click()
    print(f"Product: '{products_page['product_5'].text}' added to cart.\nPrice - {products_page['price_5'].text}")
elif entered_number == 6:
    products_page["add_to_cart_button_6"].click()
    print(f"Product: '{products_page['product_6'].text}' added to cart.\nPrice - {products_page['price_6'].text}")

# CART OPENED
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Cart opened")
time.sleep(3)


# # CART PAGE
cart_page = {
    "product_1": driver.find_element(By.XPATH, "//a[@id='item_4_title_link']"),
    "price_1": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"),
    "product_2": driver.find_element(By.XPATH, "//a[@id='item_0_title_link']"),
    "price_2": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"),
    "product_3": driver.find_element(By.XPATH, "//a[@id='item_1_title_link']"),
    "price_3": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div"),
    "product_4": driver.find_element(By.XPATH, "//a[@id='item_5_title_link']"),
    "price_4": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div"),
    "product_5": driver.find_element(By.XPATH, "//a[@id='item_2_title_link']"),
    "price_5": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div"),
    "product_6": driver.find_element(By.XPATH, "//a[@id='item_3_title_link']"),
    "price_6": driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"),
}

# # PRODUCT 1
# product_1_cart = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
# product_1_cart_text = product_1_cart.text
# product_1_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
# product_1_price_cart_text = product_1_price_cart.text
#
# product_2_cart = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
# product_2_cart_text = product_2_cart.text
# product_2_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
# product_2_price_cart_text = product_2_price_cart.text
#
# product_3_cart = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
# product_3_cart_text = product_3_cart.text
# product_3_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[5]/div[2]/div[2]/div")
# product_3_price_cart_text = product_3_price_cart.text
#
# product_4_cart = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
# product_4_cart_text = product_4_cart.text
# product_4_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[6]/div[2]/div[2]/div")
# product_4_price_cart_text = product_4_price_cart.text
#
# product_5_cart = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
# product_5_cart_text = product_5_cart.text
# product_5_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[7]/div[2]/div[2]/div")
# product_5_price_cart_text = product_5_price_cart.text
#
# product_6_cart = driver.find_element(By.XPATH, "//*[@id='item_3_title_link']/div")
# product_6_cart_text = product_6_cart.text
# product_6_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[8]/div[2]/div[2]/div")
# product_6_price_cart_text = product_6_price_cart.text
#
#
#




# # ASSERTS CART TEXT & CART PRICE
# # PRODUCT 1
# assert light_products_text == light_cart_text
# print("PRODUCT #1 - CART TEXT CORRECT")
# assert light_price_products_text == light_price_cart_text
# print("PRODUCT #1 - CART PRICE CORRECT")








#
# # CHECKOUT BUTTON
# checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
# checkout_button.click()
# print("Checkout button clicked")
# time.sleep(3)
#
# # USER INFO ENTRY
# first_name = "Jack"
# first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
# first_name_field.send_keys(first_name)
# print("First name entered")
#
# last_name = "Daniels"
# last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
# last_name_field.send_keys(last_name)
# print("Last name entered")
#
# zip_code = "12345"
# zip_code_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
# zip_code_field.send_keys(zip_code)
# print("Zip code entered")
# time.sleep(3)
#
# # CONTINUE BUTTON
# continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
# continue_button.click()
# print("Continue button clicked")
# time.sleep(3)
#
# # CHECKOUT PAGE
# # PRODUCT 1 INFO
# light_checkout = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
# light_checkout_text = light_checkout.text
# print("Checkout product #1 - " + light_checkout_text)
#
# light_price_checkout = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
# light_price_checkout_text = light_price_checkout.text
# print("Checkout product #1 price - " + light_price_checkout_text)
#
# # PRODUCT 2 INFO
# onesie_checkout = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
# onesie_checkout_text = onesie_checkout.text
# print("Checkout product #2 - " + onesie_checkout_text)
#
# onesie_price_checkout = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
# onesie_price_checkout_text = onesie_price_checkout.text
# print("Checkout product #2 price - " + onesie_price_checkout_text)
#
# # ASSERTS CHECKOUT TEXT & CHECKOUT PRICE
# # PRODUCT 1
# assert light_products_text == light_checkout_text
# print("PRODUCT #1 - CHECKOUT TEXT CORRECT")
# assert light_price_products_text == light_price_checkout_text
# print("PRODUCT #1 - CHECKOUT PRICE CORRECT")
#
# # PRODUCT 2
# assert onesie_products_text == onesie_checkout_text
# print("PRODUCT #2 - CHECKOUT TEXT CORRECT")
# assert onesie_price_products_text == onesie_price_checkout_text
# print("PRODUCT #2 - CHECKOUT PRICE CORRECT")
#
# # CHECKOUT PRICES SUM
# light_clear_price = float(light_price_checkout_text.replace("$", ""))
# print(f"Product #1 clear checkout price - {light_clear_price}")
# onesie_clear_price = float(onesie_price_checkout_text.replace("$", ""))
# print(f"Product #2 clear checkout price - {onesie_clear_price}")
# prices_sum = light_clear_price + onesie_clear_price
# print(f"Checkout prices sum - {prices_sum}")
#
# # ITEM TOTAL
# item_total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
# item_total_clear = float(item_total.text.replace("Item total: $", ""))
# print(f"Item total clear - {item_total_clear}")
#
# # ASSERT CHECKOUT PRICES SUM & ITEM TOTAL
# assert prices_sum == item_total_clear
# print("ITEM TOTAL CORRECT")
#
# #FINISH
# button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
# button_finish.click()
# time.sleep(3)

driver.close()
