from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    print(browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("\nLaunching Chrome browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")