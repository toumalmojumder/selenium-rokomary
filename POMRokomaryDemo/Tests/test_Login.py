import pytest
import allure
from allure_commons.types import AttachmentType
from Config.config import TestData
from Pages.Login import LoginPage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Login(BaseTest):

    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_Link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    @allure.severity(allure.severity_level.MINOR)
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title =  self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title ==TestData.LOGIN_PAGE_TITLE

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = self.loginPage.get_title(TestData.HOME_PAGE_TITLE)
        if title == TestData.HOME_PAGE_TITLE:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
            assert False

