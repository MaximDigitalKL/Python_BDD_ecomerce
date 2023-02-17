from browser import Browser
from selenium import webdriver

class page_links(Browser):


    def link_page(self,expected_link):
        test_error = "Navigation to submenu unsuccessful"
        actual_link = self.chrome.current_url
        self.link_confirmation(expected_link,actual_link,test_error)

    def link_confirmation(self, expected_link, actual_link, test_error):
        assert expected_link == actual_link, test_error

