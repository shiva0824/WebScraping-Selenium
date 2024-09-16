import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


s = Service(r'C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

dropdown = driver.find_element(By.XPATH, "//select[@id='country']")
drpcountry = Select(dropdown)

#selecting option from the dropdown
#drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("13") #Australia
#drpcountry.select_by_index(17)  #Bangladesh #index

#capture all the options and print them
all_options = drpcountry.options
#print(len(all_options))

#for i in all_options:
 #   print(i.text)

#select options from dropdown without using built-in methods
for i in all_options:
    if i.text == "India":
        i.click()
        break

#we can also select all the options using xpath instead of select class

#options = driver.find_elements(By.XPATH, "//*[@id='input-country']/option") # this will also select all options
#print(len(options))


time.sleep(10)