Feature: tag

  Scenario: Assign a tag to a task and filter by tag
    Given I am logged into Todoist
    And I am on the "Filters and Tags" page
    When I create a new tag named "Work"
    And I return to the Inbox
    And I create a new task with the name "Finish report"
    And I assign the tag "Work" to the task "Finish report"
    And I filter tasks by the tag "Work"
    Then I should see the task "Finish report" in the filtered results


  Scenario: Create, edit, and delete a tag
    Given I am logged into Todoist
    And I am on the "Filters and Tags" page
    When I create a new tag named "Urgent"
    And I edit the tag "Urgent" to have the name "High Priority"
    And I delete the tag "High Priority"
    Then the tag "High Priority" should no longer exist