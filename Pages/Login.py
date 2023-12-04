
import os

from selenium.common.exceptions import NoSuchElementException

from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# import pytesseract
# from PIL import Image


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.2)
    element.click()
    sleep(0.2)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(1)
    #ActionChains(self.driver).move_to_element(element).send_keys(Keys.CONTROL + "a").send_keys(Keys.BACKSPACE).send_keys(text).perform()

    element.click()
    sleep(0.2)
    element.send_keys(Keys.CONTROL + "a")
    sleep(0.2)
    element.send_keys(Keys.BACKSPACE)
    sleep(0.2)
    element.send_keys(text)
    sleep(0.2)


def get_url_with_refresh(self, url, element_id, max_retries=2, delay_seconds=0.1):
    for retry_count in range(max_retries + 1):
        self.driver.get(url)
        try:
            self.driver.find_element('xpath', element_id)
            return
        except NoSuchElementException:
            print(f"Element with id '{element_id}' not found. Retrying in {delay_seconds} seconds...")

        if retry_count < max_retries:
            sleep(delay_seconds)
        else:
            raise Exception(f"Maximum number of retries reached. Element with id '{element_id}' not found.")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_login_phone_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_phone_number, text)

    def enter_login_check_phone_number(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_check_phone_number)

    def enter_login_password(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_password, text)

    def enter_login_password_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_password_submit)

    def visibility_of_elements(self, element_locator):
        self.driver.find_element('xpath', element_locator)

    def assert_login_wrong_phone_number(self, element_locator, text):
        sleep(1)
        wait = WebDriverWait(self.driver, 20)
        sleep(1)
        element = wait.until(EC.element_to_be_clickable(('xpath', element_locator)))
        e = element.text
        assert text in e

    def assert_login_wrong_password(self, element_locator, text):
        wait = WebDriverWait(self.driver, 20)
        sleep(0.2)
        element = wait.until(EC.element_to_be_clickable(('xpath', element_locator)))
        e = element.text
        assert text in e

    def test_pass_type(self, xpath):
        wait = WebDriverWait(self.driver, 20)
        check_pass = wait.until(EC.element_to_be_clickable(('xpath', xpath)))
        assert check_pass.is_displayed(), "Your password is masked!"

    def enter_login_hidden_password(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_hidden_password)

    def enter_login_link_phone_edit(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_link_phone_edit)

    def enter_login_link_forget(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_link_forget)

    def enter_login_link_otp_login(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_link_otp_login)

    def enter_check_forget_btn_submit(self):
        wait = WebDriverWait(self.driver, 20)
        sleep(0.2)
        button = self.driver.find_element('xpath', login_forget_btn_submit)
        is_disabled = button.get_attribute("disabled") == "true"
        if is_disabled:
            print("The button is disabled.")
        else:
            print("The button is enabled.")

    def enter_login_assert_btn_code(self, locator, lene):
        wait = WebDriverWait(self.driver, 20)
        sleep(0.2)
        elements = wait.until(EC.presence_of_all_elements_located(('xpath', locator)))
        timer = wait.until(EC.element_to_be_clickable(('xpath', login_forget_timer)))
        timer = timer.text
        assert '180' in timer
        print("تایمر به درستبی مشاهده شد.")
        assert len(elements) == lene
        lene = str(lene)
        print(" کد " + lene + " رقمی و صحیحی می باشد.")

