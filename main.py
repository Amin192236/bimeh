

import unittest
import schedule
from Locators import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from time import sleep
from Pages.MongoDB.Mongo import Mongodb
from Locators import code_admin
from Pages.Login import LoginPage

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)


class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []

    ###Loginssfsdfdsdsdaszsaa

    def test01_login_wrong_phone(self):
        self.driver.get(base_url)
        alert = Alert(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("989122367800")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        sleep(2)
        print(alert.text)
        alert.accept()
        message = "با زدن شماره اشتباه و کد صحیح وارد نمی شود."
        self.tests_texts.append(message)
        print(message)

    def test02_login_wrong_code(self):
        self.driver.get(base_url)
        alert = Alert(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("989122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43136")
        login.enter_login_btn_submit()
        sleep(1)
        print(alert.text)
        alert.accept()
        message = "با زدن شماره صحیح و کد اشتباه وارد نشد."
        self.tests_texts.append(message)
        print(message)

    def test03_login_not_phone(self):
        self.driver.get(base_url)
        alert = Alert(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_btn_submit_next()
        sleep(1)
        print(alert.text)
        alert.accept()
        message = "بدون وارد کردن شماره تلفن وارد نشد."
        self.tests_texts.append(message)
        print(message)

    def test04_login(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("989122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        message = "با موفقیت وارد پنل شد و تست به درستی به پایان رسید."
        self.tests_texts.append(message)
        print(message)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(1)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Login , 'test_login')
