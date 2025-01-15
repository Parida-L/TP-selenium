# Découpage des Features en Gherkin

Ce document explique le découpage choisi pour l'énoncé disponible dans le fichier [enonce.md](./enonce.md). Chaque partie de l'énoncé est transformée en une **Feature Gherkin** avec ses scénarios associés. Le découpage permet de structurer clairement les interactions avec les différentes fonctionnalités de [DemoQA](https://demoqa.com).

Etapes :

- Faire le test manuel
- relever les actions à faire
- isoler la step qui bloque
- Analyser le rapport d'erreur

J'ai décidé de séparer les features par catégories. Les différents scénarios sont les différents éléments des catégories. Ainsi, la feature "Elements" va regrouper les scénarios des checkbox et des webtables. Ainsi si plus tard, je veux rajouter d'autres scénarios comme text box ou buttons, je peux le faire facilement sur la feature "Elements". 

---

## Features et Scénarios

### 1. Feature: DemoQA Elements Page

```gherkin
Feature: DemoQA Elements Page
    As a user of DemoQA website 
    I want to interact with the Elements items 
    So that I can verify different functionality of Elements 

  Scenario: Select checkboxes except specific items
    Given I am on the "Checkbox" Elements page of DemoQA
    When I expand all the checkboxes
    And I select all checkboxes except "Office" and "Excel file.doc"
    Then only the selected checkboxes should remain checked
        
  Scenario: Verify the web tables page 
      Given I navigate to the "Web Tables" on Elements page
      When I delete the last two rows of the users table
      And I update the salary of the remaining entry to "4300"
      Then the table should reflect the changes made
```

### 2. Feature: DemoQA Alerts, Windows, Browser Page

```gherkin
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
```

### 3. Feature: Widgets Page

```gherkin
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
```

### 4. Feature: Bookstore Page

```gherkin
Feature: Search in the DemoQA Bookstore
  As a user of the DemoQA website
  I want to search for books in the bookstore
  So that I can verify the search functionality

  Scenario: Search for a book
    Given I navigate to the DemoQA website bookstore
    When I search for "Marijn Haverbeke"
    Then the books of author "Marijn Haverbeke" are displayed
```