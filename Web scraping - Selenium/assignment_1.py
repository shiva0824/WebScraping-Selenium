#Assignment - Task 2:

#step-1.open web broswer(chrome/edge..)
#step-2.open url https://admin-demo.nopcommerce.com/login
#step-3.provide email (admin@yourstore.com)
#step-4.provide password (admin)
#step-5.click on login
#step-6.capture tilte of the dashboard page(Actual title)
#step-7.Verify title of the homepage: 'Dashboard / nopCommerce administration' (expected title)
#step-8.Close broswer

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#step1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver1 = webdriver.Chrome(service=s)

#step2
driver1.get('https://admin-demo.nopcommerce.com/login')

#step3
WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.NAME, 'Email'))).clear() #performing this step as we already have email inthere
email = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.NAME, 'Email')))
email.send_keys('admin@yourstore.com')

#step4
WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.NAME, 'Password'))).clear() #performing this step as we already have PASSWORD inthere
password = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.NAME, 'Password')))
password.send_keys('admin')

#step5
login = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'login-button')))
login.click()

#step6
title1 = driver1.title
print(title1)
exp_title = 'Dashboard / nopCommerce administration'

#step7
if title1 == exp_title:
    print('Assignment is done successfully')
else:
    print('Task failed')

#step8

driver1.close()

