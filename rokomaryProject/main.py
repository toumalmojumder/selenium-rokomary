import time
import unittest
from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rokomari.com/book")
driver.close()


