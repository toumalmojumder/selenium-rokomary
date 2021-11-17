import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Gift(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_gift(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_gift()
        title = self.homePage.get_title(TestData.GIFT_PAGE_TITLE)
        assert title == TestData.GIFT_PAGE_TITLE