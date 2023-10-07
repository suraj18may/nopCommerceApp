import time

from pageObjects.loginPage import loginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test__002__DDT__Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData//LoginData.xlsx"
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("*************Test__002__DDT__Login***********")
        self.logger.info("*************test_login__ddT__Title***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=loginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        # print(self.rows)

        lst_status=[]
        for r in range(2,self.rows+1):
            self.username=XLUtils.readdata(self.path,"Sheet1",r,1)
            self.password=XLUtils.readdata(self.path,"Sheet1",r,2)
            self.exp= XLUtils.readdata(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogIn()
            time.sleep(5)

            act_title=self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("*****passed*******")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("*****failed*******")
                    self.lp.clickLogout()
                    lst_status.append("fail")

            elif act_title!=exp_title:
                if self.exp=="pass":
                    self.logger.info("*****failed*******")
                    lst_status.append("fail")
                elif self.exp=="fail":
                    self.logger.info("*****passed*******")
                    lst_status.append("pass")

        if"fail" not in lst_status:
            self.logger.info("*********Login test DDT passed************")
            self.driver.close()
            assert True

        else:
            self.logger.info("*********Login test DDT failed************")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
