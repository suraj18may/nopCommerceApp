from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:
    txtbox_email_xpath="//input[@id='SearchEmail']"
    txtbox_FirstName_xpath="//input[@id='SearchFirstName']"
    txtbox_LastName_xpath="//input[@id='SearchLastName']"
    btnSearchBox_xpath="//button[@id='search-customers']"
    table_xpath="//div[@id='customers-grid_wrapper']//div[@class='row']"
    table_rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_cloumns_xpath="//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtbox_FirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_FirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtbox_LastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_LastName_xpath).send_keys(lname)
    def ClickSearch(self):
        self.driver.find_element(By.XPATH,self.btnSearchBox_xpath).click()

    def getNoOfRows(self):
        return  len(self.driver.find_elements(By.XPATH,self.table_rows_xpath))
    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_cloumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            # table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByname(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            # table=self.driver.find_element(By.XPATH,self.table_xpath)
            Name=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag=True
                break
        return flag


