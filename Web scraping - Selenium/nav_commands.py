from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.facebook.com/')
driver.get('https://www.amazon.com/')

driver.back() #facebook
driver.forward() #amazon

driver.refresh() #reloads the page

time.sleep(10)

driver.quit()