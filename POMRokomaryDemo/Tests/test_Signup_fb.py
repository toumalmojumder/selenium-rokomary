import pytest
from Config.config import TestData
from Pages.Login import LoginPage
from Tests.test_base import BaseTest

class Test_Signup_faceBook(BaseTest):

    def test_fb_signup(self):
        self.fbsignuppage = LoginPage(self.driver)
        self.fbsignuppage.do_signup_fb(TestData.FB_USER, TestData.FB_PASS)
        title = self.fbsignuppage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
