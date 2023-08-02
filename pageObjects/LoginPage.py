from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class LoginPage_Nop:
    text_username_xpath = "// input[ @ id = 'Email']"
    text_password_xpath = "// input[ @ id = 'Password']"
    link_login_xpath = "// button[text() = 'Log in']"
    link_logout_xpath = "// a[text() = 'Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        uName = self.driver.find_element(By.XPATH, self.text_username_xpath)
        uName.clear()
        uName.send_keys(username)

    def setPassword(self, password):
        pwd = self.driver.find_element(By.XPATH, self.text_password_xpath)
        pwd.clear()
        pwd.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
