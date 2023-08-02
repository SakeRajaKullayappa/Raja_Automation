import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

web_driver = None


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_WebDriver(request):
    global web_driver
    if request.param == "chrome":
        ser_obj = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=ser_obj)
    elif request.param == "firefox":
        ser_obj = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=ser_obj)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
