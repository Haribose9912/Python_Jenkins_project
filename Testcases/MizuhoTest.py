import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException

from Utilities.customLogger import configure_logger
from Pageobjects.Mizuhopage import MizuHome
from Utilities.base_driver import basedriver


@pytest.mark.usefixtures("setup")
class Test_form_001:
    logger = configure_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.mh = MizuHome(self.driver)
        self.mh.Mizu_url()

    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_page_title(self):
        base = basedriver(self.driver)
        self.logger.info('****Verifying home page title****')

        act_title = self.driver.title
        exp_title = act_title
        if act_title == exp_title:
            print("Page title is matching")
            self.driver.save_screenshot(".\\Screenshots\\" + "homePage_title_Pass.png")
            self.logger.info('****Home page title passed****')
            self.driver.close()
            assert True
        else:
            print("Page title is not matching")
            self.driver.save_screenshot(".\\Screenshots\\" + "homePage_title_fail.png")
            # base.screenshot()
            self.logger.warn('******Home page title is failed********')
            self.driver.close()
            assert False

    def test_login_home(self):
        email = "surendrapuvvada4@gmail.com"
        password = "1@Puvvada"
        self.mh.enter_email(email)
        # self.mh.click_next()
        time.sleep(3)
        try:
            self.mh.enter_password(password)
        except TimeoutException:
            print("Timeout exception occured")

        self.mh.click_signin()
        self.driver.save_screenshot(".\\Screenshots\\" + "Mizuho_home_page.png")


