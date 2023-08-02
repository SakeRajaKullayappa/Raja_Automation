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

links = driver.find_elements(By.XPATH, "a")
print(len(links))

time.sleep(5)
driver.quit()
