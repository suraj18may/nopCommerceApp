import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    linkcuctomer_menu_Xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    linkcuctomer_menuitem_Xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txtEmail_id="Email"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_xpath="//input[@id='Gender_Male']"
    rdFemailGender_xpath="//input[@id='Gender_Female']"
    txtDOB_xpath="//input[@id='DateOfBirth']"
    txtCompanyName_xpath="//input[@id='Company']"
    txtjenish_xpath="//input[@id='customer_attribute_1']"
    txtCustomerroles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listitemAdministrator_xpath="//li[contains(text(),'Administrators')]"
    listitemRegistered_xpath="//li[contains(text(),'Registered')]"
    listitemGuest_xpath="//li[contains(text(),'Guest')]"
    listitemVendor_xpath="//li[contains(text(),'Vendors')]"
    drpManagerofvendor_xpath="//*[@id='VendorId']"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.linkcuctomer_menu_Xpath).click()

    def ClickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.linkcuctomer_menuitem_Xpath).click()
    def ClickAddButton(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(firstname)

    def setlastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lastname)

    def setGender(self,Gender):
        if Gender=="Male":
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif Gender=="Female":
            self.driver.find_element(By.XPATH,self.rdFemailGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
    def setDOB(self,Dob):
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys(Dob)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(companyname)

    def setjenish(self,jenish):
        self.driver.find_element(By.XPATH,self.txtjenish_xpath).send_keys(jenish)

    def setCustomerRole(self,role):

        self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
        self.driver.find_element(By.XPATH,self.txtCustomerroles_xpath).click()

        time.sleep(5)
        if role=="Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemAdministrator_xpath)
            self.listitem.click()
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
            self.listitem.click()

        elif role == "Guests":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuest_xpath)
            self.listitem.click()
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemVendor_xpath)
            self.listitem.click()

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuest_xpath)
        # self.driver.execute_script("argument[0].click();",self.listitem)

    def setMgrVandor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpManagerofvendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComt(self,Admincmt):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(Admincmt)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()




