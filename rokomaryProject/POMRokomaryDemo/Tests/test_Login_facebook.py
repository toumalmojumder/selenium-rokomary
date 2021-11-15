import pytest
from Config.config import TestData
from Pages.Login import LoginPage
from Tests.test_base import BaseTest

class Test_Login_faceBook(BaseTest):

    def test_fb_login(self):
        self.fbloginpage = LoginPage(self.driver)
        self.fbloginpage.do_login_fb(TestData.FB_USER, TestData.FB_PASS)
        title = self.fbloginpage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
