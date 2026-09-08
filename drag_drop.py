#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
#launch browser
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

# driver.implicitly_wait(10)

#store url
url="https://formy-project.herokuapp.com/dragdrop"
#website visit
driver.get(url)
time.sleep(2)

actions=ActionChains(driver)
drag_element=driver.find_element(By.XPATH, "//div[@id='image']//img")
drop_location=driver.find_element(By.XPATH, "//div[@id='box']")
actions.drag_and_drop(drag_element, drop_location).perform()
time.sleep(3)

driver.quit()
