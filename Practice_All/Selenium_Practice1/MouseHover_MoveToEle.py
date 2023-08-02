import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ch_options = webdriver.ChromeOptions()
ch_options.add_argument('--Incognito')

ser_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser_obj, options=ch_options)

driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(10)

electronics = driver.find_element(By.XPATH, "//div[@class = '_1wE2Px']")


time.sleep(5)
driver.close()