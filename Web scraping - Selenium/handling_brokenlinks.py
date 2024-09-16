from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests as requests

s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)


#we need to install requests package through file-->settings--.project interpreter-->click on + and search for 'requests' and install it.

driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

links = driver.find_elements(By.XPATH, "//a")
count = 0

#try except is used, as some network exceptions might be thrown...so to avoid them

for i in links:
    url = i.get_attribute("href")
    try:
        response = requests.head(url) #this request will hit the server and server will give the response
    except:
        None


    if response.status_code>=400:
        print(url, " is a broken link.")
        count+=1
    else:
        print(url, " is a valid link")

print("Total number of broken links: ", count)

time.sleep(10)




