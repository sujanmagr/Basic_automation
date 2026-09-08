from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://gurubus.com.np/sign-in")

wait = WebDriverWait(driver, 15)

# Login
email = wait.until(
    EC.visibility_of_element_located((By.NAME, "email"))
)
email.send_keys("shrestharaman041@gmail.com")

password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
password.send_keys("RamaN619@")

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_button.click()

# Wait for page after login
time.sleep(5)

# FROM field
from_city = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]"))
)
from_city.send_keys("Kathmandu")

# TO field
to_city = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[2]"))
)
to_city.send_keys("Pokhara")


tomorrow_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Tomorrow')]")
    )
)
tomorrow_button.click()

SearchBuses_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
SearchBuses_button.click()

time.sleep(4)

date_button = wait.until(
    EC.element_to_be_clickable( (By.XPATH, "//button[.//span[normalize-space()='Tue'] and .//span[normalize-space()='5'] and .//span[normalize-space()='Sep']]") )
)

date_button.click()

time.sleep(4)
# Then Book Now

book_buttons = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//button[normalize-space()='Book Now'][1]")
    )
)

book_buttons.click()

time.sleep(4)