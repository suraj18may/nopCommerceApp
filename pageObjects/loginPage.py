from selenium import webdriver
from selenium.webdriver.common.by import By

class loginPage:
    textbox_Username_xpath="//input[@id='Email']"
    textbox_Password_xpath="//input[@id='Password']"
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_xpath="//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_Password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Password_xpath).send_keys(password)

    def clickLogIn(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()


