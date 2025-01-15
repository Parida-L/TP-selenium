Feature: DemoQA Widget Page
  As a user of DemoQA website
  I want to interact with the progress bar
  So that I can verify its behavior

  Scenario: Verify the progress bar
    Given I navigate to the progress bar widget DemoQA page
    When I start the progress bar
    Then it should finish at "100%"

  Scenario: Verify the menu behavior
    Given I navigate to the menu widget DemoQA page
    When I navigate the menu 
    Then I reach "Sub Sub Item 2" menu item

  Scenario: Verify Select menu
    Given I navigate to the select menu widget on DemoQA website
    When I select "Option 1" in the "Select value" dropdown
    And I select "Option 2" in the "Select one" dropdown
    And I select "Option 3" in "Old Style Select Menu" dropdown
    And I select "Option 4" and "Option 5" in "Multi Select Drop Down" dropdown
    Then the selected values should be displayed
    