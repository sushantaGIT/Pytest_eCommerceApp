import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.CustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*************** Test_003_AddCustomer **********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ****************")

        self.logger.info("************* Starting Add Customer Test *************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()
        self.addcust.clickOnAddNewBtn()
        self.logger.info("************* Providing Customer info *************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.enterEmail(self.email)
        self.addcust.enterPassword("test123")
        self.addcust.enterFirstName("Sushant")
        self.addcust.enterLastName("Sharma")
        self.addcust.setGenderMale()
        self.addcust.enterDOB("9/11/1985")
        self.addcust.enterCompanyName("QAtest")
        self.addcust.selectCustomerRole_Administrators()
        self.addcust.clickOnSave()
        self.logger.info("*************** Saving Customer info ************")

        self.logger.info("******* Validation Started *****************")
        self.message = self.driver.find_element(By.TAG_NAME, "body").text
        #self.msg = self.driver.find_element_by_tag_name("body").txt

        #print(self.message)
        if 'customer has been added successfully.' in self.message:
            self.driver.save_screenshot(".\\Screenshots\\" + "AddCustomer_Passed.png")
            assert True == True
            self.logger.info("*************** Add Customer Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "AddCustomer_Failed.png")
            self.logger.info("************* Add Customer Test Failed ************")
            assert True == False

        self.driver.close()
        self.logger.info("*********** Ending Test_003_AddCustomer Test **************")



def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
