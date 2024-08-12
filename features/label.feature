Feature: label
 Scenario: Assign a label to a task and filter by label
  Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
  And I want to go to the filters and labels page
  And I am on the Filters and labels page
  When I create a new label "Michi"
  And I create a new task "Michiberto"
  Then I should see the task "Michiberto" created with the label assigned in the filtered results

 Scenario: Delete label
  Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
  And I want to go to the filters and labels page
  And I am on the Filters and labels page
  When I click on the delete option of the "Michi" label
  Then I should not see the "Michi" label