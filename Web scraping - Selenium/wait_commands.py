from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


s = Service(r'C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10) #it is written at the start...it will work and applicable for all the code  until the process is killed

driver.get("https://www.google.com/")

search_box  = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
search_box.send_keys('Selenium')
search_box.submit()

#explixit wait commands...we have used them in earlier python files(assignment_1.py....), check those..

wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
search_link = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))
search_link.click()


