Feature: DemoQA Windows Page
  As a user of DemoQA website 
  I want to interact with the Windows items 
  So that I can verify different functionality of Windows 

  Scenario: Verify the new tab is opened and closed
    Given I navigate to the "Browser" page of DemoQA
    When I open a new tab and close it
    Then I come back to the original tab

  Scenario: Verify the content in the large modal dialog
    Given I navigate to "Modal Dialogs" page of DemoQA
    When I open the large modal dialog
    Then it should contain "lorem ipsum" 4 times