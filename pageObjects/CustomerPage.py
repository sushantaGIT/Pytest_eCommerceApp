import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddCustomer:
    menuCustomers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    subMenuCustomers_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdGenderMale_id = "Gender_Male"
    rdGenderFemale_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    dtDOB_Calendar_xpath = "//span[@class='k-icon k-i-calendar']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    btnSave_xpath = "//button[@name='save']"
    alert_SuccessMessage_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.menuCustomers_xpath).click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element(By.XPATH, self.subMenuCustomers_xpath).click()

    def clickOnAddNewBtn(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def enterFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def enterLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGenderMale(self):
        self.driver.find_element(By.ID, self.rdGenderMale_id).click()

    def setGenderFemale(self):
        self.driver.find_element(By.ID, self.rdGenderFemale_id).click()

    def enterDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def enterCompanyName(self, compName):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(compName)

    def selectCustomerRole_Administrators(self):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath).click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()


class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstname_id = "SearchFirstName"
    txtLastname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    table_SearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_Rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_Columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enterEmailSearch(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def enterFirstnameSearch(self, fname):
        self.driver.find_element(By.ID, self.txtFirstname_id).clear()
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(fname)

    def enterLastnameSearch(self, lname):
        self.driver.find_element(By.ID, self.txtLastname_id).clear()
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Columns_xpath))

    def searchCustomerByEmail(self, Email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == Email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
