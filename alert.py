#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#launch browser
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
alert_button=driver.find_element(By.ID, "alert-button")
alert_button.click()
time.sleep(2)

alert=driver.switch_to.alert
alert.accept()
# alert.dismiss()

time.sleep(3)
driver.quit()
