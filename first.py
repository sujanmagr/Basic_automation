#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#launch browser
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

# driver.implicitly_wait(10)

#store url
url="https://www.saucedemo.com/"
#website visit
driver.get(url)
time.sleep(2)
#syntax: driver.find_element(By.locator, "value")
# username=driver.find_element(By.ID, "user-name")
username=driver.find_element(*(By.XPATH,"//input[@id='user-name']"))
username.send_keys("standard_user")
# password=driver.find_element(By.ID, "password")
password=driver.find_element(*(By.XPATH,"//input[@id='password']"))
password.send_keys("secret_sauce")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

# login_button=driver.find_element(By.NAME, "login-button")
login_button=wait.until(EC.element_to_be_clickable((By.NAME, "login-button")))
from selenium.webdriver.common.action_chains import ActionChains
actions=ActionChains(driver)
# login_button.click()
actions.double_click(login_button).perform()


actions.drag_and_drop()

time.sleep(4)

# driver.execute_script("window.scrollBy(0,400);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0,0);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#quit browser
driver.quit()





# #relative xpath
# //*[@id="user-name"]

# #absolute xpath
# /html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input