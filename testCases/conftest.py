from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup(browser):
    print(browser)
    if browser == 'chrome':
        # url = 'https://python.org/'
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.binary_location = '/Users/ngocchien/Downloads/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
        chrome_driver_path = '/Users/ngocchien/Downloads/chromedriver-mac-arm64/chromedriver'
        service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service_options,
                                  options=chrome_options)
        print("\nLaunching Chrome browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

