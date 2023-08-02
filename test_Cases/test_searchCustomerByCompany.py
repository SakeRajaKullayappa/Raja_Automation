import time

from pageObjects.Add_Customer import Add_Customer
from pageObjects.LoginPage import LoginPage_Nop
from pageObjects.Search_Customer import Search_Customer
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByCompany_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_searchCustomerByCompany(self, setup):
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

        self.serCust = Search_Customer(self.driver)
        self.serCust.setSearchCompany("Indian Cricket Team")
        self.serCust.clickSearchButton()
        time.sleep(5)

        status = self.serCust.searchCustomerByCompany("Indian Cricket Team")
        assert status == True
        print("******* Search Customer By Company is Successfully Executed *******")
        self.driver.close()



