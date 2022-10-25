Feature: Form page

  Scenario: Correctly fill out form gives success
    Given I am on the Form page
    When I fill out the form correctly
    And I click Submit
    Then I am redirected to the Thanks page
    And I get a success message