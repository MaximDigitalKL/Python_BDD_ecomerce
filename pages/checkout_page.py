import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from browser import Browser

class checkout_page(Browser):
    email = (By.ID,'customer-email')
    first_name = (By.NAME, 'firstname')
    last_name = (By.NAME, 'lastname')
    street = (By.NAME, 'street[0]')
    city = (By.NAME, 'city')
    state = (By.NAME,'region_id')
    post_code = (By.NAME,'postcode')
    country = (By.NAME,'country_id')
    phone = (By.NAME,'telephone')
    shipping_method = (By.XPATH,'//table[@class="table-checkout-shipping-method"]/tbody/tr[@class="row"][1]/td/input')
    next_button = (By.XPATH,'//button[@data-role="opc-continue"]')
    place_order_button= (By.XPATH,'//button[@class="action primary checkout"]')
    message = (By.XPATH,'//div[@class="checkout-success"]/p')
    drop_arrow = (By.XPATH, '//button[@class="action switch"]')
    sign_out_button = (By.XPATH, '//div[@class="panel header"]/ul/li[2]/div/ul/li[3]/a')

    def navigate_to_checkout_page(self):
        self.chrome.get('https://magento.softwaretestingboard.com/checkout/#shipping')

    def fill_in_details(self,email,first_name,last_name,street,city,state,post_code,country,phone):
        email_i = WebDriverWait(self.chrome, 5).until(
            EC.element_to_be_clickable((By.ID,'customer-email')))
        self.chrome.find_element(*self.email).send_keys(email)
        self.chrome.find_element(*self.first_name).send_keys(first_name)
        self.chrome.find_element(*self.last_name).send_keys(last_name)
        self.chrome.find_element(*self.street).send_keys(street)
        self.chrome.find_element(*self.city).send_keys(city)
        state_p = self.chrome.find_element(*self.state)
        select_s = Select(state_p)
        select_s.select_by_visible_text(state)
        self.chrome.find_element(*self.post_code).send_keys(post_code)
        country_p = self.chrome.find_element(*self.country)
        select_c = Select(country_p)
        select_c.select_by_visible_text(country)
        self.chrome.find_element(*self.phone).send_keys(phone)
        self.chrome.find_element(*self.shipping_method).click()
        self.chrome.find_element(*self.next_button).click()

    def fill_in_shipping_details(self):
        time.sleep(2)
        self.chrome.find_element(*self.shipping_method).click()
        self.chrome.find_element(*self.next_button).click()

    def place_order(self):
        button = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH,'//button[@class="action primary checkout"]')))
        time.sleep(2)
        button.click()

    def confirmation_message(self,confirmation_message):
        test_error = "Order was not placed"
        actual_message = self.chrome.find_element(*self.message).text
        try:
            self.chrome.find_element(*self.drop_arrow).click()
            self.chrome.find_element(*self.sign_out_button).click()
        except:
            pass
        assert confirmation_message in actual_message, test_error















