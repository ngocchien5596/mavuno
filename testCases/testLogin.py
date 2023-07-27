from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
import pytest
import time
from utilities.readPropertises import ReadConfig


class Test_Login_UI:

    # baseURL = "https://mavuno-web-staging.pula.cloud/login"
    # username = "chien"
    # password = "traikimnguu5596"

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    exp_title = "Mavuno Admin"
    act_title_xpath = "(//span[normalize-space()='Mavuno Admin'])"
    logger = LogGen.loggen()
    exp_error_message = "Please fill out this field."
    error_message_xpath = '(//p[@class="help is-danger"])'
    mavuno_logo_xpath = "(//img[@class='admin-logo'])"

    def test_Text_Title(self, setup):
        self.logger.info("test text of title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.find_element(By.XPATH,self.act_title_xpath).text
        if act_title == self.exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_FontSize_Title(self,setup):
        self.logger.info("test font size of title")
        self.driver = setup
        self.driver.get(self.baseURL)
        fontSize_act_title = self.driver.find_element(By.XPATH, self.act_title_xpath).value_of_css_property('font-size')
        print(fontSize_act_title)
        if fontSize_act_title == '16px':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_Font_Title(self,setup):
        self.logger.info("test font of title")
        self.driver = setup
        self.driver.get(self.baseURL)
        font_act_title = self.driver.find_element(By.XPATH, self.act_title_xpath).value_of_css_property('font-family')
        print(font_act_title)
        if font_act_title == 'Nunito, sans-serif':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False


    # Test clicking Login without filling all fields
    def test_Login_Flow_01(self, setup):
        self.logger.info("test flow 1: Test clicking Login without filling all fields")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = Login(self.driver)
        self.lp.clickLogin()
        time.sleep(3)
        act_error_message = self.lp.driver.find_element(By.XPATH,self.error_message_xpath).text
        print(act_error_message)
        if act_error_message == self.exp_error_message:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    @pytest.mark.sanity
    # Test clicking Login after filling all fields
    def test_Login_Flow_02(self, setup):
        self.logger.info("test flow 2: Test clicking Login after filling all fields")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = Login(self.driver)
        self.lp.setUser(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(3)

        if self.driver.find_element(By.XPATH,self.mavuno_logo_xpath):
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False






