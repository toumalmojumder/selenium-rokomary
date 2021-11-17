import pytest
import allure
from Config.config import TestData
from Pages.Home import HomePage
from Tests.test_base import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Offer(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_offer(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_offer()
        title = self.homePage.get_title(TestData.OFFER_PAGE_TITLE)
        assert title == TestData.OFFER_PAGE_TITLE