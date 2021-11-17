import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Stationary(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_stationary(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_stationary()
        title = self.homePage.get_title(TestData.STATIONARY_PAGE_TITLE)
        assert title == TestData.STATIONARY_PAGE_TITLE