#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#launch browser
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

#store url
url="https://formy-project.herokuapp.com/fileupload"
#website visit
driver.get(url)
time.sleep(2)

file_upload=driver.find_element(By.ID, "file-upload-field")

file_upload.send_keys(r"C:\Users\Bhabisara Budhathoki\Downloads\HIDR_Bug_Report_BOOK_001.docx",)
time.sleep(2)

reset_button=driver.find_element(By.XPATH, "/html/body/div/form/div/div/span[2]/button")

reset_button.click()
driver.quit()


