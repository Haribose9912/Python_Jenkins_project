pip install webdriver-auto-update
pytest -v -s --alluredir='./Reports' Testcases/Formfilltest.py --browser headless
pytest -v -s --alluredir='./Reports' Testcases/Formfilltest.py --browser chrome
allure serve "./Reports"