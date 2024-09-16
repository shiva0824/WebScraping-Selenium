from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


#step1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)


innerframe = driver.find_element(By.XPATH, "//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
driver.switch_to.frame(innerframe)


driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")

driver.switch_to.parent_frame()  #directly switch to parent frame
time.sleep(10)