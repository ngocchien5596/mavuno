class UnidashboardLocators:
    commercial_xpath = "(//div[contains(text(),'Commercial')])"
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
    

class ProjectDetail:

# Tab Project Detail
    tab_projectDetail_detail_xpath = "//a[contains(@id,'details-tab')]"

    # Research stage
    field_tsiType_xpath = "//div[contains(@class,'row-data') and contains(.,'TSI Type')]//div[contains(@class,'row-value')]"
    droplist_tsiType_xpath = "//div[contains(@class,'row-data') and contains(.,'TSI Type')]//div[contains(@class,'row-value')]//select"
    button_tsiType_save_xpath = "//div[contains(@class,'row-data') and contains(.,'TSI Type')]//div[contains(@class,'action-group')]//span[contains(.,'Save')]"
    button_addDealChampion_xpath = "//div[contains(@class,'row-data') and contains(.,'Deal Champion')]//i"
    textbox_dealChampion_Name_xpath = "//input[contains(@placeholder,'Enter Deal Champion name')]"
    textbox_dealChampion_Title_xpath = "//input[contains(@placeholder,'Enter Deal Champion title')]"
    textbox_dealChampion_Role_xpath = "//input[contains(@placeholder,'Enter Deal Champion role')]"
    textbox_dealChampion_Email_xpath = "//input[contains(@placeholder,'Enter Deal Champion email address')]"
    button_saveDealChampion_xpath = "//button[contains(.,'Save')]"
    field_donorGrant_xpath = "//div[contains(@class,'row-data') and contains(.,'Is a donor/grant funding?')]//div[contains(@class,'row-value')]"
    droplist_donorGrant_xpath = "//div[contains(@class,'row-data') and contains(.,'Is a donor/grant funding?')]//div[contains(@class,'row-value')]//select"
    button_donorGrant_save_xpath = "//div[contains(@class,'row-data') and contains(.,'Is a donor/grant funding?')]//div[contains(@class,'action-group')]//span[contains(.,'Save')]"
    field_meetingWithClient_xpath = "//div[contains(@class,'row-data') and contains(.,'Hold at least 1 meetings with the client (provide dates, locations, physical/virtual, meeting notes)')]//div[contains(@class,'row-value')]"
    textarea_meetingWithClient_xpath = "//div[contains(@class,'row-data') and contains(.,'Hold at least 1 meetings with the client (provide dates, locations, physical/virtual, meeting notes)')]//div[contains(@class,'row-value')]//textarea"
    button_meetingWithClient_save_xpath = "//div[contains(@class,'row-data') and contains(.,'Hold at least 1 meetings with the client (provide dates, locations, physical/virtual, meeting notes)')]//div[contains(@class,'action-group')]//span[contains(.,'Save')]"

    # All phase
    # phase_content_xpath = "//div[contains(@id,'"+phase+"')]//div[contains(@class,'row-value')]"
    button_save_question_xpath = "//span[contains(@class,'icon has-text-success')]"

# Tab Project Actor

    tab_projectDetail_actors_xpath = "//a[contains(@id,'projectActors-tab')]"

# Move phase
    button_actions_xpath = "//button[contains(@class,'button is-info') and contains(.,'Actions')]"