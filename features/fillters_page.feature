Feature: filters
 Scenario: Assign a label to a task and filter by label
  Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
  And I want to go to the filters and labels page
  And I am on the Filters and labels page
  When I create a new filter
  And I added the filter to favorites
  Then I should see the text "Remove from favorites" inside the filter menu
