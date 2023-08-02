import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.makemytrip.com/")
driver.refresh()
driver.implicitly_wait(10)
flight = driver.find_element(By.XPATH, "//ul[@class = 'makeFlex font12']//li[1]")
flight.click()

from_ele = driver.find_element(By.XPATH, "//input[@id= 'fromCity']")
from_ele.send_keys("Hyd")
search_results=driver.find_elements(By.XPATH,"//div[@id='react-autowhatever-1']//ul//li")
print(len(search_results))

for elem in search_results:
    print(elem.text)
    if "hyderabad" in elem.text:
        elem.click()
        time.sleep(10)









