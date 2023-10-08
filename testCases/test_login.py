import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test__001__Login:
    baseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUserName()
    Password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*************Test__001__Login***********")
        self.logger.info("*************test_homePageTitle***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginTitlePage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginPage(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogIn()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
