import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#SCENARIO 1 - PROGRESS BAR 
@scenario('features/widgets.feature', 'Verify the progress bar')
def test_verify_progress_bar():
    pass

@given('I navigate to the progress bar widget DemoQA page')
def navigate_to_widgets_page(browser):
    browser.get("https://demoqa.com/progress-bar")
    assert "DEMOQA" in browser.title, f"Expected title to contain 'DEMOQA', but got '{browser.title}'"

@when('I start the progress bar')
def start_progress_bar(browser):
    start_button_locator = (By.ID, "startStopButton")
    start_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(start_button_locator)
    )
    time.sleep(2)
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", start_button)
    time.sleep(2)
    start_button.click()

@then('it should finish at "100%"')
def verify_progress_bar_completion(browser):
    progress_bar_locator = (By.CLASS_NAME, "progress-bar")
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element(progress_bar_locator, "100%"),
        message="Progress bar did not reach 100% within the timeout."
    )
    time.sleep(3)
    progress_bar = browser.find_element(*progress_bar_locator)
    #browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", progress_bar)
    time.sleep(3)
    assert progress_bar.text == "100%", f"Expected progress bar to show '100%', but got '{progress_bar.text}'"

#SCENARIO 2 - MENU BEHAVIOR
@scenario('features/widgets.feature', 'Verify the menu behavior')
def test_verify_menu_behavior():
    pass

@given('I navigate to the menu widget DemoQA page')
def navigate_to_menu_page(browser):
    browser.get("https://demoqa.com/menu")
    assert "DEMOQA" in browser.title, f"Expected title to contain 'DEMOQA', but got '{browser.title}'"

@when('I navigate the menu')
def navigate_to_sub_list(browser):
    main_item_2_locator = (By.XPATH, '//a[text()="Main Item 2"]')
    main_item_2 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(main_item_2_locator),
        message="Main Item 2 is not found on the page"
    )
    time.sleep(2)
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", main_item_2)
    ActionChains(browser).move_to_element(main_item_2).perform()

    sub_sub_list_locator = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
    sub_sub_list = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(sub_sub_list_locator),
        message="Sub Sub List is not found on the page",
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_sub_list)
    time.sleep(3)
    ActionChains(browser).move_to_element(sub_sub_list).perform()
    time.sleep(3)  # Allow time for hover effects
   

@then('I reach "Sub Sub Item 2" menu item')
def click_sub_sub_item_2(browser):
    sub_sub_item_2_locator = (By.XPATH, '//a[text()="Sub Sub Item 2"]')
    sub_sub_item_2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(sub_sub_item_2_locator),
        message="Sub Sub Item 2 is not found on the page"
    )
    time.sleep(1)  # Allow time for animations if applicable
    mouse_over_sub_sub_item = ActionChains(browser)
    mouse_over_sub_sub_item.move_to_element(sub_sub_item_2).perform()
    sub_sub_item_2.click()
    assert sub_sub_item_2, "Sub Sub Item 2 was not clicked successfully"

#SCENARIO 3 - SELECT MENU 
@scenario('features/widgets.feature', 'Verify Select menu')
def test_verify_select_menu():
    pass

@given('I navigate to the select menu widget on DemoQA website')
def navigate_to_select_menu_page(browser):
    browser.get("https://demoqa.com/select-menu")
    assert "DEMOQA" in browser.title, f"Expected title to contain 'DEMOQA', but got '{browser.title}'"

@when('I select "Option 1" in the "Select value" dropdown')
def select_another_root_option(browser):
    select_value_dropdown_locator = (By.XPATH, "//*[@id='withOptGroup']/div/div[1]")
    select_value_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(select_value_dropdown_locator),
        message="Select value dropdown is not found on the page"
    )
    time.sleep(3)
    browser.execute_script("arguments[0].scrollIntoView(true);", select_value_dropdown)
    time.sleep(3)
    select_value_dropdown.click()
    time.sleep(3)
    another_root_option_locator = (By.ID, "react-select-2-option-3")  
    another_root_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(another_root_option_locator),
        message="Another root option is not found in the dropdown"
    )
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView(true);", another_root_option)
    time.sleep(1)
    another_root_option.click()
    time.sleep(1)
    

