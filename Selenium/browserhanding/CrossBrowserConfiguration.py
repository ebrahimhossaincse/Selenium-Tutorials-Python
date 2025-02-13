import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class CrossBrowserConfiguration(unittest.TestCase):
    url = "https://www.google.com/"
    driver = None
    browser_name = "chrome"

    @classmethod
    def setUpClass(cls):
        if cls.browser_name == "chrome":
            cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif cls.browser_name == "firefox":
            cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif cls.browser_name == "edge":
            cls.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError("Browser is not supported")
        cls.driver.maximize_window()

    def test_open_url(self):
        self.driver.get(self.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()