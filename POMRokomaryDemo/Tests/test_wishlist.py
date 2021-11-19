import pytest
import allure

from Config.config import TestData
from Pages.Home import HomePage
from Pages.Login import LoginPage

from Tests.test_base import BaseTest


@allure.severity(allure.severity_level.NORMAL)
class Test_Wish(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_wish(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        self.homePage.go_wish()
        title = self.homePage.get_title(TestData.WISH_TITLE)
        assert title == TestData.WISH_TITLE