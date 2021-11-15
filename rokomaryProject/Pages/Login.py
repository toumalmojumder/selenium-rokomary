from Config.config import TestData
from Pages.BasePages import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL = (By.ID, "j_username")
    PASSWORD = (By.ID, "j_password")
    EMAIL_FB = (By.ID, "email")
    PASSWORD_FB = (By.ID, "pass")
    FB_BUTTON=(By.XPATH, '//button[@name="login"]')
    LOGIN_BUTTON = (By.XPATH, '//form[@id="loginForm"] //button[@type="submit"]')
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up Now!")
    FACEBOOK_BUTTON = (By.XPATH, '//button[@class="btn btn-social-facebook"]')
    FACEBOOK_CONTINUE = (By.XPATH, '//div[@aria-label="Continue as Toumal"]')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def do_login_fb(self, username,password):
        self.do_click(self.FACEBOOK_BUTTON)
        self.do_send_keys(self.EMAIL_FB, username)
        self.do_send_keys(self.PASSWORD_FB, password)
        self.do_click(self.FB_BUTTON)





