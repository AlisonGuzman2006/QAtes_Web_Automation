@ui @task @acceptance
Feature: task

  Scenarios related to tasks

  Scenario: Prioritize a task and filter by priority
    Given the user is in the Today page dashboard
    When the user opens the new task form
    And the user fills in the task name
    And the user assigns any of the pre-defined priorities to the task
    And the user clicks the "add Task" button
    And the user opens view filter panel
    And the user filters the task to by seen by the priority selected
    Then the user should see the task created with the priority assigned in the filtered results