import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicity_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title_shown_on_home_page(self):
        self.selenium.get(self.live_server_url)
        assert 'Travel Wishlist' in self.selenium.title

