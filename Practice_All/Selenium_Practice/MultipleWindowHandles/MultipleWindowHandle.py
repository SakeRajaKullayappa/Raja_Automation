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

driver.get("https://www.yatra.com/")
time.sleep(2)

parent_handle = driver.current_window_handle
print(parent_handle)

offers = driver.find_element(By.XPATH, "//li[@class = 'list-dropdown ytHeaderOffers']")
offers.click()
time.sleep(2)

list_offers = driver.find_elements(By.XPATH, "//div[@class= 'offer_DealsContainer']//ul//li")
print("count of offers list is :: ", len(list_offers))

for i in range(1, 7):
    list_offers[i].click()

child_handles = driver.window_handles
print("count of child handles are :: ", len(child_handles))

for child_handle in child_handles:
    print(child_handle)
    if child_handle != parent_handle:
        for j in range(len(child_handle), len(child_handles) + 1):
            driver.switch_to.window(child_handle[j])
            time.sleep(2)
            print("Successfully switched to last window")


time.sleep(5)
driver.close()