import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    browser_name = "chrome"
    url = "https://testing-and-learning-hub.vercel.app/Selenium/pages/registration_form.html"

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Browser is not supported")

    driver.maximize_window()
    driver.get(url)

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLocateByAndExpressionXPath:
    def test_locate_by_and_expression_xpath(self):
        element = self.driver.find_element(By.XPATH, "//*[contains(@id,'mobile') and @placeholder='Enter your mobile number']")
        element.send_keys("01886644261")
        time.sleep(3)