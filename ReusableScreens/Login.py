from selenium.webdriver.common.by import By
from ReusableScreens.Locators import Locator


class Login(object):

    def __init__(self, driver):


        self.userName = driver.find_element_by_id(Locator.userName)

        self.password = driver.find_element_by_id(Locator.password)
        self.loginButton = driver.find_element_by_id(Locator.loginButton)

    def setUserName(self, userName):
        self.userName.send_keys(userName)

    def setPassword(self, password):
        self.password.send_keys(password)

    def clickLogin(self):
        self.loginButton.click()