from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Confirmation_page(Browser):

    def check_successful_account_creation(self, success_message):
        test_error = "Account was not created"
        actual_message = self.chrome.title
        assert success_message in actual_message, f'Expected {success_message}, received {actual_message}'