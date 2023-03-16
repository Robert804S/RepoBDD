from behave import *


@given('login: I am a user on the HerukuApp login page')
def step_impl(context):
    context.heruku_login_page.navigate_to_login_page()


@when('login: I check the username field')
def step_impl(context):
    context.heruku_login_page.sa_contina_user()


@when('login: I check the password field')
def step_impl(context):
    context.heruku_login_page.sa_contina_pass()


@when('login: I check the login button to be displayed and enabled')
def step_impl(context):
    context.heruku_login_page.login_btn()


@then('login: I log in successfully with "{user}" and "{password}"')
def step_impl(context, user, password):
    context.heruku_login_page.login_in_account(user, password)
