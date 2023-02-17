import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from browser import Browser

class sign_up_page(Browser):
    first_name = (By.ID,'firstname')
    last_name = (By.ID,'lastname')
    check_box = (By.ID,'is_subscribed')
    email = (By.ID,'email_address')
    password = (By.ID,'password')
    confirm_password = (By.ID,'password-confirmation')
    create_account = (By.XPATH,'//button[@title="Create an Account"]')
    missing_first_name = (By.ID, 'firstname-error')
    missing_last_name = (By.ID, 'lastname-error')
    missing_email = (By.ID,'email_address-error')
    missing_password = (By.ID, 'password-error')
    missing_pass_confirmation = (By.ID,'password-confirmation-error')
    invalid_first_name = (By.XPATH,'//div[@role="alert"]/div/div')
    invalid_email = (By.XPATH,'//div[@for="email_address"]')
    invalid_password = (By.XPATH,'//div[@for="password"]')
    invalid_pass_confirmation = (By.XPATH,'//div[@for="password-confirmation"]')
    error_message_list = [missing_first_name, missing_last_name, missing_email, missing_password, missing_pass_confirmation,invalid_first_name,
                          invalid_email, invalid_password,]
    drop_arrow = (By.XPATH, '//button[@class="action switch"]')
    sign_out_button = (By.XPATH, '//div[@class="panel header"]/ul/li[2]/div/ul/li[3]/a')
    Confirmation_message = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')




    def navigate_to_sign_up_page(self):
        try:
            self.chrome.find_element(*self.drop_arrow).click()
            self.chrome.find_element(*self.sign_out_button).click()
        except:
            pass
        self.chrome.get('https://magento.softwaretestingboard.com/customer/account/create/')


    def fill_in_first_name(self,first_name):
        if first_name != "N/A":
            self.chrome.find_element(*self.first_name).send_keys(first_name)

    def fill_in_last_name(self,last_name):
        if last_name != "N/A":
            self.chrome.find_element(*self.last_name).send_keys(last_name)

    def tick_newsletter_box(self):
        self.chrome.find_element(*self.check_box).click()

    def fill_in_email(self,email):
        if email != "N/A":
            self.chrome.find_element(*self.email).send_keys(email)

    def fill_in_password(self,password):
        if password != "N/A":
            self.chrome.find_element(*self.password).send_keys(password)

    def fill_in_confirm_password(self,confirm_password):
        if confirm_password != "N/A":
            self.chrome.find_element(*self.confirm_password).send_keys(confirm_password)

    def press_create_account_button(self):
        self.chrome.find_element(*self.create_account).click()


    def error_message_display(self,error_text):
        message = False
        for alert in self.error_message_list:
            try:
                actual_message = self.chrome.find_element(*alert).text
                if error_text in actual_message:
                    message = True
                    break
            except:
                pass
        try:
            if self.chrome.find_element(*self.Confirmation_message).is_displayed():
                self.chrome.find_element(*self.drop_arrow).click()
                self.chrome.find_element(*self.sign_out_button).click()
        except:
            pass
        assert message == True, f'Account created'



