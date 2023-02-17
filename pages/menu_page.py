from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from browser import Browser

class menu_page(Browser):
    what_is_new_menu = (By.ID, 'ui-id-3')
    women_menu = (By.ID, 'ui-id-4')
    men_menu = (By.ID, 'ui-id-5')
    gear_menu = (By.ID, 'ui-id-6')
    training_menu = (By.ID, 'ui-id-7')
    sale_menu = (By.ID, 'ui-id-8')
    tops_women = (By.ID, 'ui-id-9')
    bottoms_women = (By.ID, 'ui-id-10')
    jackets_women = (By.ID, 'ui-id-11')
    hoodie_s_shirts_women = (By.ID, 'ui-id-12')
    tees_women = (By.ID, 'ui-id-13')
    bras_tanks_women = (By.ID, 'ui-id-14')
    pants_women = (By.ID, 'ui-id-15')
    shorts_women = (By.ID, 'ui-id-16')
    tops_men = (By.ID, 'ui-id-17')
    bottoms_men = (By.ID, 'ui-id-18')
    jackets_men = (By.ID, 'ui-id-19')
    hoodie_s_shirts_men = (By.ID, 'ui-id-20')
    tees_men = (By.ID, 'ui-id-21')
    tanks_men = (By.ID, 'ui-id-22')
    pants_men = (By.ID, 'ui-id-23')
    shorts_men = (By.ID, 'ui-id-24')
    bags = (By.ID, 'ui-id-25')
    fitness_equipment = (By.ID, 'ui-id-26')
    watches = (By.ID, 'ui-id-27')
    video_download = (By.ID, 'ui-id-28')
    sign_in = (By.XPATH,'//li[@class="authorization-link"]/a')
    menu_item_dict = {'jackets_w': jackets_women, 'hoodies_w': hoodie_s_shirts_women, 'tees_w': tees_women, 'tanks_w': bras_tanks_women, 'pants_w': pants_women, 'shorts_w': shorts_women,
                      'jackets_m': jackets_men, 'hoodies_m': hoodie_s_shirts_men, 'tees_m': tees_men, 'tanks_m': tanks_men, 'pants_m': pants_men, 'shorts_m': shorts_men}



    def navigate_to_menu_page(self):
        self.chrome.get('https://magento.softwaretestingboard.com/')

    def select_news_pages(self,main_page_button):
        if main_page_button == 'what_is_new':
            self.chrome.find_element(*self.what_is_new_menu).click()
        elif main_page_button == 'sale':
            self.chrome.find_element(*self.sale_menu).click()
        else:
            training_menu = self.chrome.find_element(*self.training_menu)
            training_m = ActionChains(self.chrome).move_to_element(training_menu)
            training_m.perform()
            self.chrome.find_element(*self.video_download).click()

    def select_category_menu_item(self,menu_item,submenu,product_category):
        if submenu == 'Tops':
            if menu_item == 'Women':
                menu = self.chrome.find_element(*self.women_menu)
                select_menu = ActionChains(self.chrome).move_to_element(menu)
                select_menu.perform()
                submenu = self.chrome.find_element(*self.tops_women)
                select_submenu = ActionChains(self.chrome).move_to_element(submenu)
                select_submenu.perform()
            else:
                menu = self.chrome.find_element(*self.men_menu)
                select_menu = ActionChains(self.chrome).move_to_element(menu)
                select_menu.perform()
                submenu = self.chrome.find_element(*self.tops_men)
                select_submenu = ActionChains(self.chrome).move_to_element(submenu)
                select_submenu.perform()
        else:
            if menu_item == 'Women':
                menu = self.chrome.find_element(*self.women_menu)
                select_menu = ActionChains(self.chrome).move_to_element(menu)
                select_menu.perform()
                submenu = self.chrome.find_element(*self.bottoms_women)
                select_submenu = ActionChains(self.chrome).move_to_element(submenu)
                select_submenu.perform()
            else:
                menu = self.chrome.find_element(*self.men_menu)
                select_menu = ActionChains(self.chrome).move_to_element(menu)
                select_menu.perform()
                submenu = self.chrome.find_element(*self.bottoms_men)
                select_submenu = ActionChains(self.chrome).move_to_element(submenu)
                select_submenu.perform()

        for product,value in self.menu_item_dict.items():
            if product == product_category:
                self.chrome.find_element(*value).click()


    def select_additional_articles(self,article_ctg):
        if article_ctg == "bags":
            gear_menu = self.chrome.find_element(*self.gear_menu)
            gear_m = ActionChains(self.chrome).move_to_element(gear_menu)
            gear_m.perform()
            self.chrome.find_element(*self.bags).click()
        elif article_ctg == "fitness_eqp":
            gear_menu = self.chrome.find_element(*self.gear_menu)
            gear_m = ActionChains(self.chrome).move_to_element(gear_menu)
            gear_m.perform()
            self.chrome.find_element(*self.fitness_equipment).click()
        else:
            gear_menu = self.chrome.find_element(*self.gear_menu)
            gear_m = ActionChains(self.chrome).move_to_element(gear_menu)
            gear_m.perform()
            self.chrome.find_element(*self.watches).click()

    def select_sign_in_button(self):
        self.chrome.find_element(*self.sign_in).click()

