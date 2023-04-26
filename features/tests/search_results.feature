Feature: Search results features

  Scenario: Search results show the right result
    Given Open main page
    When Click on search icon
    And Search for the SPF
    Then Verify the results have SPF