import time

from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.loginPage import loginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_SearchCustomerbyEmail__004:
    baseURl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("********Test_SearchCustomerbyEmail__004**********")
        self.driver=setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp=loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.logger.info("********successfully login************")

        self.logger.info("********starting SearchCustomer Test************")

        self.driver.implicitly_wait(10)
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomerMenu()
        self.addcust.ClickOnCustomerMenuItem()
        self.logger.info("**********test Search BY Email is Finished************")


        self.srchCustomer=SearchCustomer(self.driver)
        self.srchCustomer.setEmail("victoria_victoria@nopCommerce.com")
        self.srchCustomer.ClickSearch()
        time.sleep(2)
        status=self.srchCustomer.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status


