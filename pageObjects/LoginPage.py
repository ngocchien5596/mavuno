from selenium.webdriver.common.by import By

class Login:
    textbox_username_xpath = "(//input[@name='username'])"
    textbox_password_xpath = "(//input[@name='password'])"
    button_login_xpath = "(//button[normalize-space()='Login'])"

    def __init__(self, driver):
        self.driver = driver

    def setUser(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()