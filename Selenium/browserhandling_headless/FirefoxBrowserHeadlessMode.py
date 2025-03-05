import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestFirefoxBrowserInSelenium:
    url = "https://testing-and-learning-hub.vercel.app/"

    def test_open_url(self, driver):
        driver.get(self.url)
        assert driver.current_url == self.url  # Optional assertion to verify navigation
