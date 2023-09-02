import time
import pytest
# from pytest_html_reporter.plugin import screenshot
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        # initializing window handles
        p = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        self.logger.info('**** Started form filling ****')
        self.ff.full_form_fill("hariesh", "kumar", "hari@gmail.com", "040-9944996", "plot.no.94/p,subashnagar",
                               "hyderabad", "50055", "www.google.com", "testingworldnewapproach")
        base.screenshot()
        time.sleep(2)
        self.logger.info('**** Completed form filling ****')
        # cw = self.driver.window_handles
        # Locate the element by link text and click on it
        self.driver.execute_script("window.open('https://demo.seleniumeasy.com/','_blank');")
        child = self.driver.window_handles[1]
        # switching to child window
        self.logger.info('**** switching to child window ****')
        self.driver.switch_to.window(child)
        wait = WebDriverWait(self.driver, 20)
        n = 2
        k = wait.until(EC.number_of_windows_to_be(n))
        self.logger.info(f'Number of windows {n} are available is {k}')
        # self.driver.switch_to.window(cw[0])
        # for i in self.driver.window_handles:
        #     if i != cw:
        #         self.driver.switch_to.window(i)
        #         break
        # title = self.driver.title
        # wait.until(EC.title_is(title))
        self.logger.info(f'title of Child window is: {self.driver.title}')
        date = self.driver.find_element(By.LINK_TEXT, 'Date pickers')
        date.click()
        ele2 = "(//a[text()='Bootstrap Date Picker'])[2]"
        date_picker = self.driver.find_element(By.XPATH, ele2)
        self.driver.execute_script("arguments[0].click();", date_picker)
        # print(self.driver.title)
        base.custom_screenshot("Child_window.png")
        ele_select_date = self.driver.find_element(By.XPATH,
                                                   "//div[@id='sandbox-container1']//*[text()=' Select Date']")
        ele_select_date.text

        # print(ele_select_date.text)
        self.logger.info(f'Text of the date element is: {ele_select_date.text}')
        # switching to parent window
        self.logger.info('**** switching to Parent window ****')
        self.driver.switch_to.window(parent)
        self.logger.info(f'title of parent window is: {self.driver.title}')
        # print(self.driver.title)
        btn_ele = self.driver.find_element(By.XPATH, "//*[text()='Send ']")
        btn_ele.text
        base.custom_screenshot("Parent_window.png")
        # print(btn_ele.text)
        self.logger.info(f"Text of the button is: {btn_ele.text} ")
        self.logger.info('**** switching to child window ****')
        self.driver.switch_to.window(child)
        base.custom_screenshot("child_window.png")
        self.logger.info(f'title of Child window is: {self.driver.title}')
        ele_date_input =self.driver.find_element(By.XPATH, "//input[@placeholder='dd/mm/yyyy']")
        ele_date_input.send_keys('15/07/1993')
        ele_date_input.send_keys(Keys.ENTER)
        self.logger.info(f"Text present in the date input box: {ele_date_input.text}")
        self.logger.info("*****Closing browser*****")
        self.driver.quit()


    @pytest.mark.skip
    def test_form_fill2(self):
        base = basedriver(self.driver)
        self.ff.full_form_fill("ravana", "kumara", "ravana@gmail.com", "040-9944996", "plot.no.94/p,subashnagar",
                               "malesiya", "50055", "www.ravana.com", "testingworldnewapproach")
        base.screenshot()
        assert len(self.driver.window_handles) == 1
        time.sleep(5)

    # def screenshot_on_failure(self):
    #     for self._testMethodName, error in self._outcome.errors:
    #         if error:
    #             attach(data=screenshot, name="screenshot.png", attachment_type="image/png")
########### end of the code ############
