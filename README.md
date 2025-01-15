# Découpage des Features en Gherkin

Ce document explique le découpage choisi pour l'énoncé disponible dans le fichier [enonce.md](./enonce.md). Chaque partie de l'énoncé est transformée en une **Feature Gherkin** avec ses scénarios associés. Le découpage permet de structurer clairement les interactions avec les différentes fonctionnalités de [DemoQA](https://demoqa.com).

Etapes : 
- Faire le test manuel
- relever les actions à faire 
- isoler la step qui bloque 
- Analyser le rapport d'erreur

---

## Features et Scénarios

### 1. Feature: DemoQA Elements Page

```gherkin
Feature: DemoQA Elements Page
    As a user of DemoQA website 
    I want to interact with the Elements items 
    So that I can verify different functionality of Elements 

  Scenario: Verify the checkbox page 
    Given I navigate to "Check box" on the Elements page
    When I click on all checkboxes except "Office" and "Excel doc"
    Then I select the checkboxes except "Office" and "Excel doc"
    
  Scenario: Verify the web tables page 
	Given I navigate to the "Web Tables" on Elements page
    When I delete the last two rows of the users table
    And I update the salary of the remaining entry to "4300"
    Then the table should reflect the updated salary 
```
