from Config.config import TestData
from Pages.BasePages import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)
