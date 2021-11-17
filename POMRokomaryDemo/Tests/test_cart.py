import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Pages.Login import LoginPage
from Tests.test_base import BaseTest


@allure.severity(allure.severity_level.NORMAL)
class Test_Cart(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_Cart()
        title = self.homePage.get_title(TestData.CART_PAGE_TITLE)
        assert title == TestData.CART_PAGE_TITLE