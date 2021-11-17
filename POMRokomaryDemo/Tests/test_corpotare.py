import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Corporate(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_corporate(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_corporate()
        title = self.homePage.get_title(TestData.CORPORATE_PAGE_TITLE)
        assert title == TestData.CORPORATE_PAGE_TITLE