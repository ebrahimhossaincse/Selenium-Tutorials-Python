import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class FirefoxBrowserInSelenium(unittest.TestCase):
    url = "https://www.google.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.maximize_window()

    def test_open_url(self):
        self.driver.get(self.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()