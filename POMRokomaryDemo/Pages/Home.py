import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Config.config import TestData
from Pages.BasePages import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    PROFILE_BUTTON=(By.XPATH, '//span[@class="user-name"]')
    MY_ACCOUNT_BUTTON=(By.XPATH, '//a[@href="/my-section/profile"]')
    MY_ORDER_BUTTON=(By.XPATH, '//a[@href="/my-section/orders"]')
    MY_LIST_BUTTON=(By.XPATH, '//a[@href="/my-section/list"]')
    CROSS_BUTTON=(By.XPATH, '//button[@class="rating-modal__close-btn js--rating-modal__close-btn"]')
    CHANGE_INFO = (By.ID, "js--edit-personal")
    NAME = (By.XPATH, '//input[@class="form-control personal p-3 name"]')
    SIGNOUT = (By.XPATH, '//a[@href="/logout"]')
    SAVE_BUTTON = (By.ID, "personalInfo")
    CART_BUTTON = (By.ID, "js-cart-menu")
    NOTIFICATION_BUTTON = (By.XPATH, '//div[@class="notification-wrapper"]')
    NOTIFICATION_VIEW_ALL = (By.XPATH, '//a[@href="/notification/view-all"]')
    BOOK_BUTTON = (By.XPATH, '//a[@href="/book?ref=nm"]')
    ELECTRIC_BUTTON = (By.XPATH, '//a[@href="/electronics?ref=nm"]')
    STATIONARY_BUTTON = (By.XPATH, '//a[@href="/stationary?ref=nm"]')
    GIFT_BUTTON = (By.XPATH, '//a[@href="/giftfinder?ref=nm"]')
    CORPORATE_BUTTON = (By.XPATH, '//a[@href="/corporate?ref=nm"]')
    OFFER_BUTTON = (By.XPATH, '//a[@href="/offer?ref=nm"]')
    BLOG_BUTTON = (By.XPATH, '//a[@href="https://blog.rokomari.com/?ref=nm"]')
    c = (By.XPATH, '//div[@id="js--exit-intent"] //button[@type="button"]')
    CREATE_NEW_LIST=(By.XPATH, '//button[@class="btn float-right"]')
    LIST_TITLE = (By.ID, "list_title")
    CUSTOM_SELECT=(By.XPATH, '//select[@class="custom-select"]')
    SELECTED_BOOK= (By.XPATH, '//option[@value="electronics"]')
    LIST_TYPE = (By.ID, "customRadioInline2")
    LIST_DESC = (By.XPATH, '//textarea [@rows="5"][@name="dtl"]')
    PRODUCT = (By.ID, "products")
    PRODUCT_DEMO = (By.ID, "ui-id-2")
    SUBMIT = (By.ID, "submit")
    SEAECH_BAR = (By.ID, "js--search")
    POINT = (By.XPATH, '//a[@href="/my-section/point"]')
    WISH = (By.XPATH, '//a[@href="/my-section/wish-list"]')
    REVIEW = (By.XPATH, '//a[@href="/my-section/reviews/not-reviewed?ref=my_review"]')



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

    def go_list(self,title, desc, product):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.MY_LIST_BUTTON)
        self.do_click(self.CREATE_NEW_LIST)
        self.do_send_keys(self.LIST_TITLE, title)
        self.do_click(self.CUSTOM_SELECT)
        self.do_click(self.SELECTED_BOOK)

        self.do_send_keys(self.LIST_DESC, desc)
        self.do_send_keys(self.PRODUCT, product)
        time.sleep(2)
        self.do_click(self.PRODUCT_DEMO)
        self.do_click(self.SUBMIT)

    def go_notification(self):
        self.do_click(self.NOTIFICATION_BUTTON)
        self.do_click(self.NOTIFICATION_VIEW_ALL)

    def do_search(self, book):
        self.do_click(self.c)
        self.do_send_keys(self.SEAECH_BAR, book)
        P_XPATH = "//p[contains(text(),'Teach Yourself ASP. NET In 21 Days')]"
        #return self.driver.find_element_by_xpath().text
        time.sleep(1)
        title = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, P_XPATH))
         )
        return title.text
    def do_signout(self):
        self.do_click(self.PROFILE_BUTTON)
        time.sleep(1)
        self.do_click(self.SIGNOUT)

    def go_point(self):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.POINT)
    def go_wish(self):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.WISH)
    def go_review(self):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.REVIEW)











