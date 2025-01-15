import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario
from selenium.common.exceptions import ElementClickInterceptedException

# Test Fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Scenario: Select checkboxes except specific items
@scenario('features/elements.feature', 'Select checkboxes except specific items')
def test_checkboxes():
    pass

@given('I am on the "Checkbox" Elements page of DemoQA')
def navigate_to_checkboxes_elements(browser):
    # Step 1: Navigate to DemoQA website
    browser.get("https://demoqa.com/")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")),message="DemoQA website is not accessible")
    assert browser.title == "DEMOQA", "Title does not match"
    # Step 2: Click on "Elements"
    element = browser.find_element(By.CLASS_NAME, 'card')
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)  # Allow time for the scrolling animation to complete
    element.click()
    # Step 3: Click on "Check Box"
    check_box_section = WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.XPATH, '//span[text()="Check Box"]')),message="Check Box section is not accessible")
    check_box_section.click()
    assert browser.find_element(By.XPATH, '//h1[text()="Check Box"]').text == 'Check Box', "Header does not match"

@when('I expand all the checkboxes')
def expand_checkboxes(browser):
    # Step 4: Expand all checkboxes with the + expand btn 
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rct-checkbox")),
        message="Checkboxes are not accessible"
        )
    expand_all_button = browser.find_element(By.CLASS_NAME, "rct-option-expand-all")
    expand_all_button.click()   

@when('I select all checkboxes except "Office" and "Excel file.doc"')
def select_checkboxes(browser):
    # Step 5: Select all checkboxes 
    home_checkbox_locator = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
    # wait for the home checkbox to be clickable
    home_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located(home_checkbox_locator),message="Home checkbox is not accessible")
    home_checkbox.click()
    time.sleep(1)  # Allow time for the checkbox to be selected
    home_checkbox_input_locator = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/input')
    home_checkbox_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located(home_checkbox_input_locator),message="Home checkbox input is not accessible")
    assert home_checkbox_input.is_selected(), "The 'Home' checkbox is not selected after clicking!"

    # Step 6: Deselect specific items

    #OFFICE CHECKBOX
    office_checkbox_locator = (By.CSS_SELECTOR, '.rct-node:nth-child(1) > ol:nth-child(2) > .rct-node:nth-child(2) > ol:nth-child(2) > .rct-node:nth-child(2) > .rct-text:nth-child(1) .rct-checkbox:nth-child(2) path:nth-child(1)')
    # wait for the office checkbox to be clickable
    office_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located(office_checkbox_locator),message="Office checkbox is not accessible")
    #scroll to the office checkbox
    browser.execute_script("arguments[0].scrollIntoView(true);", office_checkbox)
    time.sleep(1)  # Allow time for the scrolling animation to complete
    office_checkbox.click()
    time.sleep(1)  # Allow time for the checkbox to be deselected
    # ASSERTION: Verify that the Office checkbox is UNCHECKED 
    office_checkbox_input_locator = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]')
    office_checkbox_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located(office_checkbox_input_locator),message="Office checkbox INPUT is not accessible to verify")
    browser.execute_script("arguments[0].scrollIntoView(true);", office_checkbox_input)
    time.sleep(1)  # Allow time for the checkbox to be deselected
    assert not office_checkbox_input.is_selected(), "The 'Office' checkbox is selected !"

    #EXCEL CHECKBOX
    time.sleep(1)  # Allow time for the checkbox to be deselected
    excel_checkbox_locator = (By.CSS_SELECTOR, '.rct-node:nth-child(3) .rct-node:nth-child(2) .rct-checkbox path')  
    excel_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located(excel_checkbox_locator),message="Excel checkbox is not accessible")
    browser.execute_script("arguments[0].scrollIntoView(true);", excel_checkbox)
    time.sleep(1)  # Allow time for the scrolling animation to complete
    excel_checkbox.click()
    # ASSERTION: Verify that the Office checkbox is UNCHECKED
    time.sleep(1)  # Allow time for the checkbox to be deselected
    excel_checkbox_input_locator = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]')
    excel_checkbox_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located(excel_checkbox_input_locator),message="Excel checkbox input is not accessible")
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView(true);", excel_checkbox_input)
    assert not excel_checkbox_input.is_selected(), "The excel checkbox is still selected!"

