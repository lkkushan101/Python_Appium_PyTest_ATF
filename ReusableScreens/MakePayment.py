from selenium.webdriver.common.by import By
from ReusableScreens.Locators import Locator


class MakePayment(object):

    def __init__(self, driver):

        self.tele = driver.find_element_by_id(Locator.inputTel)

        self.name = driver.find_element_by_id(Locator.inputName)
        self.tracker = driver.find_element_by_id(Locator.amountTracker)

        self.inputCountry = driver.find_element_by_id(Locator.inputCountry)
        self.sendPaymentButton = driver.find_element_by_id(Locator.sendPaymentButton)




    def makePayment(self, tele, name, country):
        self.tele.send_keys(tele)
        self.name.send_keys(name)
        self.inputCountry.send_keys(country)
        self.tracker.send_keys('0.5')

        self.sendPaymentButton.click()