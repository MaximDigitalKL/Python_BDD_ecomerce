from behave import *

@given("I navigate to the menu page")
def step_impl(context):
    context.menu_page.navigate_to_menu_page()

@Then('I am redirected to new page "{expected_link}"')
def step_impl(context,expected_link):
    context.link_pages.link_page(expected_link)

# #---------------------------------------------NEWS--------------------------------------------------------------

@when('User selects the "{main_page_button}" button')
def step_impl(context,main_page_button):
    context.menu_page.select_news_pages(main_page_button)

# #--------------------------------------------WOMEN/MEN--------------------------------------------------------------------

@when('I select the "{menu_item}" "{submenu}" "{product_category}" button')
def step_impl(context,menu_item,submenu,product_category):
    context.menu_page.select_category_menu_item(menu_item,submenu,product_category)

#----------------------------------------------------------Additional_Categories-----------------------------------------------------

@when('User decides to look for "{article_ctg}"')
def step_impl(context,article_ctg):
    context.menu_page.select_additional_articles(article_ctg)
