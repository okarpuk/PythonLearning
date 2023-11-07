import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
elements_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")
elements_button.click()
time.sleep(2)

checkbox_button = driver.find_element(By.XPATH, "//li[@id='item-1']")
checkbox_button.click()
time.sleep(2)

checkbox_tree = driver.find_element(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
checkbox_tree.click()

checkbox = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/span/label/span[1]")
checkbox.click()
time.sleep(2)

# Assertion is checkbox marked
is_checked = checkbox.is_selected()

if is_checked:
    print("Checkbox marked")
else:
    print("Checkbox does not marked")

time.sleep(2)
driver.close()
