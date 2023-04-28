Feature: Main page features

  Scenario: Verify Footer Links
    Given Open main page
    Then Verify each footer policy link opens correct page

  Scenario: Verify Email field
    Given Open main page
    When Enter email: abc in email field
    Then Verify an error message is displayed
    When Enter email: john@email.com in email field
    Then Verify subscription is successful