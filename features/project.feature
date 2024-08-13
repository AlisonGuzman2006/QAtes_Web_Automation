Feature: Project Management

Scenario: Duplicate existing project
    Given I am logged into Todoist with credentials "20170111@est.umss.edu" "password1707"
    And the user is in the team dashboard
    And the user creates a new project "pruebita1"
    When the user sees the options of a project
    Then the user duplicates the selected active project


Scenario: Create a new folder to project
    Given I am logged into Todoist with credentials "20170111@est.umss.edu" "password1707"
    And the user is in the team dashboard
    And the user creates a new project "pruebita2"
    When the user creates a new folder "foldercito1"
    Then the user adds the created project to the new folder







