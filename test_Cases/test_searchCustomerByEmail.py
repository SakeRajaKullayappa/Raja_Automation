import time

from pageObjects.Add_Customer import Add_Customer
from pageObjects.LoginPage import LoginPage_Nop
from pageObjects.Search_Customer import Search_Customer
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_searchCustomerByEmail(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage_Nop(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addCust = Add_Customer(self.driver)
        self.addCust.clickCustomers_menu()
        self.addCust.clickCustomers_submenu()

        self.searchCust = Search_Customer(self.driver)
        self.searchCust.setSearchEmai("nqeeagu@gmail.com")
        self.searchCust.clickSearchButton()
        time.sleep(5)

        status = self.searchCust.searchCustomerByEmail("nqeeagu@gmail.com")
        assert True == status
        print("***** Customer Search By Email is Success ******")
        self.driver.close()
