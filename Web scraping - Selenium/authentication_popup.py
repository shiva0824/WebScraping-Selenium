from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


#step1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)


#driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

time.sleep(10)