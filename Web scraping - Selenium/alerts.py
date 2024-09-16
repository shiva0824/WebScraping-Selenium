
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


#step1
s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alert_window = driver.switch_to.alert

print(alert_window.text) #captures text of alert window
alert_window.send_keys("welcome")  #passing input to input box

alert_window.accept() #close the alert window by using OK button
#alert_window.dismiss() #close the alert window by using CANCEL button

time.sleep(10)




