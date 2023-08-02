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

driver.get("https://www.expedia.com/")
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
time.sleep(2)

flight = driver.find_element(By.XPATH, "//div[@data-testid = 'main-region']//ul//li[2]")
flight.click()

one_way = driver.find_element(By.XPATH, "//ul[@id = 'uitk-tabs-button-container']//li[2]")
one_way.click()

leaving_from = driver.find_element(By.XPATH, "//button[@aria-label= 'Leaving from']")
# leaving_from.click()
time.sleep(3)
leaving_from.send_keys("ben")

search_results = driver.find_elements(By.XPATH, "//ul[@data-stid= 'location-field-leg1-origin-results']//li")
print(len(search_results))










time.sleep(5)
driver.close()