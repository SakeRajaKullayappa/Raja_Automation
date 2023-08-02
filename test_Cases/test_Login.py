from pageObjects.LoginPage import LoginPage_Nop
from utilities.readProperties import ReadConfig
from utilities.customLogger import GenLogs


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    exp_homepage_title = ReadConfig.exp_homepage_title()
    exp_loginPage_title = ReadConfig.exp_loginPage_title()

    logger = GenLogs.logGen()

    def test_homePageTitle(self, setup):
        self.logger.info("====== Test_001_Login ======")
        self.logger.info("====== Verifying test_homePageTitle ======")

        self.driver = setup
        self.driver.get(self.baseURL)

        act_homepage_title = self.driver.title

        if act_homepage_title == self.exp_homepage_title:
            assert True
            self.logger.info("****** test_homePageTitle is Passed ******")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.logger.info("****** test_homePageTitle is Failed ******")
            assert False

        self.driver.close()

    def test_login(self, setup):
        self.logger.info("====== Test_001_Login ======")
        self.logger.info("====== Verifying test_login ======")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage_Nop(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_loginPage_title = self.driver.title

        if act_loginPage_title == self.exp_loginPage_title:
            assert True
            self.logger.info("****** test_login is Passed ******")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.logger.info("****** test_login is Failed ******")
            assert False
        self.driver.close()
