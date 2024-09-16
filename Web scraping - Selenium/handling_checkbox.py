from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


#step1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))


#selecting specific checkbox
#driver.find_element(By.XPATH, "//input[@type='checkbox'][8]").click()

# selecting checkboxes by choice
##for i in checkboxes:
 #   weekname = i.get_attribute('id')
 #   if weekname == "monday" or weekname == "sunday":
 #       i.click()

#selecting last 2 checkboxes
#for i in range(len(checkboxes)-2,len(checkboxes)):
#    checkboxes[i].click()

#selecting first 2 checkboxes
#for i in range(len(checkboxes)):
#    if i<2:
#        checkboxes[i].click()

#selecting all checkboxes
for i in range(len(checkboxes)):
    checkboxes[i].click()

time.sleep(5)

#clearing all checkboxes
for i in checkboxes:
    if i.is_selected():
        i.click()

time.sleep(10)

