Feature: Switch window

  Scenario Outline: Correctly displayed the alert message
    Given I am on the switch-window page
    When I click on the open "<button>"
    Then I get the "This is a test alert!" is <status>

  Examples:
   | button | status |
   |alert-button| displayed|
   |new-tab-button| not displayed|
