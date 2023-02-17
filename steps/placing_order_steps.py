from behave import *

@Given('The user navigates to main page')
def step_impl(context):
    context.menu_page.navigate_to_menu_page()

@When('The user logs into his account email "{log_email}" password "{password}"')
def step_impl(context,log_email,password):
    context.menu_page.select_sign_in_button()
    context.sign_in_page.log_in(log_email,password)

@When('He searches for a desired item "{item}"')
def step_impl(context,item):
    context.search_page.search_for_specific_item(item)

@When('He adds the item to the shopping cart')
def step_impl(context):
    context.items_page.add_one_item()

@When('He proceeds to checkout')
def step_impl(context):
    context.items_page.proceed_to_checkout()

@When('He fills in all the required details "{email}","{first_name}","{last_name}","{street}","{city}","{state}","{post_code}","{country}","{phone}"')
def step_impl(context,email,first_name,last_name,street,city,state,post_code,country,phone):
    context.checkout_page.fill_in_details(email,first_name,last_name,street,city,state,post_code,country,phone)

@When('He fills in the shipping details')
def step_impl(context,):
    context.checkout_page.fill_in_shipping_details()

@When('He places the order')
def step_impl(context):
    context.checkout_page.place_order()

@Then('The order is placed, success message "{confirmation_message}"')
def step_impl(context,confirmation_message):
    context.checkout_page.confirmation_message(confirmation_message)

@When('He edits the quantity of the item')
def step_impl(context):
    context.shopping_cart_page.navigate_to_shopping_cart()
    context.shopping_cart_page.update_quantity()

@Then('The discount is correctly calculated')
def step_impl(context):
    context.shopping_cart_page.discount_is_calculated_corectly()
    context.shopping_cart_page.clear_all_items()