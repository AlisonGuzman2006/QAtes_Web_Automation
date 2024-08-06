Feature: Todoist Login

  Scenario: Successful login with valid credentials
    Given the user is on the Todoist login page
    When the user enters a valid email "user@example.com"
    And the user enters a valid password "password123"
    And the user clicks on the "Log in" button
    Then the user should be redirected to the Todoist dashboard
    And the user should see a welcome message "Welcome back!"