import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Book(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_Book()
        title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE