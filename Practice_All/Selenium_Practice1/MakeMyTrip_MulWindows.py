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
driver.get("https://www.makemytrip.com/promos/df-mmtsuper-10092021.html?discValue=2000&couponCode=MMTSUPER")
driver.refresh()
driver.implicitly_wait(10)


# all_offers = driver.find_element(By.XPATH, "//div[@class = 'makeFlex perfectCenter']//ul//li[1]")
# all_offers.click()

parent = driver.current_window_handle
print("Parent Window Handle is :: ", parent)

# book_now = driver.find_element(By.XPATH, "//div[@class='slick-slide slick-active slick-current']//div//a["
#                                          "@class='font14 primaryText latoBlack pushRight capText'][normalize-space("
#                                          ")='BOOK NOW']")
# time.sleep(3)
# book_now.click()

BOOK_NOW = driver.find_element(By.XPATH, "//div[@class = 'smlTxt']//div//a[text() = 'Book Now']")
BOOK_NOW.click()

handles = driver.window_handles
print(len(handles))

for handle in handles:
    print(handle)

for handle in handles:
    if handle != parent:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.refresh()
time.sleep(5)

driver.close()