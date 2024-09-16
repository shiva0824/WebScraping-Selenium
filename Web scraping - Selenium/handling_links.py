from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://automationexercise.com/')
driver.maximize_window()

#click on link
#driver.find_element(By.LINK_TEXT, "Test Cases").click()

#finding no:of links
links = driver.find_elements(By.XPATH, "//a")
print(len(links))

#printing all link names
for i in links:
    print(i.text)


time.sleep(10)