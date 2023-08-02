import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

URL = "https://www.nopcommerce.com/en/login"

service_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get(URL)

d = {
    "login": "https://www.nopcommerce.com/en/login",
    "signIn": "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",
    "login_admin": "https://www.nopcommerce.com/en/boards/topic/3803/login-as-administrator",
    "login_admin2": "https://www.nopcommerce.com/en/boards/topic/55034/admin-login",
    "open_source": "https://www.nopcommerce.com/en",
    "cant_login": "https://www.nopcommerce.com/en/boards/topic/2578/cant-login",
    "popup_login": "https://www.nopcommerce.com/en/popup-login-plugin-by-nopstation",
    "req_login": "https://www.nopcommerce.com/en/boards/topic/22294/require-login-at-first-page",
    "edit_login": "https://www.nopcommerce.com/en/boards/topic/15044/how-to-edit-login-page",
    "social_login": "https://www.nopcommerce.com/en/social-login-via-facebook-google-etc-foxnetsoftcom"
}

print("dict values are :: ", d.values())
lst = list(d.values())
print("dict values in to list are :: ", lst)

print("Parent Window Handle ID Title is :: ", driver.title)
parent_handle = driver.current_window_handle
print("Parent Window Handle ID is :: ", parent_handle)

for i in range(0, len(lst)):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i + 1])
    driver.get(lst[i])
    print("After Opened all the links in New Tab from Parent Tab :: ", driver.title)

handles = driver.window_handles
length = len(handles)
print("Length of Handles is :: ", length)
for handle in handles:
    print(handle)

if handles[length - 1] != parent_handle:
    driver.switch_to.window(handles[length - 10])
    print("After Switching from Lat window to 4 window is :: ", driver.title)