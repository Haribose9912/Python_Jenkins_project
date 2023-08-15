pytest -v -s --alluredir='./Reports' Testcases/Formfilltest.py --browser headless
pytest -v -s --alluredir='./Reports' Testcases/Formfilltest.py
pytest -v -s --html-report=./report --title='Hariesh Project Test Report' Testcases/Formfilltest.py --browser chrome