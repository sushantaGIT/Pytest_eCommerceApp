import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.CustomerPage import AddCustomer
from pageObjects.CustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*************** Test_004_SearchCustomerByEmail **********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ****************")

        self.logger.info("************* Starting Search Customer by Name *************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()
        #self.addcust.clickOnAddNewBtn()

        self.logger.info("************* Searching Customer by First and Last Name *************")
        searchcust = SearchCustomer(self.driver)
        searchcust.enterFirstnameSearch("Victoria")
        searchcust.enterLastnameSearch("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***************** Test_004_SearchCustomerByName Finished ***************")
        self.driver.close()
