from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://www.goibibo.com/")

driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()


driver.find_element(By.XPATH,"//a[text()='Trains']").click()
driver.find_element(By.XPATH,"//div[@class='styles_FswFieldItem__WiCpQ']//p[text()='Enter Source Name']").send_keys("bangalore")

driver.quit()
