@ui @task @acceptance
Feature: Task Conduct

  Scenario: Move a task to a different section
    Given I am logged into Todoist with credentials "lclarosrocha@gmail.com" "papasfritas"
    And the user is in the Today page dashboard for task management
    When the user creates a new task with title "CATherine MICHIel"
    And the user open the new task
    Then the user moves the task created
    #Then the user should not see "CATherine"

Scenario: Assign a team member to a task and filter by member
    Given I am logged into Todoist with credentials "lclarosrocha@gmail.com" "papasfritas"
    And the user is in test in Qates project
    When the user creates a new task with title "CATherine MICHIel MIAUricio"
    And the user open the new task
    And I click on Assignee button
    And I assign the task to a team member
    And the user opens view filter panel
    And the user filters the task to be filter by selected assignee
    And the user filters the task to be filter by a team member
    Then the user should see the task created with the team member assigned in the filtered results

