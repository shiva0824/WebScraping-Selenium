#first Task:

#step-1.open web broswer(chrome/edge..)
#step-2.open url https://opensource-demo.orangehrmlive.com/
#step-3.enter username (Admin)
#step-4.enter password (admin123)
#step-5.click on login
#step-6.capture tilte of the homepage(Actual title)
#step-7.Verify title of the homepage: OrangeHRM  (expected title)
#step-8.Close broswer


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Step-1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Step-2: Open the website
driver.get('https://opensource-demo.orangehrmlive.com/')
#Note: To perform 3-8 steps....we need to access the methods which are in .Chrome class......we can access those methods only using objects(i.e driver in our case)

#step3
#send_keys method will help to add the text to a textbox
#driver.find_element(By.NAME, 'username').send_keys('admin123').....actually this line of code should be enough....but our page is..
#taking some time load...hence used below method
# Wait for the username field to be present
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username'))) #selecting by name tag
username_field.send_keys('Admin')

#step4
# Wait for the password field to be present
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))#selecting by name tag
#password_filed = driver.find_element(By.NAME, 'password')
password_field.send_keys('admin123')

#step5
# Wait for the login button to be clickable
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.oxd-button.oxd-button--main')))#selecting by css selector tag
#login_button = driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--main')
login_button.click()

#step6
#title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'title'))) #selecting by html tag name
title = driver.title
expected_title = 'OrangeHRM'

#step7
if title == expected_title:
    print('Task is Sucessfully completed')
else:
    print('Task failed')

#step8
driver.close()