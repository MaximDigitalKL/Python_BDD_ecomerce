from pages.menu_page import menu_page
from browser import Browser
from pages.link_pages import page_links
from pages.search_page import search_page
from pages.shopping_cart_page import shopping_cart_page
from pages.items_page import items_page
from pages.sign_up_page import sign_up_page
from pages.confirmation_page import Confirmation_page
from pages.checkout_page import checkout_page
from pages.sign_in_page import sign_in_page

def before_all(context):
    context.menu_page = menu_page()
    context.browser = Browser()
    context.link_pages = page_links()
    context.search_page = search_page()
    context.shopping_cart_page = shopping_cart_page()
    context.items_page = items_page()
    context.sign_up_page = sign_up_page()
    context.confirmation_page = Confirmation_page()
    context.checkout_page = checkout_page()
    context.sign_in_page = sign_in_page()




def after_all(context):
    context.browser.close()
