import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
chrome.maximize_window()
chrome.get('https://magento.softwaretestingboard.com/customer/account/create/')
chrome.implicitly_wait(4)
chrome.find_element(By.ID,'firstname').send_keys('test1')
chrome.find_element(By.ID,'lastname').send_keys('test2')
chrome.find_element(By.ID,'email_address').send_keys('mamalui2@asd.io')
chrome.find_element(By.ID,'password').send_keys('Qwert1234')
chrome.find_element(By.ID,'password-confirmation').send_keys('Qwert1234')
chrome.find_element(By.XPATH,'//button[@title="Create an Account"]').click()
mesaj = chrome.title
print(mesaj)




