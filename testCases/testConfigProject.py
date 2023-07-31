from pageObjects.LoginPage import Login
from utilities.readPropertises import ReadConfig
import time
from pageObjects.Commercial.UnidashboardPage import UnidashboardPage
from Configurations.dataTest import DataTestForTestAddNewproject
class Test_ConfigProject:

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_Add_ProjectActors(self, setup):
        self.driver = setup

        # Login
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUser(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # Select left menu
        self.uni = UnidashboardPage(self.driver)
        self.uni.clickCommercial()
        time.sleep(3)
        self.uni.clickUnidashboard()
        time.sleep(5)

        # Search for created project
        self.uni.searchProject(DataTestForTestAddNewproject.projectName)
        self.uni.setPipeline(DataTestForTestAddNewproject.pipelineValue)
        time.sleep(4)
        names = self.uni.getProjectName()
        print(names)

        # Click project
        self.uni.clickProject(DataTestForTestAddNewproject.projectName)
        print(DataTestForTestAddNewproject.projectName)
        time.sleep(3)