#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#launch browser
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
#store url
url="https://formy-project.herokuapp.com/switch-window"
#website visit
driver.get(url)
time.sleep(2)
switch_button=driver.find_element(By.XPATH, "//button[@id='new-tab-button']")
switch_button.click()
windows=driver.window_handles
print(windows)

# print(windows[0])
# print(windows[1])
# print(windows[0])
print(driver.current_window_handle)
driver.switch_to.window(windows[1])
time.sleep(2)
# driver.find_element(By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Autocomplete']").click()
print(driver.current_window_handle)
time.sleep(2)
driver.close()
time.sleep(2)
driver.quit()
