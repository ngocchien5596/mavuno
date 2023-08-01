from pageObjects.LoginPage import Login
from utilities.readPropertises import ReadConfig
import time
from pageObjects.Commercial.UnidashboardPage import UnidashboardPage
from pageObjects.Commercial.ProjectDetailPage import ProjectDetailPage
from Configurations.dataTest import *
class Test_ConfigProject:

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_Add_ProjectDetails(self, setup):
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
        time.sleep(7)
        names = self.uni.getProjectName()
        print(names)

        # Click project
        self.uni.clickProject(DataTestForTestAddNewproject.projectName)
        time.sleep(3)

        self.pd = ProjectDetailPage(self.driver)
        time.sleep(3)

        # Fill for Research phase
        self.pd.setTsiType(DataForProjectDetail.tsiType)
        print('tsiType')
        time.sleep(0.5)
        self.pd.setDealChampion(DataForProjectDetail.name, DataForProjectDetail.title, DataForProjectDetail.role, DataForProjectDetail.email)
        print('DealChampion')
        time.sleep(0.5)
        self.pd.setDonorGrant(DataForProjectDetail.donorGrant)
        print('donorGrant')
        time.sleep(0.5)
        self.pd.setMeetingWithClient(DataForProjectDetail.meetingWithClient)
        print('meetingWithClient')
        time.sleep(0.5)

        # Fill answers for Identification phase
        numberOfQuestion = self.pd.getLenOfPhaseQuestions("Identification")
        self.pd.setAnswers("Identification", numberOfQuestion,DataForProjectDetail.text)
        time.sleep(3)

        # Fill answers for Engagement phase
        numberOfQuestion = self.pd.getLenOfPhaseQuestions("Engagement")
        self.pd.setAnswers1("Engagement", numberOfQuestion, DataForProjectDetail.text)
        time.sleep(10)

        # Fill answers for Budget Motivation phase
        numberOfQuestion = self.pd.getLenOfPhaseQuestions("Budget Motivation")
        self.pd.setAnswers("Budget Motivation", numberOfQuestion, DataForProjectDetail.text)
        time.sleep(3)

        # Fill answers for Qualifying phase
        numberOfQuestion = self.pd.getLenOfPhaseQuestions("Qualifying")
        self.pd.setAnswers("Qualifying", numberOfQuestion, DataForProjectDetail.text)
        time.sleep(3)