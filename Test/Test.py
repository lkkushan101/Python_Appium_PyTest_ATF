import os
import time
import unittest
from time import sleep
from appium import webdriver
from ReusableScreens.Login import Login
from ReusableScreens.MainScreen import MainScreen
from ReusableScreens.MakePayment import MakePayment
from htmllogger.Htmllogger import HTMlLogger
import allure
import json
import pytest
@allure.story('Python Test Automation Framework')
@allure.feature('Registration')
@allure.testcase('Registration Test Case')
class ContactAppTestAppium(unittest.TestCase):


    def setUp(self):
        with open('../Data/data.json', encoding='utf-8') as data_file:
            self.logger = HTMlLogger('C:/Users/user/PycharmProjects/Appium_ATF')
            data = json.loads(data_file.read())
            desired_caps = {}
            desired_caps['platformName'] = data['platformName']

            desired_caps['deviceName'] = data['deviceName']
            desired_caps['appPackage'] = data['appPackage']
            desired_caps['appActivity'] = data['appActivity']

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def tearDown(self):

        self.driver.quit()


    def test_single_bankapp(self):
        with open('../Data/data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
       # driver = self.driver
        login = Login(self.driver)
        login.setUserName(data['User'])
        login.setPassword(data['User'])
        login.clickLogin()
        self.logger.assert_step_log("Logged into the eribank app")
        time.sleep(3)
        mainScreen = MainScreen(self.driver)
        mainScreen.clickMakePayment()
        self.logger.assert_step_log("Navigated into the make payment screen")
        makePaymentScreen = MakePayment(self.driver)
        makePaymentScreen.makePayment(data['tele'], data['name'], data['country'])
        self.logger.assert_step_log("Did the payment")
        sleep(5)