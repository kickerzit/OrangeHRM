@allure.feature 
Feature: Login

    Scenario: OK Login
    Given I am on the login page
    When I enter valid credentials
    And I press on the login button #ve stepech používáme @when. Tady je to, aby se to líp četlo
    Then I see that I am logged in

    Scenario: NON OK Login
    Given I am on the login page # ten už ve stepech mám, tudíž ho nemusím psát znovu
    When I enter invalid credentials
    And I press on the login button # ten už ve stepech mám taky, tudíž ho nepíšu
    Then I see error message