from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import unittest


class EdgeBrowserInSelenium(unittest.TestCase):
    url = "https://www.google.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        cls.driver.maximize_window()

    def test_open_url(self):
        self.driver.get(self.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()