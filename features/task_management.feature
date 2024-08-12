Feature: Task Management


  Background:
    Given the user is on the Todoist login page
    When the user enters a valid email "201604530@est.umss.edu"
    And the user enters a valid password "papasfritas"
    And the user clicks on the "Log in" button
    Then the user should be redirected to the Todoist dashboard

  Scenario: Create, edit, and delete a task
    Given the user is in the Today page dashboard for task management
    When the user creates a new task with title "New Task"
    And the user edits the task "New Task" to have title "Updated Task"
    And the user deletes the task "Updated Task"
    Then the task "Updated Task" should no longer appear in the task list

  Scenario: Mark a task as completed and verify in completed tasks list
    Given the user is in the Today page dashboard for task management
    When the user creates a new task with title "Complete Task"
    And the user marks the task "Complete Task" as completed
    And the user navigates to the Inbox dashboard
    Then the user should see the task "Complete Task" in the completed tasks list
