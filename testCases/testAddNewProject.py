from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.Commercial.UnidashboardPage import UnidashboardPage
from utilities.customLogger import LogGen
import pytest
import time
from utilities.readPropertises import ReadConfig

class Test_AddNewProject:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    #Project info to create
    projectName = "Chien test auto 4"
    client = "MOA"
    country = "Vietnam"
    valueChain = "wheat"
    plantingDate = "20"
    harvestDate = "21"
    expectedDate = "22"
    age = "3"
    season = "Long rain 2023"
    productType = "Dry Run"
    dealType = "Dryrun (no premium paid)"
    financialRelationship = "Credit"
    clientType = "Government"
    sector = "Energy"
    clientInsurance = "Diachi Life"
    name = "Ngoc Chien"
    title = "Best staff"
    role = "Admin"
    email = "chienadmin@gmail.com"
    phoneNumber = "+84975788609"
    clientAndDealInfo = "This is info"
    hypothesis = " High Basis risk. "
    commercialFarm = "Hybrid"
    value1 = "10"
    value2 = "20"
    value3 = "30"
    value4 = "40"
    details = "Good"
    pipelineValue = "commercial"

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

        #Select right menu
        self.uni = UnidashboardPage(self.driver)
        self.uni.clickCommercial()
        time.sleep(3)
        self.uni.clickUnidashboard()
        time.sleep(5)

        #Create new project
        self.uni.clickAddNew()
        time.sleep(7)
        self.uni.setProgramName(self.projectName)
        time.sleep(1)
        self.uni.setClient(self.client)
        time.sleep(1)
        self.uni.setCountry(self.country)
        time.sleep(1)
        self.uni.setValueChanin(self.valueChain)
        time.sleep(1)
        self.uni.setFirstPlantingDate(self.plantingDate)
        time.sleep(1)
        self.uni.setFirstHarvestDate(self.harvestDate)
        time.sleep(1)
        self.uni.setExpectedInvoiceDate(self.expectedDate)
        time.sleep(1)
        self.uni.clickNext()
        time.sleep(1)
        self.uni.setAge(self.age)
        time.sleep(1)
        self.uni.setSeason(self.season)
        time.sleep(1)
        self.uni.setProductType(self.productType)
        time.sleep(1)
        self.uni.setDealType(self.dealType)
        time.sleep(1)
        self.uni.setFinancialRelationship(self.financialRelationship)
        time.sleep(1)
        self.uni.setClientType(self.clientType)
        time.sleep(1)
        self.uni.setSector(self.sector)
        time.sleep(1)
        self.uni.setClientInsurance(self.clientInsurance)
        time.sleep(1)
        self.uni.setDecisionMaker(self.name, self.title, self.role, self.email, self.phoneNumber)
        time.sleep(1)
        self.uni.clickSaveDicisionmaker()
        time.sleep(1)
        self.uni.setClientAndDealInfo(self.clientAndDealInfo)
        time.sleep(1)
        self.uni.setHypothesis(self.hypothesis)
        time.sleep(1)
        self.uni.setCommercialFarm(self.commercialFarm)
        time.sleep(1)
        self.uni.setPulaValueIn2023inUSD(self.value1)
        time.sleep(1)
        self.uni.setPulaValueAtScaleInUSD(self.value2)
        time.sleep(1)
        self.uni.setPulaValueIn2024inUSD(self.value3)
        time.sleep(1)
        self.uni.setProbabilityToWin(self.value4)
        time.sleep(1)
        self.uni.setPulaValueCalculationDetails(self.details)
        time.sleep(1)
        self.uni.clickSave()
        time.sleep(7)
        self.uni.clickUnidashboard()
        time.sleep(5)

        #Search for created project
        self.uni.searchProject(self.projectName)
        self.uni.setPipeline(self.pipelineValue)
        time.sleep(4)
        names = self.uni.getProjectName()
        print(names)

        #Compare the search result
        if self.projectName in names:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False