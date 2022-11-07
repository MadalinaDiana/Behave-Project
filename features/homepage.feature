Feature: Homepage

  Scenario: Redirect to Complete Web Form page
    Given I am on Homepage
    When I click "Complete Web Form" link
    Then I am redirected to Form Page

  Scenario: Redirect to Switch-window page
    Given I am on Homepage
    When I click "Switch Window" link
    Then I am redirected to switch-window page
