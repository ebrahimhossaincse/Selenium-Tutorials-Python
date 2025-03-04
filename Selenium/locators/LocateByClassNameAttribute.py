import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class LocateByClassName(unittest.TestCase):
    url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
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
        cls.driver.get(cls.url)

    def test_locate_by_id(self):
        element = self.driver.find_element(By.CLASS_NAME, "name")
        element.send_keys("Md. Ebrahim Hossain SQA Engineer")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()