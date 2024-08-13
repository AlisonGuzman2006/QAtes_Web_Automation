Feature: filters
 Scenario: Create a filter and add to favorites
  Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
  And I want to go to the filters and labels page
  And I am on the Filters and labels page
  When I create a new filter
  And I added the filter to favorites
  Then I should see the text "Remove from favorites" inside the filter menu

 Scenario: Delete filter
  Given I am logged into Todoist with credentials "201604530@est.umss.edu" "papasfritas"
  And I want to go to the filters and labels page
  And I am on the Filters and labels page
  When I delete the filter "Tasks due next week"
  Then I should see the text "Your list of filters will show up here."

