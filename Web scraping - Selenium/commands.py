from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://demo.nopcommerce.com/register')

driver.maximize_window()

#application commands:
#print(driver.title)
#print(driver.current_url)

#conditional commands:
a = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status : ", a.is_displayed())
print("Enabled status : ", a.is_enabled())

print(f'Status before clicking buttons:')
b = driver.find_element(By.XPATH, "//input[@value='M']")
c = driver.find_element(By.XPATH, "//input[@value='F']")
print("male : ", b.is_selected())
print("female: ", c.is_selected())

print(f'Status after clicking female radio button:')
c.click()
print("male: ", b.is_selected())
print("female: ", c.is_selected())




