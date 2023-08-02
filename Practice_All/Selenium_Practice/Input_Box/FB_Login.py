import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

service_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
time.sleep(2)
# uName = driver.find_element(By.ID, "email")
# print("is_displayed Status for UName:: ", uName.is_displayed())
# print("is_enabled Status for UName:: ", uName.is_enabled())
# uName.send_keys("rajasake1995@gmail.com")
#
# pwd = driver.find_element(By.ID, "pass")
# print("is_displayed Status for pwd:: ", pwd.is_displayed())
# print("is_enabled Status for pwd:: ", pwd.is_enabled())
# pwd.send_keys("Raja@15031995")
#
# login = driver.find_element(By.ID, "loginbutton")
# login.click()

forgot_pwd = driver.find_element(By.XPATH, "//a[text()= 'Forgotten account?']")
forgot_pwd.click()

identify_UName = driver.find_element(By.XPATH, "//input[@id= 'identify_email']")
identify_UName.send_keys("9515522115")

search_button = driver.find_element(By.XPATH, "//button[@id= 'did_submit']")
search_button.click()

# continue_button = driver.find_element(By.XPATH, "//button[@type= 'submit']")
# continue_button.click()
time.sleep(2)

try_another_way = driver.find_element(By.XPATH, "//div[@class = 'clearfix']//div//a[@role= 'button']")
try_another_way.click()

time.sleep(5)
driver.close()