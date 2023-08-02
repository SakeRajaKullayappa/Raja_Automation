from pageObjects.Add_Customer import Add_Customer
from pageObjects.LoginPage import LoginPage_Nop
from pageObjects.Search_Customer import Search_Customer
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName_006:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_searchCustomerByName(self, setup):
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
        self.serCust.setSearchFName("Victoria")
        self.serCust.setSearchLName("Terces")
        self.serCust.clickSearchButton()

        status = self.serCust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.driver.close()