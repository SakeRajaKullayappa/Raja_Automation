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
hyd = driver.find_element(By.XPATH, "//div[@id= 'react-autowhatever-1']//ul//li[1]//div[text() = 'HYD']")
hyd.click()

to_ele = driver.find_element(By.XPATH, "//input[@id= 'toCity']")
to_ele.send_keys("BLR")
blr= driver.find_element(By.XPATH, "//div[@id= 'react-autowhatever-1']//ul//li[1]//div[text() = 'BLR']")
blr.click()

departure=driver.find_element(By.XPATH,"//div[@aria-label='Sun Jul 30 2023']//p[text()=30]")
departure.click()

search=driver.find_element(By.XPATH,"//a[text()='Search']")
search.click()






driver.quit()
