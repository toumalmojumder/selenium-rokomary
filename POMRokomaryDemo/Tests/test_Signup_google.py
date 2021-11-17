import pytest
from Config.config import TestData
from Pages.Login import LoginPage
from Tests.test_base import BaseTest

class Test_Login_faceBook(BaseTest):

    def test_google_signup(self):
        self.googlesignuppage = LoginPage(self.driver)
        self.googlesignuppage.do_Signup_google(TestData.GOOGLE_USER, TestData.GOOGLE_PASS)
        title = self.googlesignuppage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE