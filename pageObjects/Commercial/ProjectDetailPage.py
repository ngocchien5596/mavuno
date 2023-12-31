from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Configurations.locators import *
from selenium.webdriver.common.action_chains import ActionChains


class ProjectDetail_detail:

    # Research stage
    def __init__(self, driver):
        self.driver = driver

    def clickProjectDetailTab(self):
        self.driver.find_element(By.XPATH, ProjectDetail.tab_projectDetail_detail_xpath).click()

    def setTsiType(self, tsiType):
        self.driver.find_element(By.XPATH, ProjectDetail.field_tsiType_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, ProjectDetail.droplist_tsiType_xpath))
        select.select_by_visible_text(tsiType)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.button_tsiType_save_xpath).click()
        time.sleep(0.5)

    def setDealChampion(self, name, title, role, email):
        self.driver.find_element(By.XPATH, ProjectDetail.button_addDealChampion_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.textbox_dealChampion_Name_xpath).send_keys(name)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.textbox_dealChampion_Title_xpath).send_keys(title)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.textbox_dealChampion_Role_xpath).send_keys(role)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.textbox_dealChampion_Email_xpath).send_keys(email)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.button_saveDealChampion_xpath).click()
        time.sleep(0.5)

    def setDonorGrant(self, value):
        self.driver.find_element(By.XPATH, ProjectDetail.field_donorGrant_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, ProjectDetail.droplist_donorGrant_xpath))
        select.select_by_visible_text(value)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.button_donorGrant_save_xpath).click()
        time.sleep(0.5)

    def setMeetingWithClient(self, value):
        self.driver.find_element(By.XPATH, ProjectDetail.field_meetingWithClient_xpath).click()
        time.sleep(1)
        print("clicked")
        # actions = ActionChains(self.driver)
        # actions.send_keys(value)
        # actions.perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, ProjectDetail.textarea_meetingWithClient_xpath).send_keys(value)
        print("typing")
        self.driver.find_element(By.XPATH, ProjectDetail.button_meetingWithClient_save_xpath).click()
        print("save")
        time.sleep(1)

    # Identification stage

    def getLenOfPhaseQuestions(self, phase):
        phase_content_xpath = "//div[contains(@id,'" + phase + "')]//div[contains(@class,'row-value')]"
        max_title = len(self.driver.find_elements(By.XPATH, phase_content_xpath))
        print("number of title: ",max_title)
        return max_title

    def setAnswers(self, phase, max, text):
        for i in range(0, max):
            print(phase, max)
            element_xpath = "//div[contains(@id,'"+phase+"')]//div[contains(@class,'row-value')]"
            element = self.driver.find_elements(By.XPATH, element_xpath)[i]
            element.click()
            print("Clicked",i)
            time.sleep(0.5)
            if element.find_elements(By.XPATH, './/select'):
                print("droplist")
                droplist_element = element_xpath + "//select"
                select = Select(self.driver.find_element(By.XPATH, droplist_element))
                select.select_by_index(1)
                self.driver.find_element(By.XPATH, ProjectDetail.button_save_question_xpath).click()
                time.sleep(2)
            else:
                print("textbox")
                actions = ActionChains(self.driver)
                actions.send_keys(text)
                time.sleep(0.5)
                actions.perform()
                time.sleep(0.5)
                self.driver.find_element(By.XPATH, ProjectDetail.button_save_question_xpath).click()
                time.sleep(2)

    def setAnswers1(self, phase, max, text):
        for i in range(0, max):
            print(phase, max)
            element_xpath = "//div[contains(@id,'"+phase+"')]//div[contains(@class,'row-value')]"
            element = self.driver.find_elements(By.XPATH, element_xpath)[i]
            actions = ActionChains(self.driver)
            actions.click(on_element=element)
            actions.perform()
            print("Clicked", i)
            time.sleep(0.5)
            if element.find_elements(By.XPATH, ".//input[contains(@placeholder,'Click to select date')]"):
                print("date-picker")
                datepicker_element = element_xpath + "//div[contains(@class,'datepicker control project-datepicker')]//input"

                button_datePicker_nextPage_xpath = "//div[contains(@class,'row-value')]//div[contains(@class,'datepicker control project-datepicker')]//a[contains(@class,'pagination-next')]"
                value_xpath = "//div[contains(@class,'row-value')]//div[contains(@class,'datepicker control project-datepicker')]//a[contains(@class,'datepicker-cell is-selectable')]//span[contains(.,'15')]"
                self.driver.find_element(By.XPATH, datepicker_element).click()
                time.sleep(0.5)
                self.driver.find_element(By.XPATH, button_datePicker_nextPage_xpath).click()
                time.sleep(0.5)
                self.driver.find_element(By.XPATH, value_xpath).click()
                time.sleep(0.5)
                self.driver.find_element(By.XPATH, ProjectDetail.button_save_question_xpath).click()
                time.sleep(2)
            elif element.find_elements(By.XPATH, './/select'):
                print("droplist")
                droplist_element = element_xpath + "//select"
                select = Select(self.driver.find_element(By.XPATH, droplist_element))
                select.select_by_index(2)
                print("Finish selecting droplist")
                self.driver.find_element(By.XPATH, ProjectDetail.button_save_question_xpath).click()
                print("Saved droplist")
                time.sleep(2)

            else:
                print("textbox")
                actions = ActionChains(self.driver)
                actions.send_keys(text)
                actions.perform()
                time.sleep(2)

class ProjectDetail_actors:
    def __init__(self, driver):
        self.driver = driver

    def scrollToElememt(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def clickProjectActorsTab(self):
        self.driver.find_element(By.XPATH, ProjectDetail.tab_projectDetail_actors_xpath).click()

    def setActors(self, actorTitle, actorName):
        field_actor_xpath = "//div[contains(@class,'row-data') and contains(.,'"+ actorTitle +"')]//div[contains(@class,'row-value')]"
        actorName_xpath = "//div[contains(@class,'row-data') and contains(.,'"+ actorTitle +"')]//a[contains(@class,'dropdown-item')]//span[contains(.,'"+actorName+"')]"
        self.driver.find_element(By.XPATH, field_actor_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, field_actor_xpath).click()
        time.sleep(0.5)
        action = ActionChains(self.driver)
        action.send_keys(actorName)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, actorName_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, ProjectDetail.button_save_question_xpath).click()
        time.sleep(0.5)

class MovePhase:
    def __init__(self, driver):
        self.driver = driver

    def hoverButtonActions(self):
        self.driver.find_element(By.XPATH, ProjectDetail.button_actions_xpath).click()

    def movePhase(self, phaseButtonText):
        button_phaseTitle_xpath = "//div[contains(@class,'dropdown dropdown-menu-animation is-hoverable is-mobile-modal') and contains(.,'Actions')]//a[contains(.,'"+phaseButtonText+"')]"
        if phaseButtonText == "Move to Qualifying":
            button_save_xpath = "//footer[contains(@class,'modal-card-foot')]//span[contains(.,'Save')]"
            self.driver.find_element(By.XPATH, button_phaseTitle_xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, button_save_xpath).click()
            time.sleep(3)
        if phaseButtonText == "Create RFQ":
            self.createRFQ()

        else:
            self.driver.find_element(By.XPATH, button_phaseTitle_xpath).click()
            time.sleep(1)
        return phaseButtonText

    def checkMovementNextPhaseSuccess_OnProjectDetail(self, phase):
        label_phaseText_xpath = "//p[contains(@class,'modal-card-title')]//span[contains(.,'"+phase+"')]"
        if self.driver.find_element(By.XPATH, label_phaseText_xpath):
            return "Pass"
        else:
            return "Fail"

    def createRFQ(self):
        print("Open pie page")

