@ui @task @acceptance
Feature: Task

  Scenarios related to tasks

  Scenario: Prioritize a task and filter by priority
    Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
    And the user is in the Today page dashboard
    When the user opens the new task form
    And the user fills in the task name
    And the user assigns any of the pre-defined priorities to the task
    And the user clicks the "add Task" button
    And the user opens view filter panel
    And the user filters the task to by seen by the priority selected
    Then the user should see the task created with the priority assigned in the filtered results

  Scenario: Set a due date on a task and filter by due date
    Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
    And the user is in the Today page dashboard
    When the user opens the new task form
    And the user fills in the task name
    And the user sets a due date to the task
    And the user clicks the "add Task" button
    And the user goes to the Inbox dashboard
    And the user opens view filter panel from Inbox dashboard
    And the user filters the task to be seen by due date
    Then the user should see the task created with the due date assigned in the filtered results