@when('I select "Option 2" in the "Select one" dropdown')
def select_other_option(browser):
    select_one_dropdown_locator = (By.XPATH, '//*[@id="selectOne"]/div/div[1]')
    select_one_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(select_one_dropdown_locator),
        message="Select one dropdown is not found on the page"
    )
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView(true);", select_one_dropdown)
    time.sleep(1)
    select_one_dropdown.click()
    time.sleep(1)

    other_option_locator = (By.XPATH, '//div[@id="selectOne"]/div[2]/div/div/div[2]/div[6]')  
    other_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(other_option_locator),
        message="Other option is not found in the dropdown"
    )
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView(true);", other_option)
    time.sleep(1)
    other_option.click()

@when('I select "Option 3" in "Old Style Select Menu" dropdown')
def select_aqua_option(browser):
    old_style_select_menu_locator = (By.ID, "oldSelectMenu")
    old_style_select_menu = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(old_style_select_menu_locator),
        message="Old Style Select Menu dropdown is not found on the page"
    )
    time.sleep(1)
    # Use the Select class to interact with the dropdown
    select_menu = Select(old_style_select_menu)  # Initialize Select on the <select> element
    time.sleep(1)
    select_menu.select_by_visible_text("Aqua")  # Select the "Aqua" option by visible text
    time.sleep(1)

@when('I select "Option 4" and "Option 5" in "Multi Select Drop Down" dropdown')
def select_red_and_black_option(browser):
    multi_select_dropdown_locator = (By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]')
    multi_select_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(multi_select_dropdown_locator),
        message="Multi Select Drop Down is not found on the page"
    )
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView(true);", multi_select_dropdown)
    time.sleep(1)
    multi_select_dropdown.click()
    
    red_option_locator = (By.ID, "react-select-4-option-2")  
    red_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(red_option_locator),
        message="Red option is not found in the dropdown"
    )
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView(true);", red_option)
    time.sleep(1)
    red_option.click()

    black_option_locator = (By.ID, "react-select-4-option-3") 
    black_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(black_option_locator),
        message="Black option is not found in the dropdown"
    )
    time.sleep(1)
    black_option.click()

@then('the selected values should be displayed')
def verify_selected_values(browser):
    #Verify Select Value
    select_value_selected = browser.find_element(By.XPATH, '//*[@id="withOptGroup"]/div/div[1]/div[1]')
    assert select_value_selected.text == "Another root option", f"Expected selected value to be 'Another root option', but got '{select_value_selected.text}'"
    
    #Verify Select One
    select_one_selected = browser.find_element(By.XPATH, '//*[@id="selectOne"]/div/div[1]/div[1]')
    assert select_one_selected.text == "Other", f"Expected selected value to be 'Other', but got '{select_one_selected.text}'"

    #Verify Old Style Select Menu
    old_style_select_menu = browser.find_element(By.ID, "oldSelectMenu")
    select_menu = Select(old_style_select_menu) # Initialize Select on the <select> element
    # Assert the selected option is "Aqua"
    selected_option = select_menu.first_selected_option
    assert selected_option.text == "Aqua", f"Expected selected value to be 'Aqua', but got '{selected_option.text}'"

    # #Verify Multi Select Drop Down
    multi_select_dropdown_selected_black = browser.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[1]/div/div[1]')
    assert multi_select_dropdown_selected_black.text == "Black", f"Expected selected value to be 'Black', but got '{multi_select_dropdown_selected_black.text}'"
    multi_select_dropdown_selected_red = browser.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[2]/div/div[1]')
    assert multi_select_dropdown_selected_red.text == "Red", f"Expected selected value to be 'Red', but got '{multi_select_dropdown_selected_red.text}'"