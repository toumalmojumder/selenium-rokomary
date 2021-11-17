import pytest
import allure
from allure_commons.types import AttachmentType
from Config.config import TestData
from Pages.Login import LoginPage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Login(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)

        self.loginPage.do_Signup(TestData.FULL_NAME, TestData.PERSONAL_EMAIL, TestData.PERSONAL_PHONE, TestData.PERSONAL_PASS)
        title = self.loginPage.get_title(TestData.HOME_PAGE_TITLE)
        if title == TestData.HOME_PAGE_TITLE:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testSignupScreen",
                          attachment_type=AttachmentType.PNG)
            assert False