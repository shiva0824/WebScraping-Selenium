from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


#step1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#windowid = driver.current_window_handle
#print(windowid)  # 1st time --> 0F77790F7F148B0F241380A690BBFBF9
                 #2nd time --> 9680EAED5FADD09272EA5196271931F5
#Note**: Everytime when we open the ulr, new id will be created by the browser randomly.

driver.find_element(By.CSS_SELECTOR, "a[href='http://www.orangehrm.com']").click()
windowids = driver.window_handles
parentwindowid = windowids[0]
childwindowid = windowids[1]

print(parentwindowid)
print(childwindowid)


#approach 1
driver.switch_to.window(childwindowid)
print(driver.title)

driver.switch_to.window(parentwindowid)
print(driver.title)

#approach 2
#for i in windowids:
#    driver.switch_to.window(i)
#   print(driver.title)

#close specific browser window

for i in windowids:
    driver.switch_to.window(i)
    if driver.title == "OrangeHM" :
        driver.close()

time.sleep(10)