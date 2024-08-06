Feature: task

  Scenario: Prioritize a task and filter by priority
    Given I am logged into Todoist
    And I am on the Inbox page
    When I create a new task named "Finish report" with priority "High"
    And I filter tasks by priority "High"
    Then I should see the task "Finish report" in the filtered results


  Scenario: Set a due date on a task and filter by date
    Given I am logged into Todoist
    And I am on the Inbox page
    When I create a new task named "Submit report" with a due date of "2024-08-10"
    And I filter tasks by due date "2024-08-10"
    Then I should see the task "Submit report" in the filtered results


  Scenario: Assign a team member to a task and filter by member
    Given I am logged into Todoist
    And I am on the Inbox page
    When I create a new task named "Prepare presentation"
    And I assign the task "Prepare presentation" to the team member "John Doe"
    And I filter tasks by the team member "John Doe"
    Then I should see the task "Prepare presentation" in the filtered results


  Scenario: Move a task to a different section
    Given I am logged into Todoist
    And I am on the Inbox page
    When I create a new task named "Plan meeting"
    And I find the task "Plan meeting" in the task list
    And I move the task "Plan meeting" to the section "Projects"
    Then I should see the task "Plan meeting" in the "Projects" section


  Scenario: Create, edit, and delete a task
    Given I am logged into Todoist
    And I am on the Inbox page
    When I create a new task named "Write blog post" with description "Draft the blog post for next week"
    And I find the task "Write blog post"
    And I edit the task description to "Complete the blog post for next week"
    And I delete the task "Write blog post"
    Then the task "Write blog post" should no longer exist


  Scenario: Mark a task as completed and filter by completed tasks
    Given I am logged into Todoist
    And I am on the Inbox page
    When I create a new task named "Read articles"
    And I mark the task "Read articles" as completed
    And I filter tasks by the completed status
    Then I should see the task "Read articles" in the filtered results