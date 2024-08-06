Feature: Todoist Login

  Scenario: Successful login with valid credentials
    Given a web browser is at the todoist login page
    When a user enters the Todoist username "fernandezfreddy778@gmail.com" and the Todoist password "password1707" and clicks on the Todoist login button
    Then the Todoist url will contain "app.todoist.com"

  Scenario: Unsuccessful login with invalid credentials
    Given a web browser is at the todoist login page
    When a user provides incorrect Todoist credentials and clicks on the Todoist login button
      | username               | password       |
      | invalidUser1@gmail.com | wrongPassword1 |
      | invalidUser2@gmail.com | wrongPassword2 |
    Then the Todoist error message "Invalid email or password." is displayed

  Scenario: Login with empty username
    Given a web browser is at the todoist login page
    When a user enters an empty Todoist username and the Todoist password "somePassword" and clicks on the Todoist login button
    Then the Todoist error message "Email is required." is displayed

  Scenario: Login with empty password
    Given a web browser is at the todoist login page
    When a user enters the Todoist username "fernandezfreddy778@gmail.com" and an empty Todoist password and clicks on the Todoist login button
    Then the Todoist error message "Password is required." is displayed
