import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePages import BasePage


class HomePage(BasePage):

    PROFILE_BUTTON=(By.XPATH, '//span[@class="user-name"]')
    MY_ACCOUNT_BUTTON=(By.XPATH, '//a[@href="/my-section/profile"]')
    MY_ORDER_BUTTON=(By.XPATH, '//a[@href="/my-section/orders"]')
    CROSS_BUTTON=(By.XPATH, '//button[@class="rating-modal__close-btn js--rating-modal__close-btn"]')
    CHANGE_INFO = (By.ID, "js--edit-personal")
    NAME = (By.XPATH, '//input[@class="form-control personal p-3 name"]')
    SAVE_BUTTON = (By.ID, "personalInfo")
    CART_BUTTON = (By.ID, "js-cart-menu")
    BOOK_BUTTON = (By.XPATH, '//a[@href="/book?ref=nm"]')
    ELECTRIC_BUTTON = (By.XPATH, '//a[@href="/electronics?ref=nm"]')
    STATIONARY_BUTTON = (By.XPATH, '//a[@href="/stationary?ref=nm"]')
    GIFT_BUTTON = (By.XPATH, '//a[@href="/giftfinder?ref=nm"]')
    CORPORATE_BUTTON = (By.XPATH, '//a[@href="/corporate?ref=nm"]')
    OFFER_BUTTON = (By.XPATH, '//a[@href="/offer?ref=nm"]')
    BLOG_BUTTON = (By.XPATH, '//a[@href="https://blog.rokomari.com/?ref=nm"]')
    c = (By.XPATH, '//div[@id="js--exit-intent"] //button[@type="button"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def go_Profile(self, name):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.MY_ACCOUNT_BUTTON)
        time.sleep(1)
        self.do_click(self.CHANGE_INFO)
        self.driver.find_element_by_xpath('//input[@class="form-control personal p-3 name"]').clear()
        self.do_send_keys(self.NAME, name)
        self.do_click(self.SAVE_BUTTON)

    def go_Order(self):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.MY_ORDER_BUTTON)

    def go_Cart(self):
        self.do_click(self.CART_BUTTON)

    def go_Book(self):
        self.do_click(self.c)
        self.do_click(self.BOOK_BUTTON)

    def go_Electronic(self):
        self.do_click(self.c)
        self.do_click(self.ELECTRIC_BUTTON)

    def go_stationary(self):
        self.do_click(self.c)
        self.do_click(self.STATIONARY_BUTTON)

    def go_gift(self):
        self.do_click(self.c)
        self.do_click(self.GIFT_BUTTON)

    def go_corporate(self):
        self.do_click(self.c)
        self.do_click(self.CORPORATE_BUTTON)

    def go_offer(self):
        self.do_click(self.c)
        self.do_click(self.OFFER_BUTTON)

    def go_blog(self):
        self.do_click(self.c)
        self.do_click(self.BLOG_BUTTON)