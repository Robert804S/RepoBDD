from browser import Browser
from selenium.webdriver.common.by import By


class HerukuLoginPage(Browser):

    USERNAME = (By.XPATH, "//label[@for='username']")
    PASSWORD = (By.XPATH, "//label[@for='password']")
    LOGIN_BUTTON = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
    USER_FIELD = (By.XPATH, "//input[@id='username']")
    PASS_FIELD = (By.XPATH, "//input[@id='password']")

    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def sa_contina_user(self):
        username_text = self.driver.find_element(*self.USERNAME).text
        expected_text = "Username"
        assert username_text == expected_text
        print(f"Elementul contine textul {expected_text}")

    def sa_contina_pass(self):
        username_text = self.driver.find_element(*self.PASSWORD).text
        expected_text = "Password"
        assert username_text == expected_text
        print(f"Elementul contine textul {expected_text}")

    def login_btn(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.is_displayed()
        login_button.is_enabled()
        print(f'Login_button este vizibil - {login_button.is_displayed()}')
        print(f'Pe Login_button se poate da click - {login_button.is_enabled()}')

    def login_in_account(self, user, password):
        self.driver.find_element(*self.USER_FIELD).send_keys(user)
        self.driver.find_element(*self.PASS_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

        actual_url = self.driver.current_url
        expected_url = "https://the-internet.herokuapp.com/secure"
        assert actual_url == expected_url
        print("Url-ul paginii este cel asteptat!")