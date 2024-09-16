from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver3 = webdriver.Chrome(service=s)

driver3.get('https://www.facebook.com/')
#css selectors

#1. tag,id
driver3.find_element(By.CSS_SELECTOR, 'input#email').send_keys('nani@gmail.com')
#or can also be written as
#driver3.find_element(By.CSS_SELECTOR, '#email').send_keys('nani@gmail.com')


#2. tag, classname
driver3.find_element(By.CSS_SELECTOR, 'input.inputtext').clear()
#or can also be written as
#driver3.find_element(By.CSS_SELECTOR, '.inputtext').clear()

#3. tag, attribute
driver3.find_element(By.CSS_SELECTOR, 'input[data-testid=royal_email]').send_keys('shiva@gmail.com')
#or can also be written as
#driver3.find_element(By.CSS_SELECTOR, '[data-testid=royal_email]').send_keys('shiva@gmail.com')

#4. tag, class, attribute
driver3.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid=royal_pass]').send_keys('Shiva@2002')

time.sleep(30)