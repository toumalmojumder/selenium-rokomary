import pytest
from Config.config import TestData
from Pages.Login import LoginPage
from Tests.test_base import BaseTest

class Test_Login_faceBook(BaseTest):

    def test_google_login(self):
        self.googleloginpage = LoginPage(self.driver)
        self.googleloginpage.do_login_google(TestData.GOOGLE_USER, TestData.GOOGLE_PASS)
        title = self.googleloginpage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE