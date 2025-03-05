import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="class")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestChromeBrowserInSelenium:
    url = "https://testing-and-learning-hub.vercel.app"

    def test_open_url(self, driver):
        driver.get(self.url)

    def test_page_title(self, driver):
        print(driver.title)
        assert "Testing and Learning Hub" in driver.title  # Verify page title