import pytest
import allure

from Config.config import TestData
from Pages.Home import HomePage
from Pages.Login import LoginPage

from Tests.test_base import BaseTest


@allure.severity(allure.severity_level.NORMAL)
class Test_List(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_list(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        self.homePage.go_list(TestData.LIST_TITLE, TestData.List_Description, TestData.PRODUCT)
        title = self.homePage.get_title(TestData.LIST_TITLE)
        assert title == TestData.LIST_TITLE