import pytest


@pytest.mark.usefixtures("init_WebDriver")
class Base_Twitter_Test:
    pass


class Test_Twitter_Chrome(Base_Twitter_Test):
    def test_Twitter_Title(self):
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


@pytest.mark.usefixtures("init_WebDriver")
class Base_Firefox_Test:
    pass


class Test_FB_Firefox(Base_Firefox_Test):
    def test_FB_Title(self):
        self.driver.get("https://www.facebook.com/login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)



