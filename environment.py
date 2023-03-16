from browser import Browser
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.heruku_login_page import HerukuLoginPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.heruku_login_page = HerukuLoginPage()


def after_all(context):
    context.browser.close()
