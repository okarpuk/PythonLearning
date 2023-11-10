import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/dynamic-properties/'
driver.get(base_url)
driver.maximize_window()

# неявное ожидание - макс 10 секунд
driver.implicitly_wait(10)
visible_after = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")

# явное ожидание - макс 30 секунд
visible_after = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(By.XPATH, "//button[@id='visibleAfter']"))

visible_after.click()







time.sleep(5)
driver.close()
