import time
from selenium.webdriver.common.keys import Keys
from Config.config import TestData
from Pages.BasePages import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):

    CHANGE_INFO = (By.ID, "js--edit-personal")
    NAME = (By.XPATH,'//input[@class="form-control personal p-3 name"]')
    SAVE_BUTTON = (By.ID, "personalInfo")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.PROFILE_URL)

    def get_profile_page_title(self, title):
        return self.get_title(title)
    def do_change_info(self, name):
        self.do_click(self.CHANGE_INFO)
        self.do_send_keys(self.NAME, name)
        self.do_click(self.SAVE_BUTTON)

