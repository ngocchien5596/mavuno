from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.Commercial.UnidashboardPage import UnidashboardPage
from utilities.customLogger import LogGen
import pytest
import time
from utilities.readPropertises import ReadConfig
from Configurations.dataTest import DataTestForTestAddNewproject

class Test_AddNewProject:

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_AddNewProject_FullFlow(self, setup):
        self.driver = setup

        #Login
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUser(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # time.sleep(3)

        #Select select menu
        self.uni = UnidashboardPage(self.driver)
        self.uni.clickCommercial()
        time.sleep(3)
        self.uni.clickUnidashboard()
        time.sleep(5)

        #Create new project
        self.uni.clickAddNew()
        time.sleep(7)
        self.uni.setProgramName(DataTestForTestAddNewproject.projectName)
        time.sleep(1)
        self.uni.setClient(DataTestForTestAddNewproject.client)
        time.sleep(1)
        self.uni.setCountry(DataTestForTestAddNewproject.country)
        time.sleep(1)
        self.uni.setValueChanin(DataTestForTestAddNewproject.valueChain)
        time.sleep(1)
        self.uni.setFirstPlantingDate(DataTestForTestAddNewproject.plantingDate)
        time.sleep(1)
        self.uni.setFirstHarvestDate(DataTestForTestAddNewproject.harvestDate)
        time.sleep(1)
        self.uni.setExpectedInvoiceDate(DataTestForTestAddNewproject.expectedDate)
        time.sleep(1)
        self.uni.clickNext()
        time.sleep(1)
        self.uni.setAge(DataTestForTestAddNewproject.age)
        time.sleep(1)
        self.uni.setSeason(DataTestForTestAddNewproject.season)
        time.sleep(1)
        self.uni.setProductType(DataTestForTestAddNewproject.productType)
        time.sleep(1)
        self.uni.setDealType(DataTestForTestAddNewproject.dealType)
        time.sleep(1)
        self.uni.setFinancialRelationship(DataTestForTestAddNewproject.financialRelationship)
        time.sleep(1)
        self.uni.setClientType(DataTestForTestAddNewproject.clientType)
        time.sleep(1)
        self.uni.setSector(DataTestForTestAddNewproject.sector)
        time.sleep(1)
        self.uni.setClientInsurance(DataTestForTestAddNewproject.clientInsurance)
        time.sleep(1)
        self.uni.setDecisionMaker(DataTestForTestAddNewproject.name, DataTestForTestAddNewproject.title, DataTestForTestAddNewproject.role, DataTestForTestAddNewproject.email, DataTestForTestAddNewproject.phoneNumber)
        time.sleep(1)
        self.uni.clickSaveDicisionmaker()
        time.sleep(1)
        self.uni.setClientAndDealInfo(DataTestForTestAddNewproject.clientAndDealInfo)
        time.sleep(1)
        self.uni.setHypothesis(DataTestForTestAddNewproject.hypothesis)
        time.sleep(1)
        self.uni.setCommercialFarm(DataTestForTestAddNewproject.commercialFarm)
        time.sleep(1)
        self.uni.setPulaValueIn2023inUSD(DataTestForTestAddNewproject.value1)
        time.sleep(1)
        self.uni.setPulaValueAtScaleInUSD(DataTestForTestAddNewproject.value2)
        time.sleep(1)
        self.uni.setPulaValueIn2024inUSD(DataTestForTestAddNewproject.value3)
        time.sleep(1)
        self.uni.setProbabilityToWin(DataTestForTestAddNewproject.value4)
        time.sleep(1)
        self.uni.setPulaValueCalculationDetails(DataTestForTestAddNewproject.details)
        time.sleep(1)
        self.uni.clickSave()
        time.sleep(7)
        self.uni.clickUnidashboard()
        time.sleep(5)

        #Search for created project
        self.uni.searchProject(DataTestForTestAddNewproject.projectName)
        self.uni.setPipeline(DataTestForTestAddNewproject.pipelineValue)
        time.sleep(4)
        names = self.uni.getProjectName()
        print(names)

        #Compare the search result
        if DataTestForTestAddNewproject.projectName in names:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
            #a