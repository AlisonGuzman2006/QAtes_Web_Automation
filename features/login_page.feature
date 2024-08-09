Feature: Todoist Login

  Scenario: Successful login with valid credentials
    Given the user is on the Todoist login page
    When the user enters a valid email "201604530@est.umss.edu"
    And the user enters a valid password "papasfritas"
    And the user clicks on the "Log in" button
    Then the user should be redirected to the Todoist dashboard
