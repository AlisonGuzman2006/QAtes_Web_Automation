Feature: task

  Scenario: Assign a team member to a task and filter by member
    Given I am logged into Todoist
    And I am on Qates proyect page
    When I click on a proyect of Qates team
    And I click on Add task button
    And I write a new task name
    And I create the new task clicking on Add task button
    And I click in the new created task
    And I click on Assignee button
    And I assign the task to a team member
    And I close the information of the task
    And I click on filter button
    And I click on Assigne button located on 'Filter by' section
    And I click on "Selected asignees"
    And I click on "Choose assignees"
    And I select the team member whom I assigned the task
    And I close the assigness pop up clicking on an empty section of the page
    And I close the filter options pop up clicking on an empty section of the page
    Then I should see the task asiggned to the team member I assigned

  Scenario: Move a task to a different section
    Given I am logged into Todoist
    And I am on the Inbox page
    When I click on add task button
    And I write a new task name
    And I create the new task clicking on Add task button
    And I click in the new created task
    And I click on the Inbox button of the new task information pop up
    And I move the task created to another section
    Then I should see the name of the project I moved the task to in the project label in the task information

