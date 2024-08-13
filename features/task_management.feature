Feature: Task Management


  Scenario: Edit a new task
    Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
    And the user is in the Today page dashboard for task management
    When the user creates a new task with title "New Task"
    And the user open the new task
    And the user edits the task with new title "new title"
    Then the user should see the new title task "new title"


  Scenario: Mark a task as completed
    Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
    And the user is in the Today page dashboard for task management
    When the user creates a new task with title "Complete Task"
    And the user open the new task
    And the user marks the task as completed
    Then the user should see a toast with the title "1 task completed"

  Scenario: Delete a new task
    Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
    And the user is in the Today page dashboard for task management
    When the user creates a new task with title "Delete Task"
    And the user open the new task
    And the user deletes the task created
    And the user goes to the Inbox dashboard
    Then the user should not see "Delete Task"
