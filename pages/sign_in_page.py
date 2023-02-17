import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from browser import Browser

class sign_in_page(Browser):
    log_email = (By.XPATH, '//input[@name="login[username]"]')
    password = (By.XPATH,'//input[@name="login[password]"]')
    sign_in_button =(By.XPATH,'//button[@id="send2"]')

    def log_in(self,log_email,password):
        button = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH,'//button[@id="send2"]')))
        self.chrome.find_element(*self.log_email).send_keys(log_email)
        self.chrome.find_element(*self.password).send_keys(password)
        self.chrome.find_element(*self.sign_in_button).click()
        time.sleep(2)

