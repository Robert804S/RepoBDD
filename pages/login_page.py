from browser import Browser
from selenium.webdriver.common.by import By


class LoginPage(Browser):

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log in']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")
    ERROR = (By.XPATH, "//div[@class='message-error validation-summary-errors']")

    def navigate_to_login_page(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def error_message(self, text_error):
        error_location = self.driver.find_element(*self.ERROR).text
        assert text_error in error_location
