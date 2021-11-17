import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Electronic(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_electronic(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_Electronic()
        title = self.homePage.get_title(TestData.ELECTRONIC_PAGE_TITLE)
        assert title == TestData.ELECTRONIC_PAGE_TITLE