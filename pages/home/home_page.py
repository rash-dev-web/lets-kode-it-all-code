from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # locators
    _sign_in_link = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def get_sign_in_link(self):
        return self.driver.find_element(By.XPATH, self._sign_in_link)

    def get_email_field(self):
        return self.driver.find_element(By.ID, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.ID, self._password_field)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def click_sign_in_link(self):
        self.get_sign_in_link().click()

    def enter_email(self, email):
        self.get_email_field().send_keys(email)

    def enter_password(self, pwd):
        self.get_password_field().send_keys(pwd)

    def click_login_button(self):
        self.get_login_button().click()

    def login(self, email, passwd):
        self.click_sign_in_link()
        self.enter_email(email)
        self.enter_password(passwd)
        self.click_login_button()
