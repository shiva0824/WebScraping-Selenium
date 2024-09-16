from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver2 = webdriver.Chrome(service=s)

#driver2.get('http://automationpractice.com/index.php')
driver2.get('https://www.inmotionhosting.com/')

#Class_name
a = driver2.find_elements(By.CLASS_NAME, 'imh-rostrum-card ')
print(len(a)) #9 tags using class name 'imh-rostrum-card'

#linktext
#WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.LINK_TEXT, ' WordPress '))).click()
#driver2.find_element(By.LINK_TEXT, ' WordPress ').click()

#finding more than one element
b = driver2.find_elements(By.TAG_NAME, 'a')
print(len(b))  #we have 255 a tags in our website

