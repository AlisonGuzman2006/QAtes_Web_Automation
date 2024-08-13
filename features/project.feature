Feature: Project Management

Scenario: Duplicate existing project
    Given I am logged into Todoist with credentials "20170111@est.umss.edu" "password1707"
    And the user is in the team dashboard
    And the user creates a new project "pruebita1"
    When the user sees the options of a project
    Then the user duplicates the selected active project
    #Then I should see the duplicate of the project "Copy of <Project>" in the list projects of the Team.

Scenario: Create a new folder to project
    Given I am logged into Todoist with credentials "20170111@est.umss.edu" "password1707"
    And the user is in the team dashboard
    And the user creates a new project "pruebita2"
    When the user creates a new folder "foldercito1"
    And the user adds the created project to the new folder
    Then the user should see a pop-up message "Folder “project” has been created"






