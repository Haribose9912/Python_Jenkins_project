import time
import pytest
# from pytest_html_reporter.plugin import screenshot
from selenium import webdriver
from Utilities.customLogger import configure_logger
from Pageobjects.Formfillpage import Formfill
# from ddt import ddt, data, file_data, unpack
from Utilities.base_driver import basedriver


# from pytest_html_reporter import attach


@pytest.mark.usefixtures("setup")
class Test_form_001:
    logger = configure_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ff = Formfill(self.driver)
        self.ff.Form_url()

    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.skip
    def test_page_title(self):
        base = basedriver(self.driver)
        self.logger.info('****Verifying home page title****')

        act_title = self.driver.title
        exp_title = act_title
        if act_title == exp_title:
            print("Page title is matching")
            self.driver.save_screenshot(".\\Screenshots\\" + "homePage_title_Pass.png")
            self.logger.info('****Home page titile passed****')
            self.driver.close()
            assert True
        else:
            print("Page title is not matching")
            self.driver.save_screenshot(".\\Screenshots\\" + "homePage_title_fail.png")
            # base.screenshot()
            self.logger.warn('******Home page title is failed********')
            self.driver.close()
            assert False

    def test_form_fill(self):
        base = basedriver(self.driver)

        self.ff.full_form_fill("hariesh", "kumar", "hari@gmail.com", "040-9944996", "plot.no.94/p,subashnagar",
                               "hyderabad", "50055", "www.google.com", "testingworldnewapproach")
        base.screenshot()
        time.sleep(2)
        cd = self.driver.window_handles


    @pytest.mark.skip
    def test_form_fill2(self):
        base = basedriver(self.driver)
        self.ff.full_form_fill("ravana", "kumara", "ravana@gmail.com", "040-9944996", "plot.no.94/p,subashnagar",
                               "malesiya", "50055", "www.ravana.com", "testingworldnewapproach")
        base.screenshot()
        time.sleep(5)

    # def screenshot_on_failure(self):
    #     for self._testMethodName, error in self._outcome.errors:
    #         if error:
    #             attach(data=screenshot, name="screenshot.png", attachment_type="image/png")
########### end of the code ############
