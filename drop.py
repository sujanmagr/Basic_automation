#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#launch browser
# driver=webdriver.Chrome()
# time.sleep(2)
# driver.maximize_window()

driver=webdriver.Chrome()
time.sleep(1)
driver.maximize_window()
# driver.implicitly_wait(10)

#store url
url="https://formy-project.herokuapp.com/form"
#website visit
driver.get(url)
time.sleep(2)

first_name=driver.find_element(By.ID, "first-name")

first_name.send_keys("Sachin")
time.sleep(3)
driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)
dropdown=driver.find_element(By.ID, "select-menu")
select=Select(dropdown)
select.select_by_value("4")
time.sleep(2)
driver.quit()
