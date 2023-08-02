import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def exp_homepage_title():
        homepage_title = config.get('common info', 'exp_homepage_title')
        return homepage_title

    @staticmethod
    def exp_loginPage_title():
        loginPage_title = config.get('common info', 'exp_loginPage_title')
        return loginPage_title



