import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--Incognito")

ser_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(10)
driver.refresh()

ele = driver.find_element(By.XPATH, "we need to provide xpath")
ele.click()
time.sleep(5)

alert = driver.switch_to.alert
alert.accept()
# alert.dismiss()
driver.quit()
