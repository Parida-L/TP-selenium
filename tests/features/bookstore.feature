Feature: Search in the DemoQA Bookstore
  As a user of the DemoQA website
  I want to search for books in the bookstore
  So that I can verify the search functionality

  Scenario: Search for a book
    Given I navigate to the DemoQA website bookstore
    When I search for "Marijn Haverbeke"
    Then the books of author "Marijn Haverbeke" are displayed
