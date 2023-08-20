import time
# from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from Utilities.base_driver import basedriver


class MizuHome(basedriver):
    # locators of all webelements
    email_id = "//input[@type='email']"
    Next_btn = "//input[@type='submit']"
    password = "//input[@type='password']"
    sign_in = "//input[@id='idSIButton9']"

    Mizuho_url = "https://uat.issueraccess.mizuhogroup.com"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Mizu_url(self):
        self.driver.get(self.Mizuho_url)

    def get_email_id(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.email_id)

    def enter_email(self, email):
        self.get_email_id().clear()
        self.get_email_id().send_keys(email)
        self.get_email_id().send_keys(Keys.ENTER)

    def get_paasword(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.password)

    def enter_password(self, password):
        self.get_paasword().clear()
        self.get_paasword().send_keys(password)
        self.get_paasword().send_keys(Keys.ENTER)

    def click_next(self):
        self.wait_until_element_is_clickable(By.XPATH, self.Next_btn).click()

    # def click_hosting_btn_yes(self):
    #     self.wait_until_element_is_clickable(By.XPATH, self.hosting_yes).click()

    def click_signin(self):
        self.wait_until_element_is_clickable(By.XPATH, self.sign_in).click()

    # def retry_on_timeout(func, max_retries=3):
    #     for attempt in range(max_retries + 1):
    #         try:
    #             return func()
    #         except TimeoutException:
    #             print(f"Attempt {attempt + 1}/{max_retries + 1}: TimeoutException occurred. Retrying...")
    #
    #     raise TimeoutException("Maximum retries reached. Action failed.")