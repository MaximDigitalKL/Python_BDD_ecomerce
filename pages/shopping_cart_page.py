import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from browser import Browser

class shopping_cart_page(Browser):
    remove_button = (By.XPATH, '//table[@id="shopping-cart-table"]/tbody[1]/tr[2]/td/div/a[2]')
    counter = (By.XPATH, '//span[@class="counter-number"]')
    edit_button = (By.XPATH, '//table[@id="shopping-cart-table"]/tbody[1]/tr[2]/td/div/a[1]')
    item_size = (By.XPATH,'//table[@id="shopping-cart-table"]/tbody[1]/tr/td/div/dl/dd[1]')
    item_colour = (By.XPATH,'//table[@id="shopping-cart-table"]/tbody[1]/tr/td/div/dl/dd[2]')
    quantity = (By.XPATH,'//table[@id="shopping-cart-table"]/tbody[1]/tr/td[3]/div/div/label/input')
    cart_items = (By.XPATH,'//tbody[@class="cart item"]')
    new_size = (By.XPATH, '//div[@id="option-label-size-143-item-166"]')
    new_colour = (By.XPATH,'//div[@id="option-label-color-93-item-49"]')
    new_quantity = (By.XPATH,'//div[@class="control"]/input[@type="number"]')
    update_cart = (By.XPATH,'//div[@class="actions"]/button[@title="Update Cart"]')
    message = (By.XPATH,'//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    check_out = (By.XPATH,'//button[@data-role="proceed-to-checkout"]')
    subtotal = (By.XPATH,'//td[@class="amount"]/span[@class="price"]')
    order_discount = (By.XPATH,'//td[@class="amount"]/span/span[@class="price"]')
    order_total = (By.XPATH,'//strong/span[@class="price"]')
    update_shopping_cart = (By.XPATH,'//button[@title="Update Shopping Cart"]')


    def navigate_to_shopping_cart(self):
        time.sleep(2)
        self.chrome.get('https://magento.softwaretestingboard.com/checkout/cart/')


    def check_cart_has_one_less_item(self):
        counter_w = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="counter-number"]')))
        time.sleep(2)
        initial = self.chrome.find_element(*self.counter).text
        self.chrome.find_element(*self.remove_button).click()
        counter_w = WebDriverWait(self.chrome, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="counter-number"]')))
        time.sleep(2)
        number = self.chrome.find_element(*self.counter).text
        assert number < initial, f"We got {number} expected {self.initial}"

    def clear_all_items(self):
        items = self.chrome.find_elements(*self.cart_items)
        for item in items:
            self.chrome.find_element(*self.remove_button).click()


    def edit_item_details(self):
        old_size = self.chrome.find_element(*self.item_size).text
        old_colour = self.chrome.find_element(*self.item_colour).text
        qty = self.chrome.find_element(*self.quantity)
        old_quantity = qty.get_attribute('value')
        self.chrome.find_element(*self.edit_button).click()
        self.chrome.find_element(*self.new_size).click()
        self.chrome.find_element(*self.new_colour).click()
        self.chrome.find_element(*self.new_quantity).clear()
        self.chrome.find_element(*self.new_quantity).send_keys(2)
        self.chrome.find_element(*self.update_cart).click()
        time.sleep(2)
        new_size = self.chrome.find_element(*self.item_size).text
        new_colour = self.chrome.find_element(*self.item_colour).text
        qty_n = self.chrome.find_element(*self.quantity)
        new_quantity = qty_n.get_attribute('value')
        assert old_size != new_size, f"Size didn't change, expected {new_size} but got {old_size}"
        assert old_colour != new_colour, f"Colour didn't change, expected {new_colour} but got {old_colour}"
        assert old_quantity != new_quantity, f"Quantity didn't change, expected {new_quantity} but got {old_quantity}"

    def update_quantity(self):
        self.chrome.find_element(*self.quantity).clear()
        self.chrome.find_element(*self.quantity).send_keys(3)
        self.chrome.find_element(*self.update_shopping_cart).click()

    def discount_is_calculated_corectly(self):
        time.sleep(2)
        order_subtotal = self.chrome.find_element(*self.subtotal).text
        if "," in order_subtotal:
            order_subtotal = order_subtotal.replace(",","")
        subtotal = order_subtotal[1:]
        order_discount = self.chrome.find_element(*self.order_discount).text
        if "," in order_discount:
            order_discount = order_discount.replace(",","")
        discount = order_discount[2:]
        order_total = self.chrome.find_element(*self.order_total).text
        if "," in order_total:
            order_total = order_total.replace(",","")
        order = order_total[1:]
        expected_discount = round(float(subtotal)*0.20,2)
        assert float(discount) == expected_discount, f"Expected discount {expected_discount}, received {discount}"
        expected_order = float(subtotal) - float(discount)
        assert expected_order == float(order), f'Order total expected {expected_order}, received {order}'









