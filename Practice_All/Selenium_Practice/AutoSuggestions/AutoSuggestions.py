import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

service_obj = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()

driver.get("https://www.google.com/")
driver.implicitly_wait(3)

search = driver.find_element(By.XPATH, "//textarea[@type = 'search']")
time.sleep(3)
search.send_keys("selenium")
search_results = driver.find_elements(By.XPATH, "//ul[@jsname= 'bw4e9b']//li")
print(len(search_results))

for search_result in search_results:
    if "selenium download" in search_result.text:
        time.sleep(3)
        search_result.click()
        time.sleep(3)
        break


time.sleep(5)