import time
from selenium.webdriver.common.keys import Keys
from Config.config import TestData
from Pages.BasePages import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    EMAIL = (By.ID, "j_username")
    PASSWORD = (By.ID, "j_password")
    EMAIL_FB = (By.ID, "email")
    PASSWORD_FB = (By.ID, "pass")
    FB_BUTTON=(By.XPATH, '//button[@name="login"]')
    LOGIN_BUTTON = (By.XPATH, '//form[@id="loginForm"] //button[@type="submit"]')
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up Now!")
    FACEBOOK_BUTTON = (By.XPATH, '//button[@class="btn btn-social-facebook"]')
    FACEBOOK_SIGNUP_BUTTON = (By.XPATH, '//div[@class="registration-form show"] //button[@class="btn btn-social-facebook"]')

    FACEBOOK_CONTINUE = (By.XPATH, '//div[@aria-label="Continue as Toumal"]')
    EMAIL_GOOGLE = (By.XPATH, '//input[@type="email"]')
    PASSWORD_GOOGLE = (By.XPATH, '//input[@type="password"]')
    GOOGLE_BUTTON = (By.XPATH, '//button[@class="btn btn-social-google"]')
    GOOGLE_SIGNUP_BUTTON = (By.XPATH, '//div[@class="registration-form show"] //button[@class="btn btn-social-google"]')
    SIGNUP_NOW_BUTTON=(By.XPATH, '//a[@href="/registration"]')

    GOOGLE_NEXT = (By.ID, "identifierNext")

    FULL_NAME = (By.ID, "nm")
    PERSONAL_EMAIL=(By.ID, "js-email")
    PERSONAL_PHONE=(By.ID, "js-phone")
    PERSONAL_PASS=(By.ID, "pwd")
    ROBOT_CHK=(By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
    CREATE_ACCOUNT=(By.XPATH, '//form [@id="accountForm"] //button[@type="submit"]')
    PROFILE_BUTTON=(By.ID, "dropdownMenu2")
    MY_ACCOUNT_BUTTON=(By.XPATH, '//a[@href="/my-section/profile"]')
    CROSS_BUTTON=(By.XPATH, '//button[@class="rating-modal__close-btn js--rating-modal__close-btn"]')

    CHANGE_INFO = (By.ID, "js--edit-personal")
    NAME = (By.XPATH, '//input[@class="form-control personal p-3 name"]')
    SAVE_BUTTON = (By.ID, "personalInfo")

    HOME_POINT = (By.XPATH, '//header')
    C = (By.ID, "js--overlay")

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



    def do_Signup(self, name, Email, phone, password):
        self.do_click(self.SIGNUP_NOW_BUTTON)
        self.do_send_keys(self.FULL_NAME, name)
        self.do_send_keys(self.PERSONAL_EMAIL, Email)
        self.do_send_keys(self.PERSONAL_PHONE, phone)
        self.do_send_keys(self.PERSONAL_PASS,password)
        #self.do_click(self.ROBOT_CHK)
        time.sleep(5)
        self.do_click(self.CREATE_ACCOUNT)
        time.sleep(10)


    def do_login_fb(self, username,password):
        self.do_click(self.FACEBOOK_BUTTON)
        self.do_send_keys(self.EMAIL_FB, username)
        self.do_send_keys(self.PASSWORD_FB, password)
        self.do_click(self.FB_BUTTON)

    def do_login_google(self, username,password):
        self.do_click(self.GOOGLE_BUTTON)
        time.sleep(2)
        self.do_send_keys(self.EMAIL_GOOGLE, username)
        self.do_send_keys(self.EMAIL_GOOGLE, Keys.ENTER )
        time.sleep(2)
        self.do_send_keys(self.PASSWORD_GOOGLE, password)
        self.do_send_keys(self.PASSWORD_GOOGLE, Keys.ENTER)
        time.sleep(2)

    def do_signup_fb(self, username, password):
        self.do_click(self.SIGNUP_NOW_BUTTON)
        time.sleep(1)
        self.do_click(self.FACEBOOK_SIGNUP_BUTTON)
        self.do_send_keys(self.EMAIL_FB, username)
        self.do_send_keys(self.PASSWORD_FB, password)
        self.do_click(self.FB_BUTTON)

    def do_Signup_google(self, username, password):
        self.do_click(self.SIGNUP_NOW_BUTTON)
        self.do_click(self.GOOGLE_SIGNUP_BUTTON)
        time.sleep(1)
        self.do_send_keys(self.EMAIL_GOOGLE, username)
        self.do_click(self.GOOGLE_NEXT)
        time.sleep(1)
        self.do_send_keys(self.PASSWORD_GOOGLE, password)
        self.do_click(self.GOOGLE_NEXT)
    def go_Profile(self, name):
        self.do_click(self.CROSS_BUTTON)
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.MY_ACCOUNT_BUTTON)
        time.sleep(1)
        self.do_click(self.CHANGE_INFO)
        self.driver.find_element_by_xpath('//input[@class="form-control personal p-3 name"]').clear()
        self.do_send_keys(self.NAME, name)
        self.do_click(self.SAVE_BUTTON)






