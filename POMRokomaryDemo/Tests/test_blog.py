import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Blog(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_blog(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_blog()
        title = self.homePage.get_title(TestData.BLOG_PAGE_TITLE)
        assert title == TestData.BLOG_PAGE_TITLE