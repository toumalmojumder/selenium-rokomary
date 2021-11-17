import pytest

from Config.config import TestData
from Pages.Home import HomePage

from Tests.test_base import BaseTest

class TestHome(BaseTest):
    def test_login_page_title(self):
        self.homepage = HomePage(self.driver)
        title = self.homepage.get_title(TestData.HOME_PAGE_TITLE)
        assert title ==TestData.HOME_PAGE_TITLE
