import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# ser_obj = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=ser_obj)

ser_obj = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=ser_obj)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()

driver.refresh()

time.sleep(5)
driver.quit()