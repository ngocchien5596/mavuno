from pageObjects.LoginPage import Login
from utilities.readPropertises import ReadConfig
import time
from pageObjects.Commercial.UnidashboardPage import UnidashboardPage
from pageObjects.Commercial.ProjectDetailPage import *
from Configurations.dataTest import *
class Test_ConfigProject:

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_Add_ProjectDetail(self, setup):
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
        # self.uni.searchProject("Chien test auto")
        self.uni.setPipeline(DataTestForTestAddNewproject.pipelineValue)
        time.sleep(7)
        # names = self.uni.getProjectName()

        # Click project
        self.uni.clickProject(DataTestForTestAddNewproject.projectName)
        time.sleep(3)

        # self.uni.clickProject1()
        # time.sleep(7)

        self.pdd = ProjectDetail_detail(self.driver)
        time.sleep(3)

        # # Fill for Research phase
        # self.pdd.setTsiType(DataForProjectDetail.tsiType)
        # print('tsiType')
        # time.sleep(0.5)
        # self.pdd.setDealChampion(DataForProjectDetail.name, DataForProjectDetail.title, DataForProjectDetail.role, DataForProjectDetail.email)
        # print('DealChampion')
        # time.sleep(0.5)
        # self.pdd.setDonorGrant(DataForProjectDetail.donorGrant)
        # print('donorGrant')
        # time.sleep(0.5)
        # self.pdd.setMeetingWithClient(DataForProjectDetail.meetingWithClient)
        # print('meetingWithClient')
        # time.sleep(0.5)

        # Fill answers for Identification phase
        numberOfQuestion = self.pdd.getLenOfPhaseQuestions("Identification")
        self.pdd.setAnswers("Identification", numberOfQuestion,DataForProjectDetail.text)
        time.sleep(3)

        # Fill answers for Engagement phase
        numberOfQuestion = self.pdd.getLenOfPhaseQuestions("Engagement")
        self.pdd.setAnswers1("Engagement", numberOfQuestion, DataForProjectDetail.text)
        time.sleep(3)

        # Fill answers for Budget Motivation phase
        numberOfQuestion = self.pdd.getLenOfPhaseQuestions("Budget Motivation")
        self.pdd.setAnswers("Budget Motivation", numberOfQuestion, DataForProjectDetail.text)
        time.sleep(3)

        # Fill answers for Qualifying phase
        numberOfQuestion = self.pdd.getLenOfPhaseQuestions("Qualifying")
        self.pdd.setAnswers("Qualifying", numberOfQuestion, DataForProjectDetail.text)
        time.sleep(3)
        
        self.pda = ProjectDetail_actors(self.driver)

        # # Scroll up
        # self.pda.scrollToElememt(ProjectDetail.tab_projectDetail_actors_xpath)
        # time.sleep(1)

        self.driver.execute_script("window.scrollTo(0, 100)")
        self.driver.save_screenshot("./Screenshots/1.png")

        # Click Actors tab
        self.pda.clickProjectActorsTab()
        time.sleep(1)

        # Select Field OPs Manager
        self.pda.setActors("Field OPs Manager", "kien1")

        # Select Project Configuration Lead
        self.pda.setActors("Project Configuration Lead", "fOpsConfiguration")

        # Select Data OPs Analyst
        self.pda.setActors("Data OPs Analyst", "DataOps")

        # Select Payout Actuary
        self.pda.setActors("Payout Actuary", "actuarial01")

        # Select Crop Development Analyst
        self.pda.setActors("Crop Development Analyst", "CropDevelopment1")

        # Select Call Center Agent
        self.pda.setActors("Call Center Agent", "CallCenterB")


        self.mp = MovePhase(self.driver)
        list_status = []

        # Move to Identification phase
        self.mp.hoverButtonActions()
        time.sleep(2)
        self.mp.movePhase("Move to Identification")
        time.sleep(4)
        # Check displaying Identification on the end of Project name on Project Detail
        list_status.append(self.mp.checkMovementNextPhaseSuccess_OnProjectDetail("Identification"))
        print(list_status)
        time.sleep(2)
        # Check displaying project on Identification tab
        list_status.append(self.uni.checkMovementNextPhaseSuccess_OnUnidashboard("Identification"))
        print(list_status)
        time.sleep(2)

        names = self.uni.getProjectName()
        # Click project
        self.uni.clickProject1(DataTestForTestAddNewproject.projectName, names)
        time.sleep(5)

        # Move to Engagement phase
        self.mp.hoverButtonActions()
        time.sleep(2)
        self.mp.movePhase("Move to Engagement")
        time.sleep(4)
        # Check displaying Engagement on the end of Project name on Project Detail
        list_status.append(self.mp.checkMovementNextPhaseSuccess_OnProjectDetail("Engagement"))
        print(list_status)
        time.sleep(2)
        # Check displaying project on Engagement tab
        list_status.append(self.uni.checkMovementNextPhaseSuccess_OnUnidashboard("Engagement"))
        print(list_status)
        time.sleep(2)

        names = self.uni.getProjectName()
        # Click project
        self.uni.clickProject1(DataTestForTestAddNewproject.projectName, names)
        time.sleep(5)

        if "Fail" not in list_status:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
