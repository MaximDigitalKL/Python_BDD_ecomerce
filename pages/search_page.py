from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from browser import Browser

class search_page(Browser):
    search_menu = (By.ID, 'search')
    search_result_text = (By.XPATH,'//strong/a[@href="https://magento.softwaretestingboard.com/oslo-trek-hoodie.html"]')
    items = (By.XPATH,'//li[@class="item product product-item"]')
    search_message = (By.XPATH,'//div[@class="message notice"]/div')


    def navigate_to_search_page(self):
        self.chrome.get('https://magento.softwaretestingboard.com/')

    def search_for_generic_item(self,item):
        search = self.chrome.find_element(*self.search_menu)
        search.send_keys(item)
        search.send_keys(Keys.ENTER)

    def search_for_specific_item(self,item):
        search = self.chrome.find_element(*self.search_menu)
        search.send_keys(item)
        search.send_keys(Keys.ENTER)

    def search_for_non_existing_item(self,item):
        search = self.chrome.find_element(*self.search_menu)
        search.send_keys(item)
        search.send_keys(Keys.ENTER)

    def search_result_generic(self):
        test_error = "Search function is not working as expected"
        items_list_name = self.chrome.find_elements(*self.items)
        found = True
        for item in items_list_name:
            atribut = item.get_attribute('innerHTML')
            if "Hoodie" not in atribut:
                found = False
                break
        assert found == True, test_error

    def search_result_specific(self, expected_item):
        test_error = "Search function is not working as expected"
        actual_item = self.chrome.find_element(*self.search_result_text).text
        assert expected_item == actual_item, test_error

    def search_result_non_existing(self, expected_message):
        test_error = "Search function is not working as expected"
        actual_message = self.chrome.find_element(*self.search_message).text
        assert expected_message in actual_message , test_error

