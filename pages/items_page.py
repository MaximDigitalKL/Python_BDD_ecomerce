import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from browser import Browser

class items_page(Browser):
    counter = (By.XPATH,'//span[@class="counter-number"]')
    tee_one = (By.XPATH,'//ol[@class="products list items product-items"]/li[1]')
    tee_one_size = (By.XPATH,
                    '//ol[@class="products list items product-items"]/li[1]/div/div/div[3]/div/div/div[@id="option-label-size-143-item-168"]')
    tee_one_colour = (By.XPATH,
                      '//ol[@class="products list items product-items"]/li[1]/div/div/div[3]/div[2]/div/div[@id="option-label-color-93-item-50"]')
    tee_one_add = (By.XPATH,'//ol/li[1]/div/div/div[4]/div/div/form/button')
    tee_two = (By.XPATH,'//ol[@class="products list items product-items"]/li[2]')
    tee_two_size = (By.XPATH,
                    '//ol[@class="products list items product-items"]/li[2]/div/div/div[3]/div/div/div[@id="option-label-size-143-item-168"]')
    tee_two_colour = (By.XPATH,
                      '//ol[@class="products list items product-items"]/li[2]/div/div/div[3]/div[2]/div/div[@id="option-label-color-93-item-53"]')
    tee_two_add = (By.XPATH,'//ol/li[2]/div/div/div[4]/div/div/form/button')
    tee_three = (By.XPATH, '//ol[@class="products list items product-items"]/li[3]')
    tee_three_size = (By.XPATH,
                    '//ol[@class="products list items product-items"]/li[3]/div/div/div[3]/div/div/div[@id="option-label-size-143-item-168"]')
    tee_three_colour = (By.XPATH,
                      '//ol[@class="products list items product-items"]/li[3]/div/div/div[3]/div[2]/div/div[@id="option-label-color-93-item-50"]')
    tee_three_add = (By.XPATH, '//ol/li[3]/div/div/div[4]/div/div/form/button')

    shopping_cart = (By.XPATH,'//a[@class="action showcart"]')
    proceed_button = (By.ID, 'top-cart-btn-checkout')





    def navigate_to_item(self):
        self.chrome.get('https://magento.softwaretestingboard.com/men/tops-men/tees-men.html')

    def add_one_item(self):
        one_tee = self.chrome.find_element(*self.tee_one)
        element = ActionChains(self.chrome).move_to_element(one_tee)
        element.perform()
        self.chrome.find_element(*self.tee_one_size).click()
        self.chrome.find_element(*self.tee_one_colour).click()
        self.chrome.find_element(*self.tee_one_add).click()



    def check_one_item_in_cart(self):
        counter_w = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="counter-number"]')))
        time.sleep(3)
        number = self.chrome.find_element(*self.counter).text
        assert number == "1", f"We got {number} expected 1"

    def add_multiple_items(self):
        one_tee = self.chrome.find_element(*self.tee_one)
        element = ActionChains(self.chrome).move_to_element(one_tee)
        element.perform()
        self.chrome.find_element(*self.tee_one_size).click()
        self.chrome.find_element(*self.tee_one_colour).click()
        self.chrome.find_element(*self.tee_one_add).click()
        time.sleep(2)
        two_tee = self.chrome.find_element(*self.tee_two)
        element = ActionChains(self.chrome).move_to_element(two_tee)
        element.perform()
        self.chrome.find_element(*self.tee_two_size).click()
        self.chrome.find_element(*self.tee_two_colour).click()
        self.chrome.find_element(*self.tee_two_add).click()
        time.sleep(2)
        three_tee = self.chrome.find_element(*self.tee_two)
        element = ActionChains(self.chrome).move_to_element(three_tee)
        element.perform()
        self.chrome.find_element(*self.tee_three_size).click()
        self.chrome.find_element(*self.tee_three_colour).click()
        self.chrome.find_element(*self.tee_three_add).click()
        time.sleep(2)



    def check_multiple_items_in_cart(self):
        counter_w = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="counter-number"]')))
        time.sleep(2)
        number = self.chrome.find_element(*self.counter).text
        assert int(number) > 1, f"We got {number} expected 3"

    def proceed_to_checkout(self):
        counter_w = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="counter-number"]')))
        time.sleep(2)
        self.chrome.find_element(*self.shopping_cart).click()
        self.chrome.find_element(*self.proceed_button).click()


