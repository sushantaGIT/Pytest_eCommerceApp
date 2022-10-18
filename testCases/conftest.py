from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

"""
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    return driver """

# To run tests on Specific Browser:
# pytest -v -s testCases/test_Login.py --browser chrome
# pytest -v -s testCases/test_Login.py --browser edge

# To run tests with HTML report
# pytest -v -s --html=Reports\report.html testCases/test_Login.py (If log not showing in report, then remove '-s' from command)

# To run specific set of tests 'markers'
# pytest -v -m "regression" --html=Reports\report_regression.html testCases/


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        print("Launching Chrome browser .....")
    elif browser=='edge':
        driver = webdriver.Edge(executable_path="C:\Drivers\msedgedriver.exe")
        print("Launching Edge browser .....")
    else:
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        print("Launching Chrome browser .....")
    return driver

def pytest_addoption(parser):   # This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")

########## To Generate PyTest HTML Report ##########################

# It is hook for adding Environment into HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'eCommerceApp'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['QA'] = 'Sushanta'


# It is hook for Delete/modify Environment into HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)