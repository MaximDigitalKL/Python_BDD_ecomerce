from behave import *

@given('I navigate to search page')
def step_impl(context):
    context.search_page.navigate_to_search_page()

@when('I search for generic item "{item}"')
def step_impl(context,item):
    context.search_page.search_for_generic_item(item)

@Then('I receive a list of items')
def step_impl(context):
    context.search_page.search_result_generic()

@when('I search for specific item "{item}"')
def step_impl(context,item):
    context.search_page.search_for_specific_item(item)

@Then('First item in result list is "{expected_item}"')
def step_impl(context,expected_item):
    context.search_page.search_result_specific(expected_item)

@when('I search for non existing item "{item}"')
def step_impl(context,item):
    context.search_page.search_for_non_existing_item(item)

@Then('I receive appropriate error message "{expected_message}"')
def step_impl(context,expected_message):
    context.search_page.search_result_non_existing(expected_message)