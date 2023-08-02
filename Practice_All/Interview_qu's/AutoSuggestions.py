import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.sleep(1)

driver.get("https://www.google.com/")
driver.implicitly_wait(10)
search_box = driver.find_element(By.XPATH, "//input[@title = 'Search']")
search_box.send_keys("selenium")
time.sleep(3)
list_search_ele = driver.find_elements(By.XPATH, "//div[@class = 'OBMEnb']//ul//li")
print(len(list_search_ele))

for search_ele in list_search_ele:
    if " download" in search_ele.text:
        search_ele.click()
        time.sleep(3)
        break

time.sleep(3)
driver.close()