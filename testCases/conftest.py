import pytest
from selenium import webdriver

# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     return driver

# enhance
# run test on cross browser
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox

    else:
        driver=webdriver.Edge()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
# def pytest_configure (config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'customer'
#     config._metadata['Tester'] = 'Suraj'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugin", None)