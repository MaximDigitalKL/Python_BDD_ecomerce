from behave import *

@given('I navigate to the create account page')
def step_impl(context):
    context.sign_up_page.navigate_to_sign_up_page()

@when('I fill in the form "{first_name}","{last_name}","{email}","{password}","{confirm_password}"')
def step_impl(context,first_name,last_name,email,password,confirm_password):
    context.sign_up_page.fill_in_first_name(first_name)
    context.sign_up_page.fill_in_last_name(last_name)
    context.sign_up_page.tick_newsletter_box()
    context.sign_up_page.fill_in_email(email)
    context.sign_up_page.fill_in_password(password)
    context.sign_up_page.fill_in_confirm_password(confirm_password)
    context.sign_up_page.press_create_account_button()

@then('I receive success message "{success_message}"')
def step_impl(context,success_message):
    context.confirmation_page.check_successful_account_creation(success_message)

@when('The user fills in the form "{first_name}","{last_name}","{email}","{password}","{confirm_password}"')
def step_impl(context,first_name,last_name,email,password,confirm_password):
    context.sign_up_page.fill_in_first_name(first_name)
    context.sign_up_page.fill_in_last_name(last_name)
    context.sign_up_page.tick_newsletter_box()
    context.sign_up_page.fill_in_email(email)
    context.sign_up_page.fill_in_password(password)
    context.sign_up_page.fill_in_confirm_password(confirm_password)
    context.sign_up_page.press_create_account_button()

@then('I receive error message "{error_text}"')
def step_impl(context, error_text):
    context.sign_up_page.error_message_display(error_text)