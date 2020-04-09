from selenium.webdriver.common.by import By
from ReusableScreens.Locators import Locator

class MainScreen(object):
    def __init__(self, driver):
        self.makePaymentBtn = driver.find_element_by_id(Locator.makePaymentButton)

    def clickMakePayment(self):
        self.makePaymentBtn.click();