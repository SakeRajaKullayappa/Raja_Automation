import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--Incognito")

ser_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(10)

driver.refresh()
time.sleep(2)

drp_ele = driver.find_element(By.XPATH, "//div[@data-cy= 'LanguageSwitcherWidget']")
drp_ele.click()
time.sleep(3)

drp_ele_country = driver.find_element(By.XPATH, "//div[@class= 'selectConWrap']")
drp_ele_country.click()
time.sleep(3)

drp_ele_country_list = driver.find_element(By.XPATH, "//div[@data-cy= 'countryList']//p[2][text() = 'UAE']")
drp_ele_country_list.click()
time.sleep(3)

driver.save_screenshot("Practice_All/Selenium/Drop_Down" + "UAE_Country.png")
time.sleep(3)

rd_button = driver.find_element(By.XPATH, "//label[@for='araLang']")
rd_button.click()
time.sleep(2)

driver.quit()

