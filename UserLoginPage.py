import random
from BaseClass import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from AdminPage import AdminPage as AP


class UserLoginPage(BaseClass):

    def go_to_login_page(self, url):
        self.logger.info("Opening source: {}".format(url + self.LOGIN_PAGE))
        self.browser.get(url + self.LOGIN_PAGE)
        return self

    def open_reg_account_page(self, url):
        self.logger.info("Opening source: {}".format(url + self.REGISTER_ACCOUNT_PAGE))
        self.browser.get(url + self.REGISTER_ACCOUNT_PAGE)
        return self

    def from_login_page_to_reg_account_page(self, url):
        self.go_to_login_page(url)
        self.logger.info("Clicking on the CONTINUE button")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON)).click()
        return self

    def compose_phone_number(self, short=3, long=11):
        shortest = 10**int(short)
        longest = 10**int(long)
        return str(random.randint(shortest, longest))

    def fill_in_with_letters(self, locator, name=None):
        if name is None:
            name = self.generate_string().capitalize()
        self.logger.info("Filling in field \"{}\" with string: {}".format(locator[1], name))
        self.fill_specified_field(locator, name)

    def enter_email(self, email=None):
        if email is None:
            email = self.generate_string(uppercase=True, num=True) + "@test.ru"
        email_field = self.find_web_element(self.EMAIL_FIELD)
        self.logger.info(f"Entering email: {email}")
        self.fill_specified_field(email_field, email)

    def enter_telephone(self, phone_number=None, min=3, max=11):
        if phone_number is None:
            phone_number = self.compose_phone_number(short=min, long=max)
        self.logger.info(f"Entering phone number: {phone_number}")
        self.fill_specified_field(self.find_web_element(self.TELEPHONE_FIELD), phone_number)

    def enter_password(self, pwd=None, save_pwd=False):
        if pwd == None:
            pwd = self.generate_string(uppercase=True, num=True, sym=True)
        self.logger.info(f"Entering password: {pwd}")
        self.fill_specified_field(self.find_web_element(self.PASSWORD_FIELD), pwd)
        if save_pwd:
            return pwd


    def enter_and_confirm_password(self, user_pwd=None):
        password = self.enter_password(pwd=user_pwd, save_pwd=True)
        self.logger.info(f"Entering and confirming password: {password}")
        self.fill_specified_field(self.find_web_element(self.PASSWORD_CONFIRM_FIELD), password)

    def form_autocomplete(self):
        self.fill_in_with_letters(self.FIRST_NAME_FIELD)
        self.fill_in_with_letters(self.LAST_NAME_FIELD)
        self.enter_email()
        self.enter_telephone()
        self.enter_and_confirm_password()

    def wait_and_click(self, clickable_element, timeout=2):
        self.logger.info("Clicking on the element \'{} = {}\'".format(*clickable_element))
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(clickable_element)).click()

    def view_success_notification(self):
        notification = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SUCCESS_NOTIFICATION))
        return notification.text

    def user_authentication(self, url, email, password):
        self.go_to_login_page(url)
        self.fill_specified_field(self.EMAIL_ADDRESS, email)
        self.fill_specified_field(self.INPUT_PASSWORD, password)
        self.find_web_element(self.LOGIN_BUTTON).click()
