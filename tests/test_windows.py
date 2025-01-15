import pytest
import time
from selenium import webdriver
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

# Scenario 1: Verify the new tab is opened and closed
@scenario('features/windows.feature', 'Verify the new tab is opened and closed')
def test_manage_windows_and_tabs(browser):
    pass 

@given('I navigate to the "Browser" page of DemoQA')
def navigate_to_browser_page(browser):
    browser.get("https://demoqa.com/alertsWindows")
    assert "DEMOQA" in browser.title, f"Expected title to contain 'DEMOQA', but got '{browser.title}'"
    #Wait for the Browser Windows button to be visible
    browser_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(.,"Browser Windows")]')),
        message="Browser Windows button is not visible after navigating to the page"
    )
    #Scroll to the Browser Windows button
    browser.execute_script("arguments[0].scrollIntoView(true);", browser_btn)
    browser_btn.click()
    # Verify the page header
    header_text = browser.find_element(By.XPATH, '//div[@id="browserWindows"]/h1').text
    assert header_text == "Browser Windows", f"Expected header to be 'Browser Windows', but got '{header_text}'"

@when('I open a new tab and close it')
def open_and_close_tab(browser):
    #Wait for the New Tab button to be visible
    new_tab_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='tabButton']")),
        message="New Tab button is not visible on the page"
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", new_tab_button)
    new_tab_button.click()
    # Verify the new tab is opened
    time.sleep(1)  # Allow time for the new tab to open
    browser.switch_to.window(browser.window_handles[1])  # Switch to the new tab
    assert "sample" in browser.current_url, f"Expected URL to contain 'sample', but got '{browser.current_url}'"
    # Close the tab
    time.sleep(2)  
    browser.close()


@then('I come back to the original tab')
def back_to_initial_browser(browser):
    # Switch back to the original tab
    browser.switch_to.window(browser.window_handles[0])
    # Verify we are back on the original tab
    assert "demoqa.com" in browser.current_url, f"Expected URL to contain 'demoqa.com', but got '{browser.current_url}'"


# Scenario 2: Verify the content in the large modal dialog
@scenario('features/windows.feature', 'Verify the content in the large modal dialog')
def test_verify_large_modal():
    pass

@given('I navigate to "Modal Dialogs" page of DemoQA')
def test_large_modal_contains_lorem_ipsum(browser):
    # Navigate to the "Modal Dialogs" page
    browser.get("https://demoqa.com/modal-dialogs")
    # Assert the page title
    assert "DEMOQA" in browser.title, f"Expected title to contain 'DEMOQA', but got '{browser.title}'"

@when('I open the large modal dialog')
def open_large_modal(browser):
    # Open the large modal dialog
    # Wait for the "Show Large Modal" button to be clickable
    large_modal_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "showLargeModal"))
    )
    #Scroll to the "Show Large Modal" button
    browser.execute_script("arguments[0].scrollIntoView(true);", large_modal_button)
    large_modal_button.click()

    # Verify the modal is displayed
    time.sleep(1)  # Allow time for the modal to appear
    # Wait for the modal to be visible
    large_modal = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", large_modal)
    time.sleep(1)  # Allow time for the modal to scroll into view
    # Verify the modal is displayed
    assert large_modal.is_displayed(), "Large modal is not displayed"

@then('it should contain "lorem ipsum" 4 times')
def verify_lorem_ipsum_in_modal(browser):
    # Verify the content of the modal
    time.sleep(2)  # Allow time for the modal content to load
    modal_body = browser.find_element(By.CLASS_NAME, "modal-body")
    # Check the text content of the modal
    modal_text = modal_body.text.lower()
    lorem_count = modal_text.count("lorem ipsum")
    assert lorem_count == 4, f"Expected 'lorem ipsum' to appear 4 times, but found {lorem_count}"

    # Close the modal
    time.sleep(1)  # Allow time for the modal content to be verified
    close_button = browser.find_element(By.ID, "closeLargeModal")
    browser.execute_script("arguments[0].scrollIntoView(true);", close_button)
    time.sleep(1)  # Allow time for the button to be clickable  
    close_button.click()

    # Ensure the modal is closed
    time.sleep(2)
    # Wait for the modal to be invisible
    WebDriverWait(browser, 5).until_not(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-body")),
        message="Modal is still visible after closing"
    )    
