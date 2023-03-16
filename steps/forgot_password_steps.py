from behave import *


@when('forgot_pass: I fill in my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)


@when('forgot_pass: I click on the recover button')
def step_impl(context):
    context.forgot_password_page.click_recover_button()


@then('forgot_pass: I verify the invalid email validation message "{msg}"')
def step_impl(context, msg):
    context.forgot_password_page.verify_email_error_message(msg)


@then('forgot_pass: I verify the notification "{notify_message}"')
def step_impl(context, notify_message):
    context.forgot_password_page.verify_notification_message(notify_message)


@when('forgot_pass: I make sure the email input is cleared')
def step_impl(context):
    context.forgot_password_page.clean_email_text_field()
