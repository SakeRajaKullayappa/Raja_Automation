import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer:
    lnk_customers_menu_xpath = "//a[@href = '#']//p[contains(text(), 'Customers')]"
    lnk_customers_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_xpath = "//a[@class = 'btn btn-primary' and @href = '/Admin/Customer/Create']"
    text_email_xpath = "//input[@id = 'Email']"
    text_password_xpath = "//input[@id = 'Password']"
    text_FirstName_xpath = "//input[@id = 'FirstName']"
    text_LastName_xpath = "//input[@id = 'LastName']"
    rd_gender_male_xpath = "//input[@id = 'Gender_Male']"
    rd_gender_female_xpath = "//input[@id = 'Gender_Female']"
    text_dob_xpath = "//input[@id='DateOfBirth']"
    text_company_xpath = "//input[@id = 'Company']"
    checkbox_isTaxExempt = "//input[@id = 'IsTaxExempt']"
    drp_mangerOfVendor_xpath = "//select[@id ='VendorId']"
    checkbox_active_xpath = "//input[@id = 'Active']"
    text_adminContext_xpath = "//textarea[@id = 'AdminComment']"
    btn_save_xpath = "//button[@name = 'save']"

    text_customerRole_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lst_administrators_xpath = "//li[contains(text(), 'Administrators')]"
    lst_forumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lst_guests_xpath = "//li[contains(text(), 'Guests')]"
    lst_registered_xpath = "//li[contains(text(), 'Registered')]"
    lst_Vendors_xpath = "//li[contains(text(), 'Vendors')]"

    success_msg_tag_name = "body"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomers_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()

    def clickCustomers_submenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_submenu_xpath).click()

    def clickAdd_new(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def setFName(self, fName):
        self.driver.find_element(By.XPATH, self.text_FirstName_xpath).send_keys(fName)

    def setLName(self, lName):
        self.driver.find_element(By.XPATH, self.text_LastName_xpath).send_keys(lName)

    def clickGender_Male(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rd_gender_male_xpath).click()

        elif gender == "FeMale":
            self.driver.find_element(By.XPATH, self.rd_gender_female_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.rd_gender_male_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.text_dob_xpath).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.text_company_xpath).send_keys(companyName)

    def clickIsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.rd_gender_male_xpath).click()

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.text_customerRole_xpath)
        time.sleep(3)

        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_administrators_xpath)
        elif role == "Guests":
            time.sleep(3)

            self.listitem = self.driver.find_element(By.XPATH, "//*[@id = 'SelectedCustomerRoleIds_taglist']/li"
                                                               "/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_guests_xpath)

        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_forumModerators_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lst_guests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectManagerOfVendor(self, managerOfVendor):
        vendor = Select(self.driver.find_element(By.XPATH, self.drp_mangerOfVendor_xpath))
        vendor.select_by_visible_text(managerOfVendor)

    def setAdminContext(self, adminContext):
        self.driver.find_element(By.XPATH, self.text_adminContext_xpath).send_keys(adminContext)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
