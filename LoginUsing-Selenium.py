import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("")

driver.maximize_window()



email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
email_field.clear()  # Clear field before entering text
email_field.send_keys("")

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
password_field.clear()  # Clear field before entering text
password_field.send_keys("")

driver.get_screenshot_as_file("LoginPage.png")

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()  # Click login button

WebDriverWait(driver, 15).until(EC.url_changes(""))  # Wait for login completion

time.sleep(3)