@then('only the selected checkboxes should remain checked')
def verify_checkboxes(browser):
    # Step 7: Verify all checkboxes are selected
    home_checkbox_locator = (By.XPATH, '//div[@id="tree-node"]/ol[1]/li[@class="rct-node rct-node-parent rct-node-expanded"]/span[@class="rct-text"]//span[@class="rct-checkbox"]')
    home_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located(home_checkbox_locator),message="Home checkbox is not accessible")
    browser.execute_script("arguments[0].scrollIntoView(true);", home_checkbox)
    time.sleep(1)
    assert 'rct-checkbox' in home_checkbox.get_attribute('class'), "The home checkbox does not have the correct class!"
    
    # Step 8: Verify specific items are deselected
    office_checkbox_locator = (By.CSS_SELECTOR, 'svg.rct-icon.rct-icon-uncheck')
    office_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located(office_checkbox_locator),message="Office checkbox input is not accessible")
    browser.execute_script("arguments[0].scrollIntoView(true);", office_checkbox)
    time.sleep(1)
    assert office_checkbox.is_selected() == False, "Office checkbox is selected"
    # Autre possibilité
    # assert not office_checkbox.is_selected(), "Office checkbox is still selected"
  
    excel_checkbox = browser.find_element(By.CSS_SELECTOR, '.rct-node:nth-child(3) .rct-node:nth-child(2) .rct-checkbox path') 
    browser.execute_script("arguments[0].scrollIntoView(true);", excel_checkbox)
    time.sleep(1) 
    assert excel_checkbox.is_selected() == False, "Excel checkbox is selected"

#SCENARIO 2: Verify the web tables page
@scenario('features/elements.feature', 'Verify the web tables page')
def test_web_tables():
    pass

@given('I navigate to the "Web Tables" on Elements page')
def navigate_to_web_tables(browser):
    # Step 1: Navigate to DemoQA website
    browser.get("https://demoqa.com/")
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card-body")),
        message="DemoQA website is not accessible"
    )   
    assert browser.title == "DEMOQA", "Title does not match"
    # Step 2: Click on "Elements"
    element = browser.find_element(By.CLASS_NAME, 'card')
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)
    element.click()
    # Step 3: Click on "Web Tables"
    web_tables_section = WebDriverWait(browser, 10).until( 
        EC.presence_of_element_located((By.XPATH, '//span[text()="Web Tables"]')),
        message="Web Tables section is not accessible"
    )
    web_tables_section.click()
    assert browser.find_element(By.XPATH, '//h1[text()="Web Tables"]').text == 'Web Tables', "Header does not match"

@when('I delete the last two rows of the users table')
def delete_last_two_rows(browser):
    delete_row = browser.find_element(By.CSS_SELECTOR, '#delete-record-3 path')
    browser.execute_script("arguments[0].scrollIntoView(true);", delete_row)
    delete_row.click()
    delete_row2 = browser.find_element(By.CSS_SELECTOR, '#delete-record-2 path')
    browser.execute_script("arguments[0].scrollIntoView(true);", delete_row2)
    delete_row2.click()

@when('I update the salary of the remaining entry to "4300"')
def update_salary(browser):
    edit_button_locator = (By.CSS_SELECTOR, '.action-buttons span[title="Edit"]')
    edit_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(edit_button_locator),
        message="Edit button is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", edit_button)
    edit_button.click()

    salary_input_locator = (By.CSS_SELECTOR, '#salary')
    salary_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(salary_input_locator),
        message="Salary input is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", salary_input)
    salary_input.clear()
    time.sleep(2)
    salary_input.send_keys('4300')

    submit_button_locator = (By.ID, 'submit')
    submit_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(submit_button_locator),
        message="Submit button is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(2)
    # Check if the element is clickable
    try:
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(submit_button_locator),
            message="Submit button is not clickable"
        )
        submit_button.click()
    except ElementClickInterceptedException:
        print("DEBUG: Element click intercepted. Attempting to force click.")
        browser.execute_script("arguments[0].click();", submit_button)


@then('the table should reflect the changes made')
def verify_updated_salary(browser):
    salary_cell_locator = (By.CSS_SELECTOR, '.rt-tr-group:nth-child(1) .rt-td:nth-child(5)')
    salary_cell = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(salary_cell_locator),
        message="Salary cell is not accessible"
    )
    print(f"Salary displayed: {salary_cell.text}") 
    assert salary_cell.text == '4300', f"Expected salary to be '4300', but got '{salary_cell.text}'"
