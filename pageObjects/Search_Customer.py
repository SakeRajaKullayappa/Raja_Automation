from selenium.webdriver.common.by import By


class Search_Customer:
    ser_emai_xpath = "//input[@id = 'SearchEmail']"
    ser_fName_xpath = "//input[@id = 'SearchFirstName']"
    ser_lName_xpath = "//input[@id = 'SearchLastName']"
    ser_company_xpath = "//input[@id = 'SearchCompany']"
    btn_search_xpath = "//button[@id = 'search-customers']"
    table_xpath = "//div[@id = 'customers-grid_wrapper']"
    table_head_row_xpath = "//div[@id = 'customers-grid_wrapper']//thead//tr"
    table_head_col_xpath = "//div[@id = 'customers-grid_wrapper']//thead//tr//th"
    table_rows_xpath = "//div[@id = 'customers-grid_wrapper']//tbody//tr"
    table_cols_xpath = "//div[@id = 'customers-grid_wrapper']//tbody//tr//td"

    def __init__(self, driver):
        self.driver = driver

    def setSearchEmai(self, serEmail):
        self.driver.find_element(By.XPATH, self.ser_emai_xpath).clear()
        self.driver.find_element(By.XPATH, self.ser_emai_xpath).send_keys(serEmail)

    def setSearchFName(self, serFName):
        self.driver.find_element(By.XPATH, self.ser_fName_xpath).clear()
        self.driver.find_element(By.XPATH, self.ser_fName_xpath).send_keys(serFName)

    def setSearchLName(self, serLName):
        self.driver.find_element(By.XPATH, self.ser_lName_xpath).clear()
        self.driver.find_element(By.XPATH, self.ser_lName_xpath).send_keys(serLName)

    def setSearchCompany(self, serCompany):
        self.driver.find_element(By.XPATH, self.ser_company_xpath).clear()
        self.driver.find_element(By.XPATH, self.ser_company_xpath).send_keys(serCompany)

    def clickSearchButton(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoOfCols(self):
        return len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))

    def searchCustomerByEmail(self, byEmail):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email_id = table.find_element(By.XPATH,
                                          "//div[@id = 'customers-grid_wrapper']//tbody//tr["+str(r)+"]//td[2]").text
            if email_id == byEmail:
                flag = True
                break
        return flag

    def searchCustomerByName(self, byName):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Name = table.find_element(By.XPATH,
                                      "//div[@id = 'customers-grid_wrapper']//tbody//tr["+str(r)+"]//td[3]").text
            if Name == byName:
                flag = True
                break
        return flag

    def searchCustomerByCompany(self, byCompany):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Company = table.find_element(By.XPATH,
                                         "//div[@id = 'customers-grid_wrapper']//tbody//tr["+str(r)+"]//td[5]").text
            if Company == byCompany:
                flag = True
                break
        return flag



