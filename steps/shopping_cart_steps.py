from behave import *

@given('Navigate to items page')
def step_impl(context):
    context.items_page.navigate_to_item()

@when('We add one item to shopping cart')
def step_impl(context):
    context.items_page.add_one_item()

@then('Count of items in shopping cart is one')
def step_impl(context):
    context.items_page.check_one_item_in_cart()
    context.shopping_cart_page.navigate_to_shopping_cart()
    context.shopping_cart_page.clear_all_items()

@when('I add multiple items to shopping cart')
def step_impl(context):
    context.items_page.add_multiple_items()

@then('There are multiple items in shopping cart')
def step_impl(context):
    context.items_page.check_multiple_items_in_cart()
    context.shopping_cart_page.navigate_to_shopping_cart()
    context.shopping_cart_page.clear_all_items()

@when('I change my mind regarding an item, I navigate to shopping cart page')
def step_impl(context):
    context.shopping_cart_page.navigate_to_shopping_cart()

@then('I edit one item details')
def step_impl(context):
    context.shopping_cart_page.edit_item_details()
    context.shopping_cart_page.clear_all_items()


@then('I remove one item from the shopping cart and shopping cart  displays one less item')
def step_impl(context):
    context.shopping_cart_page.check_cart_has_one_less_item()
    context.shopping_cart_page.clear_all_items()
