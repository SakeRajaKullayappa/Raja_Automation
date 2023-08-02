import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ch_options = webdriver.ChromeOptions()
ch_options.add_argument('--Incognito')
ch_options.add_argument('disable-geolocation')

ser_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser_obj, options=ch_options)

driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.refresh()
driver.implicitly_wait(10)

holiday_pkgs = driver.find_element(By.XPATH, "//div[@class = 'chHeaderContainer']//ul//li[4]//div//span["
                                             "normalize-space()='Holiday Packages']")
holiday_pkgs.click()

time.sleep(5)
driver.close()