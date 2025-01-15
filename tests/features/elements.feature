Feature: DemoQA Elements Page
    As a user of DemoQA website 
    I want to interact with the Elements items 
    So that I can verify different functionality of Elements 

  Scenario: Select checkboxes except specific items
    Given I am on the "Checkbox" Elements page of DemoQA
    When I expand all the checkboxes
    And I select all checkboxes except "Office" and "Excel file.doc"
    Then only the selected checkboxes should remain checked
        
#   Scenario: Verify the web tables page 
# 	Given I navigate to the "Web Tables" on Elements page
#     When I delete the last two rows of the users table
#     And I update the salary of the remaining entry to "4300"
#     Then the table should reflect the updated salary 