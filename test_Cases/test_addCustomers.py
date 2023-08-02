import random
import string
import time

from selenium.webdriver.common.by import By

from pageObjects.Add_Customer import Add_Customer
from pageObjects.LoginPage import LoginPage_Nop
from utilities.readProperties import ReadConfig


class Test_003_addCustomers:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.maximize_window()

        self.driver.get(self.baseURL)
        self.lp = LoginPage_Nop(self.driver)

        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addCust = Add_Customer(self.driver)
        self.addCust.clickCustomers_menu()
        self.addCust.clickCustomers_submenu()
        self.addCust.clickAdd_new()

        self.email = random_Generator(self) + "@gmail.com"

        self.addCust.setEmail(self.email)
        self.addCust.setPassword("Raja@9515522116")
        self.addCust.setFName("Raja")
        self.addCust.setLName("Sake")
        self.addCust.clickGender_Male("Male")
        self.addCust.setDOB("5/02/2000")
        self.addCust.setCompanyName("Sony India Pvt Ltd")
        self.addCust.clickIsTaxExempt()
        self.addCust.setCustomerRole("Guests")
        self.addCust.selectManagerOfVendor("Vendor 1")
        time.sleep(2)
        self.addCust.setAdminContext(".......This is for Testing......")
        self.addCust.clickSave()

        self.success_msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.success_msg)

        if "customer has been added successfully." in self.success_msg:
            assert True == True
            self.driver.save_screenshot(".\\ScreenShots\\" + "addCustomer_success.png")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "addCustomer1.png")
            assert True == False

        self.driver.close()


def random_Generator(self, size=8, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size + 1))
