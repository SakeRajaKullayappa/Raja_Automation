import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()

driver.get("https://www.irctc.co.in/nget/booking/train-list")
driver.find_element(By.XPATH, "//div[@class='level_1 hidden-xs ng-star-inserted']//button[1]").click()

time.sleep(5)