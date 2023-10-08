import time
import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.loginPage import loginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseURl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("********Test_003_AddCustomer**********")
        self.driver=setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp=loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.logger.info("********successfully login************")

        self.logger.info("********starting add customer Test************")

        self.driver.implicitly_wait(10)
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomerMenu()
        self.addcust.ClickOnCustomerMenuItem()
        self.addcust.ClickAddButton()
        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Mrinal")
        self.addcust.setlastName("Mishra")
        self.addcust.setGender("Male")
        self.addcust.setDOB("11/12/1995")
        self.addcust.setCompanyName("TCS")
        # self.addcust.setjenish("tester1")
        self.addcust.setCustomerRole("Guests")
        # time.sleep(10)
        self.addcust.setMgrVandor("Vendor 2")
        self.addcust.setAdminComt("for testing purpose")
        self.addcust.ClickOnSave()
        time.sleep(5)


        self.logger.info("**********saving customer info**********")
        self.logger.info("*********Add coustomer validation start")


        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("********Add customer test passed********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addcustomer_scr.png")
            self.logger.info("********Add customer test failed********")
            assert True==False
        self.driver.close()
        self.logger.info("********ending Home page Title Test********")


def random_generator(size=8 ,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
