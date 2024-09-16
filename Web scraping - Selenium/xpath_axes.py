from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service(r"C:\Users\Home\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://money.rediff.com/gainers/bse/daily/groupa')
driver.maximize_window()

#self
#text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'IIFL Finance')]/self::a").text
#print(text_msg)

#parent
#text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'IIFL Finance')]/parent::td").text
#print(text_msg)

#child
#child_nodes= driver.find_elements(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr/child::td")
#print(len(child_nodes))

#ancestor
text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr").text
print(text_msg)

#descendant
descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr/descendant::*")
print(len(descendants))

#following
following = driver.find_elements(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr/following::*")
print(len(following))

#following-siblings
following_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr/following-sibling::*") #* denotes all
print(len(following_sibling))

#preceding
precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr/preceding::tr")
print(len(precedings))

#preceding-sibling
preceding_siblings = driver.find_elements(By.XPATH, "//a[contains(text(),'IIFL Finance')]/ancestor::tr/preceding-sibling::*")
print(len(preceding_siblings))

