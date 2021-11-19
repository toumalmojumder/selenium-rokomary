import pytest
import allure

from Config.config import TestData
from Pages.Home import HomePage
from Pages.Login import LoginPage

from Tests.test_base import BaseTest


@allure.severity(allure.severity_level.NORMAL)
class Test_Search(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.do_search(TestData.PRODUCT)
        assert title == TestData.PRODUCT