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

#SCENARIO  - BOOKSTORE 
@scenario('features/bookstore.feature', 'Search for a book')
def test_search_book():
    pass

@given('I navigate to the DemoQA website bookstore')
def navigate_to_bookstore_page(browser):
    # Navigate to the bookstore page
    browser.get("https://demoqa.com/books")
    assert "DEMOQA" in browser.title, f"Expected title to contain 'DEMOQA', but got '{browser.title}'"


@when('I search for "Marijn Haverbeke"')
def search_for_book(browser):
    # Verify that the search bar is present 
    search_bar_locator = (By.ID, "searchBox")
    search_bar = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(search_bar_locator),
        message="Search bar is not visible after navigating to the bookstore"
    )
    assert search_bar.is_displayed(), "Search bar is not displayed on the page"
    search_bar.send_keys("Marijn Haverbeke")
    search_button = browser.find_element(By.ID, "basic-addon2")
    search_button.click()

@then('the books of author "Marijn Haverbeke" are displayed')
def verify_search_results(browser):
    time.sleep(2)
    books = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]')
    for book in books:
        author = book.find_element(By.XPATH, './/div[@class="rt-td"][3]').text
        assert author == "Marijn Haverbeke", f"Expected author to be 'Marijn Haverbeke', but got '{author}'"