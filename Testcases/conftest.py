from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
#   IF DRIVER FAILS TO OPEN BROWSER REFER THIS SITE
# https://stackoverflow.com/questions/76762892/chromedriver-version-115-not-found

@pytest.fixture(autouse=True)
# @pytest.fixture()
def setup(request, browser):
    ssl_cert = Options()
    # ssl_cert.use_chromium = True
    ssl_cert.add_argument('--ignore-certificate-errors')

    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--ignore-certificate-errors')
    # def setup():
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ssl_cert)
        print("Launching Chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=ssl_cert)
        print("Launching Edge browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser")
    elif browser == 'headless':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opt)
        print("Launching Headless browser")
    else:
        # driver = webdriver.Chrome(ChromeDriverManager(version="116.0.5845.97").install(), options=ssl_cert)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Default browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
    request.cls.driver = driver
    yield
    driver.quit()

    # return driver


def pytest_addoption(parser):  # this will get the val ue from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

##################### pytest HTML reports ####################

# It is hook for adding environment info to Html report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'selenium&pytest_framework'
#     config._metadata['Module Name'] = 'Products'
#     config._metadata['Tester'] = 'Harish Kumar'

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)



