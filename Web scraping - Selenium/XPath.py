from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver4 = webdriver.Chrome(service=s)

driver4.get('https://www.facebook.com/')
driver4.maximize_window()

#absolute xpath
#driver4.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys('shiva351817@gmail.com')
#driver4.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]' ).send_keys('Shiva@0824')
#driver4.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()


#relative xpath
driver4.find_element(By.XPATH, '//*[@id="email"]').send_keys('shiva351817@gmail.com')
driver4.find_element(By.XPATH, '//*[@id="pass"]').send_keys('Shiva@0824')
#driver4.find_element(By.XPATH, '//*[@id="u_0_9_aw"]').click()


time.sleep(30)