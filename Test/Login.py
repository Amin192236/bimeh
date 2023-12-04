from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.sql import SqlServer
from time import sleep
from Locators import *
from Pages.Login import LoginPage, get_url_with_refresh
import unittest
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
tick = datetime.now()


#Login

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        # cls.driver.set_window_size(320, 568)
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []

    def test01_should_get_error_if_phone_is_not_send(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.enter_login_phone_number(" ")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        print("بدون وارد کردن شماره موبایل ورود امکان پذیر نیست.")
        self.tests_texts.append("01pass/")

    def test02_should_get_error_if_phone_is_wrong(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number("0938909035r")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        print("با وارد کردن شماره موبایل اشتباه ورود امکان پذیر نیست.")
        self.tests_texts.append("02pass/")

    def test03_should_get_error_if_phone_is_wrong(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number("0 9 3 8 9 0 9 0 3 5 9")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        print("با وارد کردن شماره موبایل اشتباه ورود امکان پذیر نیست.")
        self.tests_texts.append("03pass/")

    def test04_should_get_error_if_phone_is_less_than_11_character(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number("0938909035")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        print("با وارد کردن شماره موبایل با یک کارکتر کمتر، ورود امکان پذیر نیست.")
        self.tests_texts.append("04pass/")

    def test05_should_get_error_if_phone_is_greater_than_11_character(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number("093890903599")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_verified_phone_number, '09389090359')
        print("با وارد کردن شماره موبایل با یک کارکتر بیشتر، کارکتر اضافه زده نمی شود.")
        self.tests_texts.append("05pass/")

    def test06_should_get_error_if_code_is_not_send(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number(phone_number1)
        login.enter_login_check_phone_number()
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_phone_edit)
        login.visibility_of_elements(login_link_forget)
        login.visibility_of_elements(login_link_otp_login)
        login.visibility_of_elements(login_hidden_password)
        login.enter_login_password(" ")
        login.enter_login_password_submit()
        login.assert_login_wrong_password(login_wrong_password, 'نام کاربری یا رمز عبور اشتباه است')
        print("با وارد نکردن کد، ورود امکان پذیر نیست.")
        self.tests_texts.append("06pass/")

    def test07_should_get_error_if_code_is_wrong(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number(phone_number1)
        login.enter_login_check_phone_number()
        login.enter_login_password("rahad31*")
        login.test_pass_type("//*[@type='password']")
        login.enter_login_hidden_password()
        login.test_pass_type("//*[@type='text']")
        login.enter_login_password_submit()
        login.assert_login_wrong_password(login_wrong_password, 'نام کاربری یا رمز عبور اشتباه است')
        print("با وارد کردن کد اشتباه، ورود امکان پذیر نیست.")
        self.tests_texts.append("07pass/")

    def test08_check_phone_edit(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number("09389090359")
        login.enter_login_check_phone_number()
        login.enter_login_link_phone_edit()
        login.enter_login_phone_number("09389090359")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_verified_phone_number, '09389090359')
        print("اصلاح شماره موبایل به درستی چک شد.")
        self.tests_texts.append("08pass/")

    def test09_check_forget_password(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number(phone_number2)
        login.enter_login_check_phone_number()
        login.enter_login_link_forget()
        login.enter_login_assert_btn_code(login_forget_btn_code, 4)
        login.enter_check_forget_btn_submit()
        login.visibility_of_elements(login_link_phone_edit)
        self.tests_texts.append("09pass/")
        print("فراموشی رمز عبور بررسی شد. ")

    def test10_check_otp(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number(phone_number3)
        login.enter_login_check_phone_number()
        login.enter_login_link_otp_login()
        login.enter_login_assert_btn_code(login_forget_btn_code, 6)
        login.enter_check_forget_btn_submit()
        login.visibility_of_elements(login_with_password)
        self.tests_texts.append("10pass/")
        print("ورود با کد otp بررسی شد. ")

    def test11_should_get_login_ok(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number(phone_number2)
        login.enter_login_check_phone_number()
        login.enter_login_password(code2)
        login.enter_login_password_submit()
        sleep(2)
        login.assert_login_wrong_phone_number(login_account_button, phone_number2)
        print("با وفقیت وارد پنل کاربر شد.")
        self.tests_texts.append("11pass/")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


SqlServer.run_tests_and_insert_into_sql_server(TestLogin, "Login", tick)

