from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Configurations.dataTest import DataTestForTestAddNewproject
from Configurations.locators import UnidashboardLocators


class UnidashboardPage:
    # commercial_xpath = UnidashboardLocators.commercial_xpath
    unidashboard_xpath = "(//span[normalize-space()='Unidashboard'])"
    button_addNew_xpath = "(//span[normalize-space()='+ Add new'])"
    textbox_programName_xpath = "(//input[@placeholder='Enter new program name'])"
    textbox_client_xpath = "(//input[@placeholder='Enter new client name'])"
    droplist_country_xpath = "(//div[contains(@class, 'modal-row') and contains(., 'Country')]//div[contains(@class, 'mavuno-searchable-selector')]//input)"
    droplist_valueChain_xpath = "//input[contains(@placeholder,'Add a value chain')]"
    datepicker_plantingDate_xpath = "//input[contains(@placeholder,'Click to select planting date')]"
    button_plantingDate_paginationNext_xpath = "//div[contains(@class,'modal-row') and contains(.,'First planting date')]//a[contains(@class,'pagination-next')]"
    datepicker_harvestDate_xpath = "//input[contains(@placeholder,'Click to select harvest date')]"
    button_harvestDate_paginationNext_xpath = "//div[contains(@class,'modal-row') and contains(.,'First harvest date')]//a[contains(@class,'pagination-next')]"
    datepicker_expectedInvoiceDate_xpath = "//input[contains(@placeholder,'Click to select expected invoice date')]"
    button_expectedInvoiceDate_paginationNext_xpath = "//div[contains(@class,'modal-row') and contains(.,'Expected invoice date')]//a[contains(@class,'pagination-next')]"
    button_next_xpath = "//button[contains(@class,'button action-btn is-primary')]//span[contains(.,'Next')]"
    textbox_ageOfProgram_xpath = "//input[contains(@placeholder,'e.g. 3 years')]"
    textbox_season_xpath = "//input[contains(@placeholder,'e.g. Long rain')]"
    droplist_productType_xpath = "//input[@placeholder='Add']"
    droplist_dealType_xpath = "//div[contains(@class,'modal-row') and contains(.,'Deal Type')]//select"
    droplist_financialRelationship_xpath = "//div[contains(@class,'modal-row') and contains(.,'What is the financial relationship between the client and their farmers (program type)')]//input"
    droplist_clientType_xpath = "//div[contains(@class,'modal-row') and contains(.,'Client type')]//input"
    droplist_sector_xpath = "//div[contains(@class,'modal-row') and contains(.,'Sector')]//select"
    textbox_clientInsurance_xpath = "//div[contains(@class,'modal-row') and contains(.,'What insurance is the client currently using (product type and insurance provider)')]//input"
    button_addDecisionMaker_xpath = "//div[contains(@class,'modal-row') and contains(.,'Key decision-maker (with contact details)')]//button"
    button_SaveDecisionMaker_xpath = "//div[contains(@class,'modal-card') and contains(.,'Key decision-maker contact details')]//button[contains(.,'Save')]"
    textarea_clientAndDealInfo_xpath = "//div[contains(@class,'modal-row') and contains(.,'Context information on client and deal')]//textarea"
    droplist_hypothesis_xpath = "//input[contains(@placeholder,'Add a hypothesis')]"
    droplist_commercialfarm_xpath = "//div[contains(@class,'modal-row') and contains(.,'Is this a commercial farm?')]//select"
    textbox_pulaValueIn2023inUSD_xpath = "//div[contains(@class,'modal-row') and contains(.,'Pula Value in 2023 in USD')]//input"
    textbox_pulaValueAtScaleInUSD_xpath = "//div[contains(@class,'modal-row') and contains(.,'Pula Value at scale in USD')]//input"
    textbox_pulaValueIn2024inUSD_xpath = "//div[contains(@class,'modal-row') and contains(.,'Pula Value in 2024 in USD')]//input"
    textbox_probabilityToWin_xpath = "//div[contains(@class,'modal-row') and contains(.,'Probability to win')]//input"
    textarea_pulaValueCalculationDetails_xpath = "//div[contains(@class,'modal-row') and contains(.,'Pula Value Calculation Details (TSI, Premium rate, Pula Fee rate)')]//textarea"
    button_save_xpath = "//button[contains(@class,'button action-btn is-primary')]//span[contains(.,'Save')]"
    textbox_searchProject_xpath = "//section//input[contains(@placeholder,'Search for project')]"
    droplist_pipeline_xpath = "//div[contains(@class,'field pipeline')]//select"

    def __init__(self, driver):
        self.driver = driver

    def clickCommercial (self):
        element = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, UnidashboardLocators.commercial_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.commercial_xpath).click()

    def clickUnidashboard (self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, UnidashboardLocators.unidashboard_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.unidashboard_xpath).click()

    def clickAddNew (self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, UnidashboardLocators.button_addNew_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH,self.button_addNew_xpath).click()

    def setProgramName (self, programName):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_programName_xpath).send_keys(programName)

    def setClient (self, client):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_client_xpath).send_keys(client)

    def setCountry(self, country):
        value_country_xpath = "(//div[contains(@class, 'modal-row') and contains(., 'Country')]//div[contains(@class, 'mavuno-searchable-selector')]//div[contains(@class, 'dropdown-menu')]//div[contains(@class,'dropdown-content')]//a[contains(@class,'dropdown-item')]//span)"
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_country_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_country_xpath).send_keys(country)
        time.sleep(1)
        self.driver.find_element(By.XPATH, value_country_xpath).click()
        time.sleep(1)

    def setValueChanin(self, valueChain):
        value_valueChain_xpath = "//div[contains(@class,'modal-row') and contains(.,'Value chain')]//a[contains(@class,'dropdown-item')]//span"
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_valueChain_xpath).send_keys(valueChain)
        time.sleep(1)
        self.driver.find_element(By.XPATH, value_valueChain_xpath).click()
        time.sleep(1)

    def setFirstPlantingDate(self,date):
        self.driver.find_element(By.XPATH, UnidashboardLocators.datepicker_plantingDate_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_plantingDate_paginationNext_xpath).click()
        time.sleep(1)
        value_datepicker_plantingDate_xpath = "//a[contains(@class,'datepicker-cell is-selectable')]//span[contains(.,'"+date+"')]"
        self.driver.find_element(By.XPATH, value_datepicker_plantingDate_xpath).click()
        time.sleep(1)

    def setFirstHarvestDate(self,date):
        self.driver.find_element(By.XPATH, UnidashboardLocators.datepicker_harvestDate_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_harvestDate_paginationNext_xpath).click()
        time.sleep(1)
        value_datepicker_harvestDate_xpath = "//div[contains(@class,'modal-row') and contains(.,'First harvest date')]//a[contains(@class,'datepicker-cell is-selectable')]//span[contains(.,'"+date+"')]"
        self.driver.find_element(By.XPATH, value_datepicker_harvestDate_xpath).click()
        time.sleep(1)

    def setExpectedInvoiceDate(self,date):
        self.driver.find_element(By.XPATH, UnidashboardLocators.datepicker_expectedInvoiceDate_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_expectedInvoiceDate_paginationNext_xpath).click()
        time.sleep(1)
        value_datepicker_expectedInvoiceDate_xpath = "//div[contains(@class,'modal-row') and contains(.,'Expected invoice date')]//a[contains(@class,'datepicker-cell is-selectable')]//span[contains(.,'"+date+"')]"
        self.driver.find_element(By.XPATH, value_datepicker_expectedInvoiceDate_xpath).click()
        time.sleep(1)

    def clickNext(self):
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_next_xpath).click()

    def setAge(self, age):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_ageOfProgram_xpath).send_keys(age)

    def setSeason(self, season):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_season_xpath).send_keys(season)

    def setProductType(self, producType):
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_productType_xpath).send_keys(producType)
        time.sleep(1)
        value_productType_xpath = "//div[contains(@class,'modal-row') and contains(.,'Product type')]//a"
        self.driver.find_element(By.XPATH, value_productType_xpath).click()
        time.sleep(1)

    def setDealType(self, dealType):
        select = Select(self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_dealType_xpath))
        select.select_by_visible_text(dealType)

    def setFinancialRelationship(self, financialRelationship):
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_financialRelationship_xpath).send_keys(financialRelationship)
        time.sleep(1)
        value_financialRelationship_xpath = "//div[contains(@class,'modal-row') and contains(.,'What is the financial relationship between the client and their farmers (program type)')]//a"
        self.driver.find_element(By.XPATH, value_financialRelationship_xpath).click()
        time.sleep(1)

    def setClientType(self, clientType):
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_clientType_xpath).send_keys(clientType)
        time.sleep(1)
        value_clientType_xpath = "//div[contains(@class,'modal-row') and contains(.,'Client type')]//a//span"
        self.driver.find_element(By.XPATH, value_clientType_xpath).click()
        time.sleep(1)

    def setSector(self, sector):
        select = Select(self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_sector_xpath))
        select.select_by_visible_text(sector)

    def setClientInsurance(self, clientInsurance):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_clientInsurance_xpath).send_keys(clientInsurance)

    def setDecisionMaker(self, name, title, role, email, phoneNumber):
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_addDecisionMaker_xpath).click()
        time.sleep(1)
        textbox_name_xpath = "//div[contains(@class,'modal-card') and contains(.,'Key decision-maker contact details')]//input[contains(@placeholder,'Name')]"
        textbox_title_xpath = "//div[contains(@class,'modal-card') and contains(.,'Key decision-maker contact details')]//input[contains(@placeholder,'Title')]"
        textbox_role_xpath = "//div[contains(@class,'modal-card') and contains(.,'Key decision-maker contact details')]//input[contains(@placeholder,'Role')]"
        textbox_email_xpath = "//div[contains(@class,'modal-card') and contains(.,'Key decision-maker contact details')]//input[contains(@placeholder,'Email')]"
        textbox_phoneNumber_xpath = "//div[contains(@class,'modal-card') and contains(.,'Key decision-maker contact details')]//input[contains(@placeholder,'Phone number')]"
        self.driver.find_element(By.XPATH, textbox_name_xpath).send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.XPATH, textbox_title_xpath).send_keys(title)
        time.sleep(1)
        self.driver.find_element(By.XPATH, textbox_role_xpath).send_keys(role)
        time.sleep(1)
        self.driver.find_element(By.XPATH, textbox_email_xpath).send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, textbox_phoneNumber_xpath).send_keys(phoneNumber)
        time.sleep(1)

    def clickSaveDicisionmaker(self):
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_SaveDecisionMaker_xpath).click()

    def setClientAndDealInfo(self, info):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textarea_clientAndDealInfo_xpath).send_keys(info)

    def setHypothesis(self, hypothesis):
        self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_hypothesis_xpath).send_keys(hypothesis)
        time.sleep(1)
        value_hypothesis_xpath = "//div[contains(@class,'modal-row') and contains(.,'Client pain points')]//a//span"
        self.driver.find_element(By.XPATH, value_hypothesis_xpath).click()
        time.sleep(1)

    def setCommercialFarm(self, commercialFarm):
        select = Select(self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_commercialfarm_xpath))
        select.select_by_visible_text(commercialFarm)

    def setPulaValueIn2023inUSD(self, value):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_pulaValueIn2023inUSD_xpath).send_keys(value)

    def setPulaValueAtScaleInUSD(self, value):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_pulaValueAtScaleInUSD_xpath).send_keys(value)

    def setPulaValueIn2024inUSD(self, value):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_pulaValueIn2024inUSD_xpath).send_keys(value)

    def setProbabilityToWin(self, value):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_probabilityToWin_xpath).send_keys(value)

    def setPulaValueCalculationDetails(self, details):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textarea_pulaValueCalculationDetails_xpath).send_keys(details)

    def clickSave(self):
        self.driver.find_element(By.XPATH, UnidashboardLocators.button_save_xpath).click()

    def searchProject(self, projectName):
        self.driver.find_element(By.XPATH, UnidashboardLocators.textbox_searchProject_xpath).send_keys(projectName)
        time.sleep(3)

    def setPipeline(self, pipelineValue):
        select = Select(self.driver.find_element(By.XPATH, UnidashboardLocators.droplist_pipeline_xpath))
        select.select_by_value(pipelineValue)

    def getProjectName(self):
        tr_xpath = "//div[contains(@class,'unidashboard-projects')]//tbody//tr"
        max = len(self.driver.find_elements(By.XPATH, tr_xpath))
        list_projectName = []
        for i in range(0, max):
            span_xpath = "//div[contains(@class,'unidashboard-projects')]//tbody//tr[" + str(i + 1) + "]//span[contains(@class,'name')]"
            list_projectName.append((self.driver.find_element(By.XPATH, span_xpath).text).split(" | "))
        names = [x[0] for x in list_projectName]
        return names

    def clickProject(self, projectNameTobeClicked):
        tr_xpath = "//div[contains(@class,'unidashboard-projects')]//tbody//tr"
        max = len(self.driver.find_elements(By.XPATH, tr_xpath))
        print('max: ', max)
        list_projectName = []
        for i in range(0, max):
            print(i+1)
            span_xpath = "//div[contains(@class,'unidashboard-projects')]//tbody//tr[" + str(i + 1) + "]//span[contains(@class,'name')]"
            list_projectName.append((self.driver.find_element(By.XPATH, span_xpath).text).split(" | "))
            names = [x[0] for x in list_projectName]
            print(list_projectName)
            print(names)
            if projectNameTobeClicked in names:
                self.driver.find_element(By.XPATH, span_xpath).click()

    def clickProject1(self, projectNameTobeClicked, names):
        span_xpath = "//div[contains(@class,'unidashboard-projects')]//tbody//tr//span[contains(.,'"+projectNameTobeClicked+"')]"
        if projectNameTobeClicked in names:
            self.driver.find_element(By.XPATH, span_xpath).click()

    def clickTab(self, tabName):
        acquisition_tab_xpath = "//a[contains(@id,'Acquisition-tab')]"
        tab_xpath = "//a[contains(@id,'"+tabName+"-tab')]"
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, acquisition_tab_xpath)))
        element.click()
        time.sleep(2)
        element1 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, tab_xpath)))
        element1.click()
        time.sleep(2)

    def checkMovementNextPhaseSuccess_OnUnidashboard(self, tabName):
        self.clickUnidashboard()
        time.sleep(7)
        print("clicked Unidashboard")
        self.clickTab(tabName)
        print("clicked tab name")
        time.sleep(5)
        names = self.getProjectName()
        # print(names)
        if DataTestForTestAddNewproject.projectName in names:
            return "Pass"
        else:
            return "Fail"

