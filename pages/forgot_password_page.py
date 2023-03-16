from selenium.common import NoSuchElementException

from browser import Browser
from selenium.webdriver.common.by import By


class ForgotPasswordPage(Browser):
    EMAIL_INPUT = (By.ID, "Email")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Recover']")
    EMAIL_ERROR_MESSAGE = (By.ID, "Email-error")
    NOTIFICATION_MESSAGE = (By.XPATH, "//p[@class='content']")

    def navigate_to_forgot_password_page(self):
        self.driver.get("https://demo.nopcommerce.com/passwordrecovery")

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_recover_button(self):
        self.driver.find_element(*self.RECOVERY_BUTTON).click()

    def verify_email_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"  # nu s-a afisat elementul

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def verify_notification_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"  # nu s-a afisat elementul

        assert actual_message == expected_message, f'Error, the message is incorrect'
